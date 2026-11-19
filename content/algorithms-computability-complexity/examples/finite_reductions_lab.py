#!/usr/bin/env python3
"""Tiny *finite-trace* laboratory for recognizers and mapping reductions.

This is an original teaching simulator, NOT a proof of undecidability, not a
Turing machine universal interpreter, and not a procedure for detecting
unbounded nontermination. An exhausted fuel budget means UNKNOWN.

Commands (each occupies one program counter slot):
  ("ACCEPT",)                 halt accepting
  ("REJECT",)                 halt rejecting
  ("JUMP", address)           unconditional branch
  ("DECJZ", zero, positive)   if register=0 jump to zero;
                               otherwise decrement and jump to positive
  ("INC", address)           increment register and jump

Input is a nonnegative integer used to initialize one unbounded counter.
Source-to-source mappings preserve instruction addresses and the register.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Literal, TypeAlias

Instruction: TypeAlias = tuple[str, ...] | tuple[str, int] | tuple[str, int, int]
Program: TypeAlias = tuple[Instruction, ...]
Outcome = Literal['ACCEPT', 'REJECT', 'UNKNOWN']


@dataclass
class State:
    pc: int
    value: int
    outcome: Outcome = 'UNKNOWN'


def step(program: Program, state: State) -> State:
    """Execute exactly one instruction; UNKNOWN means 'not yet halted'."""
    if state.outcome != 'UNKNOWN':
        return state
    if not (0 <= state.pc < len(program)):
        raise ValueError('ill-formed instruction pointer: use explicit halts')
    op, *args = program[state.pc]
    if op == 'ACCEPT':
        return State(state.pc, state.value, 'ACCEPT')
    if op == 'REJECT':
        return State(state.pc, state.value, 'REJECT')
    if op == 'JUMP':
        return State(args[0], state.value)
    if op == 'INC':
        return State(args[0], state.value + 1)
    if op == 'DECJZ':
        return (State(args[0], state.value) if state.value == 0
                else State(args[1], state.value - 1))
    raise ValueError(f'unknown opcode: {op}')


def simulate(program: Program, input_value: int, fuel: int) -> Outcome:
    if input_value < 0 or fuel < 0:
        raise ValueError('input and fuel must be nonnegative')
    state = State(0, input_value)
    for _ in range(fuel):
        state = step(program, state)
        if state.outcome != 'UNKNOWN':
            return state.outcome
    return 'UNKNOWN'


def acceptance_to_halting(program: Program) -> Program:
    """Total syntactic map: ACCEPT preserved; REJECT changed to a self-loop.

    For each input n, original program ACCEPTS iff mapped program HALTS.
    This equivalence follows from instruction semantics; finite tests sample it.
    """
    return tuple(('JUMP', address) if instr[0] == 'REJECT' else instr
                 for address, instr in enumerate(program))


def halting_to_acceptance(program: Program) -> Program:
    """Total syntactic map: any original terminal halt becomes acceptance.

    For each input n, original program HALTS iff mapped program ACCEPTS.
    """
    return tuple(('ACCEPT',) if instr[0] == 'REJECT' else instr
                 for instr in program)


def decide_zero_by_dovetail(input_value: int, fuel: int = 10) -> bool:
    """Two complementary recognizers; one accepts zero, other positive.

    Each recognizer deliberately loops on the side it does not recognize.
    Interleaving their steps nevertheless decides which side this input is on.
    """
    zero_recognizer: Program = (
        ('DECJZ', 1, 2), ('ACCEPT',), ('JUMP', 2),
    )
    positive_recognizer: Program = (
        ('DECJZ', 1, 2), ('JUMP', 1), ('ACCEPT',),
    )
    r, s = State(0, input_value), State(0, input_value)
    for _ in range(fuel):
        r = step(zero_recognizer, r)
        s = step(positive_recognizer, s)
        if r.outcome == 'ACCEPT':
            return True
        if s.outcome == 'ACCEPT':
            return False
    raise RuntimeError('fuel exhausted; insufficient evidence, not a false result')


SAMPLES: tuple[tuple[str, Program, int, Outcome], ...] = (
    ('accept', (('ACCEPT',),), 0, 'ACCEPT'),
    ('reject', (('REJECT',),), 0, 'REJECT'),
    ('self-loop', (('JUMP', 0),), 0, 'UNKNOWN'),
    ('countdown-accept', (
        ('DECJZ', 2, 1), ('JUMP', 0), ('ACCEPT',)), 4, 'ACCEPT'),
    ('countdown-reject', (
        ('DECJZ', 2, 1), ('JUMP', 0), ('REJECT',)), 3, 'REJECT'),
    ('countdown-loop', (
        ('DECJZ', 2, 1), ('JUMP', 0), ('JUMP', 2)), 3, 'UNKNOWN'),
    ('increment-loop', (('INC', 0),), 0, 'UNKNOWN'),
)


def check() -> None:
    budget = 80
    for name, source, initial, expected in SAMPLES:
        observed = simulate(source, initial, budget)
        assert observed == expected, (name, observed, expected)
        mapped_a = simulate(acceptance_to_halting(source), initial, budget)
        mapped_h = simulate(halting_to_acceptance(source), initial, budget)
        if expected == 'ACCEPT':
            assert mapped_a in ('ACCEPT', 'REJECT')
            assert mapped_h == 'ACCEPT'
        elif expected == 'REJECT':
            assert mapped_a == 'UNKNOWN'  # deliberately inserted self-loop
            assert mapped_h == 'ACCEPT'
        else:
            assert mapped_a == 'UNKNOWN' and mapped_h == 'UNKNOWN'
        print(f'{name:18s} original={observed:7s} '
              f'accept->halt={mapped_a:7s} halt->accept={mapped_h:7s}')
    for n in range(20):
        assert decide_zero_by_dovetail(n) is (n == 0)
    print('OK: 7 finite-trace examples and 20 two-recognizer scheduling examples')
    print('UNKNOWN = no halt observed within the finite fuel budget.')
    print('These runs do not certify nontermination or a universal theorem.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='run bounded educational examples')
    args = parser.parse_args()
    if args.check:
        check()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
