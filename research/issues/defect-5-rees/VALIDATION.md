# Defect-Five Validation Record

## Commands

```text
python3 -m py_compile research/issues/defect-5-rees/validate_defect5.py
python3 research/issues/defect-5-rees/validate_defect5.py
```

## Observed local output

```text
defect-five validator mode: independent-from-defect-four
primitive weights enumerated (1 <= p <= q <= 120): 4386
interior systems with exponent-one top descent: 1092
arithmetic no-descent cases killed by empty root support: 16024
formal no-descent systems constructed through S_5: 428
zero layers generated: 982
systems admitting multiple symbolic resonant brackets: 6
no-descent support families: 18
exact saturated Groebner eliminations: 8
largest Groebner input: 14 equations, 19 variables
semantic corruptions detected: 5
exact rational/algebraic Keller-Rees trials: 15
formal complete-staircase survivors resisting declared descent: 0
defect-five exact symbolic validation: PASS
mathematical authority: HUMAN DERIVATION AND REVIEW STATUS, NOT CHECK COUNTS
```

The elapsed time is intentionally omitted from the pinned expectation because it
is environment-dependent.

## Limits

The enumeration is bounded. The unbounded closure is the support proof in
`DERIVATION.md`. Compilation, Gröbner elimination, and repository CI are
engineering evidence; they do not turn a constructing-agent result into an
independently accepted theorem.
