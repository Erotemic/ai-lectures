#!/usr/bin/env python3
"""Reference algorithms for lectures 010000--012000.

All cases are finite checks, not proofs of a universal correctness or complexity
claim. This is deliberately independent of project runtime dependencies.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from dataclasses import dataclass
from itertools import product
from random import Random


def select_median_of_medians(values: list[int], k: int) -> int:
    """Return the zero-based k-th order statistic, counting duplicates."""
    if not 0 <= k < len(values):
        raise ValueError("rank must satisfy 0 <= k < len(values)")
    if len(values) <= 5:
        return sorted(values)[k]
    groups = [values[i:i + 5] for i in range(0, len(values), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]
    pivot = select_median_of_medians(medians, len(medians) // 2)
    low = [x for x in values if x < pivot]
    high = [x for x in values if x > pivot]
    num_equal = len(values) - len(low) - len(high)
    if k < len(low):
        return select_median_of_medians(low, k)
    if k < len(low) + num_equal:
        return pivot
    return select_median_of_medians(high, k - len(low) - num_equal)


def select_first_pivot(values: list[int], k: int) -> int:
    """Correct but sometimes quadratic: first element is always the pivot."""
    if not 0 <= k < len(values):
        raise ValueError("rank must satisfy 0 <= k < len(values)")
    pivot = values[0]
    low = [x for x in values if x < pivot]
    high = [x for x in values if x > pivot]
    equal = len(values) - len(low) - len(high)
    if k < len(low):
        return select_first_pivot(low, k)
    if k < len(low) + equal:
        return pivot
    return select_first_pivot(high, k - len(low) - equal)


@dataclass(frozen=True)
class Job:
    name: str
    start: int
    finish: int
    weight: int


def _sorted_jobs(jobs: list[Job]) -> list[Job]:
    if len({job.name for job in jobs}) != len(jobs):
        raise ValueError("job names must be distinct")
    if any(job.start >= job.finish or job.weight < 0 for job in jobs):
        raise ValueError("require start < finish and weight >= 0")
    return sorted(jobs, key=lambda j: (j.finish, j.start, j.name))


def feasible(jobs: list[Job]) -> bool:
    in_order = sorted(jobs, key=lambda j: (j.start, j.finish))
    return all(a.finish <= b.start for a, b in zip(in_order, in_order[1:]))


def greedy_earliest_finish(jobs: list[Job]) -> list[Job]:
    """Maximum *cardinality*, not maximum weight."""
    selected: list[Job] = []
    last_finish: int | None = None
    for job in _sorted_jobs(jobs):
        if last_finish is None or job.start >= last_finish:
            selected.append(job)
            last_finish = job.finish
    return selected


def dynamic_program_weighted(jobs: list[Job]) -> tuple[int, list[Job], list[int], list[int]]:
    """Return (optimal value, witness, DP prefix table, predecessor counts)."""
    ordered = _sorted_jobs(jobs)
    ends = [job.finish for job in ordered]
    pred: list[int] = []
    for i, job in enumerate(ordered):
        pred.append(bisect_right(ends, job.start, 0, i))
    dp = [0] * (len(ordered) + 1)
    for j in range(1, len(ordered) + 1):
        job = ordered[j - 1]
        dp[j] = max(dp[j - 1], job.weight + dp[pred[j - 1]])
    chosen: list[Job] = []
    j = len(ordered)
    while j:
        job = ordered[j - 1]
        include = job.weight + dp[pred[j - 1]]
        if include > dp[j - 1]:
            chosen.append(job)
            j = pred[j - 1]
        else:
            j -= 1
    chosen.reverse()
    return dp[-1], chosen, dp, pred


def brute_schedule(jobs: list[Job]) -> tuple[int, int]:
    """An independent subset enumerator; for small instances only."""
    best_weight = 0
    best_size = 0
    for bits in product((False, True), repeat=len(jobs)):
        subset = [job for bit, job in zip(bits, jobs) if bit]
        if not feasible(subset):
            continue
        best_weight = max(best_weight, sum(job.weight for job in subset))
        best_size = max(best_size, len(subset))
    return best_weight, best_size


def check() -> None:
    sample = [17, 5, 14, 2, 9, 20, 11, 7, 3, 16, 4, 8, 13, 6, 10]
    assert select_median_of_medians(sample, 7) == 9
    assert select_median_of_medians(sample, 10) == 13
    assert sample == [17, 5, 14, 2, 9, 20, 11, 7, 3, 16, 4, 8, 13, 6, 10]
    exhaustive_arrays = 0
    checked_ranks = 0
    for n in range(0, 8):
        for tup in product((-1, 0, 1, 2), repeat=n):
            values = list(tup)
            exhaustive_arrays += 1
            for k, expected in enumerate(sorted(values)):
                assert select_median_of_medians(values, k) == expected
                assert select_first_pivot(values, k) == expected
                checked_ranks += 1
    rng = Random(20261115)
    for _ in range(750):
        n = rng.randrange(1, 141)
        arr = [rng.randrange(-20, 21) for _ in range(n)]
        k = rng.randrange(n)
        assert select_median_of_medians(arr, k) == sorted(arr)[k]
    for values, k in (([], 0), ([1, 2], -1), ([1], 1)):
        try:
            select_median_of_medians(values, k)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid rank was accepted")

    # Trace from lecture 011000: sorted by (finish, start, name).
    trace = [
        Job("A", 0, 2, 4), Job("C", 0, 4, 12), Job("B", 2, 4, 4),
        Job("D", 4, 6, 5), Job("E", 3, 7, 7),
    ]
    weight, witness, table, predecessor = dynamic_program_weighted(trace)
    assert table == [0, 4, 12, 12, 17, 17], table
    assert predecessor == [0, 0, 1, 3, 1], predecessor
    assert weight == 17 and [job.name for job in witness] == ["C", "D"]
    assert feasible(witness) and sum(job.weight for job in witness) == weight
    assert brute_schedule(trace) == (17, 3)

    # Different objectives, same time intervals (lecture 012000).
    weighted_first_failure = [Job("A", 0, 2, 4), Job("B", 2, 4, 4), Job("C", 0, 4, 12)]
    assert len(greedy_earliest_finish(weighted_first_failure)) == 2
    assert sum(x.weight for x in greedy_earliest_finish(weighted_first_failure)) == 8
    assert dynamic_program_weighted(weighted_first_failure)[0] == 12
    heavy_first_failure = [Job("A", 0, 2, 6), Job("B", 2, 4, 6), Job("C", 0, 4, 11)]
    assert dynamic_program_weighted(heavy_first_failure)[0] == 12
    assert not feasible([heavy_first_failure[2], heavy_first_failure[0]])
    assert not feasible([heavy_first_failure[2], heavy_first_failure[1]])
    start_failure = [Job("long", 0, 10, 0), Job("a", 1, 2, 0), Job("b", 2, 3, 0), Job("c", 3, 4, 0)]
    assert len(greedy_earliest_finish(start_failure)) == 3
    assert brute_schedule(start_failure)[1] == 3
    duration_failure = [Job("a", 0, 3, 0), Job("short", 2, 4, 0), Job("c", 3, 6, 0)]
    assert len(greedy_earliest_finish(duration_failure)) == 2
    assert brute_schedule(duration_failure)[1] == 2

    # Exhaustive subsets of ten interval shapes, with four weight assignments.
    shapes = [(s, f) for s in range(-1, 4) for f in range(s + 1, 5)]
    shapes = shapes[:10]
    checked_schedules = 0
    for scheme in range(4):
        universe = [
            Job(str(i), start, finish, (3 * i + 2 * scheme + i * scheme) % 9)
            for i, (start, finish) in enumerate(shapes)
        ]
        for mask in range(1 << len(universe)):
            jobs = [job for i, job in enumerate(universe) if (mask >> i) & 1]
            greedy = greedy_earliest_finish(jobs)
            value, witness, dp, pred = dynamic_program_weighted(jobs)
            expected_value, expected_count = brute_schedule(jobs)
            assert feasible(greedy) and len(greedy) == expected_count
            assert value == expected_value and feasible(witness)
            assert sum(job.weight for job in witness) == value
            assert dp[-1] == value and len(pred) == len(jobs)
            checked_schedules += 1
    print(
        "OK: selection checked on", exhaustive_arrays,
        "arrays /", checked_ranks, "ranks plus 750 seeded cases;",
        "scheduling checked on", checked_schedules,
        "exhaustively enumerated interval instances"
    )
    print("These are bounded implementation checks, not machine-checked universal proofs.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run bounded independent-oracle checks")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        print("Use --check to run the reference checks for lectures 010000--012000.")


if __name__ == "__main__":
    main()
