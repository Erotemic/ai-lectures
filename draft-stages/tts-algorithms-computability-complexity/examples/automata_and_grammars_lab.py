#!/usr/bin/env python3
"""Executable teaching lab for algorithms lectures 007000-009000.

All claims about arbitrary word lengths require mathematical proofs in the
manuscripts. This script checks selected implementations on finite cases; no
bounded test certifies that a language is regular or context-free.

Python standard library only. Run with --check for a focused exhaustive check.
"""
from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from typing import Iterable, Mapping

ALPHABET = ('0', '1')


@dataclass(frozen=True)
class DFA:
    states: frozenset[str]
    initial: str
    finals: frozenset[str]
    transitions: Mapping[tuple[str, str], str]
    alphabet: tuple[str, ...] = ALPHABET

    def __post_init__(self) -> None:
        if self.initial not in self.states or not self.finals <= self.states:
            raise ValueError('Initial/accepting states outside state set')
        required = {(q, a) for q in self.states for a in self.alphabet}
        if set(self.transitions) != required:
            raise ValueError('DFA transition table is not complete')
        if not set(self.transitions.values()) <= self.states:
            raise ValueError('DFA transitions escape state set')

    def run(self, word: str) -> bool:
        state = self.initial
        for symbol in word:
            if symbol not in self.alphabet:
                raise ValueError(f'Unknown input symbol {symbol!r}')
            state = self.transitions[(state, symbol)]
        return state in self.finals

    def state_after(self, word: str) -> str:
        state = self.initial
        for a in word:
            state = self.transitions[(state, a)]
        return state


def end01_dfa() -> DFA:
    return DFA(
        frozenset(('s0', 's1', 's2')),
        's0', frozenset(('s2',)),
        {
            ('s0', '0'): 's1', ('s0', '1'): 's0',
            ('s1', '0'): 's1', ('s1', '1'): 's2',
            ('s2', '0'): 's1', ('s2', '1'): 's0',
        },
    )


def count1_mod3_dfa() -> DFA:
    return DFA(
        frozenset(('r0', 'r1', 'r2')),
        'r0', frozenset(('r0',)),
        {(f'r{i}', a): f'r{(i + (a == "1")) % 3}'
         for i in range(3) for a in ALPHABET},
    )


def product_dfa(a: DFA, b: DFA, operation: str) -> DFA:
    """Reachable product. Output states use unique encoded pairs."""
    if a.alphabet != b.alphabet:
        raise ValueError('alphabets differ')
    if operation not in {'intersection', 'union', 'xor'}:
        raise ValueError(operation)
    start = (a.initial, b.initial)
    queue = deque([start])
    seen = {start}
    transitions: dict[tuple[str, str], str] = {}
    finals: set[str] = set()
    while queue:
        pair = queue.popleft()
        name = repr(pair)
        in_a, in_b = pair[0] in a.finals, pair[1] in b.finals
        is_final = {'intersection': in_a and in_b,
                    'union': in_a or in_b,
                    'xor': in_a != in_b}[operation]
        if is_final:
            finals.add(name)
        for symbol in a.alphabet:
            dest = (a.transitions[(pair[0], symbol)],
                    b.transitions[(pair[1], symbol)])
            transitions[(name, symbol)] = repr(dest)
            if dest not in seen:
                seen.add(dest)
                queue.append(dest)
    return DFA(frozenset(map(repr, seen)), repr(start), frozenset(finals), transitions)


def shortest_acceptance_witness(dfa: DFA) -> str | None:
    """BFS witnesses nonemptiness, including possible empty-word acceptance."""
    queue = deque([(dfa.initial, '')])
    seen = {dfa.initial}
    while queue:
        q, word = queue.popleft()
        if q in dfa.finals:
            return word
        for a in dfa.alphabet:
            r = dfa.transitions[(q, a)]
            if r not in seen:
                seen.add(r)
                queue.append((r, word + a))
    return None


def shortest_disagreement(a: DFA, b: DFA) -> str | None:
    return shortest_acceptance_witness(product_dfa(a, b, 'xor'))


@dataclass(frozen=True)
class NFA:
    states: frozenset[str]
    initial: frozenset[str]
    finals: frozenset[str]
    # None is the epsilon symbol.
    transitions: Mapping[tuple[str, str | None], frozenset[str]]
    alphabet: tuple[str, ...] = ALPHABET

    def __post_init__(self) -> None:
        if not self.initial <= self.states or not self.finals <= self.states:
            raise ValueError('Invalid NFA state sets')
        for (q, a), targets in self.transitions.items():
            if q not in self.states or (a is not None and a not in self.alphabet):
                raise ValueError('Invalid NFA transition source/label')
            if not targets <= self.states:
                raise ValueError('Invalid NFA transition destination')

    def epsilon_closure(self, states: Iterable[str]) -> frozenset[str]:
        seen = set(states)
        pending = list(states)
        while pending:
            q = pending.pop()
            for r in self.transitions.get((q, None), frozenset()):
                if r not in seen:
                    seen.add(r)
                    pending.append(r)
        return frozenset(seen)

    def reachable_after(self, word: str) -> frozenset[str]:
        current = self.epsilon_closure(self.initial)
        for symbol in word:
            if symbol not in self.alphabet:
                raise ValueError(f'Unknown input symbol {symbol!r}')
            destinations = set()
            for q in current:
                destinations.update(self.transitions.get((q, symbol), frozenset()))
            current = self.epsilon_closure(destinations)
        return current

    def run(self, word: str) -> bool:
        return bool(self.reachable_after(word) & self.finals)


def suffix01_nfa() -> NFA:
    return NFA(
        frozenset(('q0', 'q1', 'q2')),
        frozenset(('q0',)), frozenset(('q2',)),
        {
            ('q0', '0'): frozenset(('q0', 'q1')),
            ('q0', '1'): frozenset(('q0',)),
            ('q1', '1'): frozenset(('q2',)),
        },
    )


def determinize(nfa: NFA) -> DFA:
    """Reachable subset construction with canonical repr of sorted states."""
    def name(states: frozenset[str]) -> str:
        return repr(tuple(sorted(states)))
    start = nfa.epsilon_closure(nfa.initial)
    queue = deque([start])
    seen = {start}
    delta: dict[tuple[str, str], str] = {}
    finals = set()
    while queue:
        current = queue.popleft()
        if current & nfa.finals:
            finals.add(name(current))
        for symbol in nfa.alphabet:
            successors = set()
            for q in current:
                successors.update(nfa.transitions.get((q, symbol), frozenset()))
            nxt = nfa.epsilon_closure(successors)
            delta[(name(current), symbol)] = name(nxt)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return DFA(frozenset(map(name, seen)), name(start), frozenset(finals),
               delta, nfa.alphabet)


def binary_words_through(max_length: int) -> Iterable[str]:
    for n in range(max_length + 1):
        for word in product(ALPHABET, repeat=n):
            yield ''.join(word)


def block_stack_accepts(word: str) -> bool:
    """Deterministic pushdown recognizer for {a^n b^n : n >= 0}."""
    phase = 'a'
    stack: list[str] = ['$']
    for symbol in word:
        if symbol == 'a' and phase == 'a':
            stack.append('X')
        elif symbol == 'b':
            phase = 'b'
            if stack[-1] != 'X':
                return False
            stack.pop()
        else:
            return False
    return stack == ['$']


def balanced_stack_accepts(word: str) -> bool:
    stack = []
    for symbol in word:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return not stack


# CNF grammar for {a^n b^n : n>=1}:
# S -> A B | A T; T -> S B; A -> a; B -> b.
TERMINAL_RULES = {'a': frozenset(('A',)), 'b': frozenset(('B',))}
BINARY_RULES = {
    ('A', 'B'): frozenset(('S',)),
    ('A', 'T'): frozenset(('S',)),
    ('S', 'B'): frozenset(('T',)),
}


def cyk_equal_nonempty(word: str) -> bool:
    """CYK membership for the displayed *fixed* grammar; epsilon is excluded."""
    n = len(word)
    if n == 0:
        return False
    if any(a not in TERMINAL_RULES for a in word):
        return False
    chart: dict[tuple[int, int], set[str]] = {}
    for i, a in enumerate(word):
        chart[i, i + 1] = set(TERMINAL_RULES[a])
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            out = set()
            for k in range(i + 1, j):
                for left in chart[i, k]:
                    for right in chart[k, j]:
                        out.update(BINARY_RULES.get((left, right), ()))
            chart[i, j] = out
    return 'S' in chart[0, n]


def count_plus_expression_trees(identifiers: int) -> int:
    """Number of parse trees for E->E+E|x on n occurrences of x."""
    if identifiers < 1:
        return 0

    @lru_cache(None)
    def count(n: int) -> int:
        if n == 1:
            return 1
        return sum(count(k) * count(n - k) for k in range(1, n))

    return count(identifiers)


def balanced_by_recursive_decomposition(word: str) -> bool:
    """Independent recognizer based on the grammar S -> (S)S | epsilon."""
    @lru_cache(None)
    def valid(text: str) -> bool:
        if not text:
            return True
        if text[0] != '(':
            return False
        depth = 0
        for i, a in enumerate(text):
            if a == '(':
                depth += 1
            elif a == ')':
                depth -= 1
            else:
                return False
            if depth == 0:
                return valid(text[1:i]) and valid(text[i + 1:])
            if depth < 0:
                return False
        return False
    return valid(word)


def run_checks() -> dict[str, int]:
    checks: dict[str, int] = {}
    ends = end01_dfa()
    mod = count1_mod3_dfa()
    nfa = suffix01_nfa()
    subset = determinize(nfa)
    intersection = product_dfa(ends, mod, 'intersection')
    union = product_dfa(ends, mod, 'union')
    xor = product_dfa(ends, mod, 'xor')

    for word in binary_words_through(10):
        good_ends = word.endswith('01')
        good_mod = word.count('1') % 3 == 0
        assert ends.run(word) == good_ends, word
        assert mod.run(word) == good_mod, word
        assert nfa.run(word) == good_ends, word
        assert subset.run(word) == good_ends, word
        assert intersection.run(word) == (good_mod and good_ends), word
        assert union.run(word) == (good_mod or good_ends), word
        assert xor.run(word) == (good_mod != good_ends), word
        checks['binary_words'] = checks.get('binary_words', 0) + 1
    assert ends.run('') is False
    assert mod.run('') is True
    assert ends.run('001001') is True
    assert mod.run('001001') is False
    assert shortest_disagreement(ends, ends) is None
    disagreement = shortest_disagreement(ends, intersection)
    assert disagreement is not None
    assert ends.run(disagreement) != intersection.run(disagreement)
    assert shortest_acceptance_witness(ends) == '01'
    checks['products_and_witnesses'] = 4

    # Exercise an actual epsilon edge, not only the closure implementation on
    # the suffix NFA (which happens to have no epsilon transitions).
    epsilon_nfa = NFA(
        frozenset(('p0', 'p1', 'p2')),
        frozenset(('p0',)), frozenset(('p2',)),
        {('p0', None): frozenset(('p1',)),
         ('p1', '1'): frozenset(('p2',))},
    )
    epsilon_dfa = determinize(epsilon_nfa)
    for word in binary_words_through(6):
        assert epsilon_nfa.run(word) == (word == '1')
        assert epsilon_dfa.run(word) == (word == '1')
        checks['epsilon_words'] = checks.get('epsilon_words', 0) + 1

    # Distinguishability tests demonstrate finite witnesses, not nonregularity.
    for i in range(16):
        for j in range(i + 1, 16):
            suffix = '1' * i
            in_equal_language = lambda w: w == '0' * (len(w) // 2) + '1' * (len(w) // 2) and len(w) % 2 == 0
            assert in_equal_language('0' * i + suffix)
            assert not in_equal_language('0' * j + suffix)
            checks['prefix_pairs'] = checks.get('prefix_pairs', 0) + 1

    for word in map(''.join, (p for n in range(13) for p in product('ab', repeat=n))):
        truth = bool(word) and word == 'a' * (len(word) // 2) + 'b' * (len(word) // 2) and len(word) % 2 == 0
        assert cyk_equal_nonempty(word) == truth, word
        assert block_stack_accepts(word) == (word == 'a' * (len(word) // 2) + 'b' * (len(word) // 2) and len(word) % 2 == 0), word
        checks['block_words'] = checks.get('block_words', 0) + 1
    for word in map(''.join, (p for n in range(13) for p in product('()', repeat=n))):
        assert balanced_stack_accepts(word) == balanced_by_recursive_decomposition(word), word
        checks['parenthesis_words'] = checks.get('parenthesis_words', 0) + 1
    assert [count_plus_expression_trees(n) for n in range(1, 6)] == [1, 1, 2, 5, 14]
    checks['ambiguity_cases'] = 5
    return checks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Run bounded exhaustive regression examples')
    args = parser.parse_args()
    if args.check:
        results = run_checks()
        print('OK: finite-state and stack/chart teaching examples')
        for name, number in results.items():
            print(f'  {name}: {number} cases')
        print('Bounded checks only; see lectures for proofs of general theorems.')
    else:
        print('Example: DFA for suffix 01 accepts 1101:', end01_dfa().run('1101'))
        print('Example: stack recognizer accepts aaabbb:', block_stack_accepts('aaabbb'))
        print('Use --check to run the bounded teaching examples.')


if __name__ == '__main__':
    main()
