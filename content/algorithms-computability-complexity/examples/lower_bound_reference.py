#!/usr/bin/env python3
"""Original, minimal lower-bound algorithm and independent bounded checker.

The mathematical domain is a nondecreasing finite sequence of integers and an
integer target. The proof in lecture 003000 establishes full-domain correctness
under its abstract assumptions. This script checks finite instances only.
"""

from __future__ import annotations

import argparse
from itertools import combinations_with_replacement
from typing import Sequence


def lower_bound(values: Sequence[int], target: int) -> int:
    """First i with values[i] >= target, or len(values) if none exists.

    Precondition: values is sorted nondecreasingly. It is not checked here.
    """
    low = 0
    high = len(values)
    while low < high:
        mid = low + (high - low) // 2
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def specification(values: Sequence[int], target: int) -> int:
    """Independent linear-search specification of the result."""
    for index, value in enumerate(values):
        if value >= target:
            return index
    return len(values)


def count_comparisons(values: Sequence[int], target: int) -> tuple[int, int]:
    """Instrument same decisions to count element/target comparisons."""
    low = 0
    high = len(values)
    count = 0
    while low < high:
        mid = low + (high - low) // 2
        count += 1
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low, count


def check() -> None:
    cases = 0
    domain = (-2, -1, 0, 1, 2)
    for length in range(0, 9):
        for values in combinations_with_replacement(domain, length):
            for target in range(-3, 4):
                got = lower_bound(values, target)
                want = specification(values, target)
                instrumented, comparisons = count_comparisons(values, target)
                assert got == want == instrumented, (values, target, got, want)
                assert 0 <= got <= len(values)
                assert all(v < target for v in values[:got])
                assert all(v >= target for v in values[got:])
                # ceil(log2(n+1)) = n.bit_length() for nonnegative n.
                assert comparisons <= len(values).bit_length()
                cases += 1
    assert lower_bound((1, 2, 2, 5), 2) == 1
    assert lower_bound((1, 2, 2, 5), 3) == 3
    assert lower_bound((1, 2, 2, 5), 6) == 4
    print(f"OK: {cases} bounded input/target cases; no random input required")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='run bounded checks')
    args = parser.parse_args()
    if args.check:
        check()
    else:
        values = (1, 2, 2, 5)
        for target in (0, 2, 3, 6):
            print(f"lower_bound({values}, {target}) = {lower_bound(values, target)}")


if __name__ == '__main__':
    main()
