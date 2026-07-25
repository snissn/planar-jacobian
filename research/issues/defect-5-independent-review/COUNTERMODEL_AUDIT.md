# Independent Countermodel and Exact-Checker Audit

## 1. Reviewer-owned implementation

`review_validate_defect5_independent.py` was written under the review-owned
path. It imports neither `validate_defect5.py` nor
`review_validate_defect5_adversarial.py`, and it contains no candidate exception
allowlist. Its case loop is generated from:

```text
1<=p<=q<=N,
gcd(p,q)=1,
a in {1,2,3,4},
b=5-a,
d_P=p+a,
d_Q=q+b,
rho=gcd(d_P,d_Q).
```

For every supported no-descent arithmetic case and every projective common-root
chart, it generates:

- complete weighted-homogeneous supports for every layer through index five;
- literal zero layers for unsupported degrees;
- the top common powers `A H^m`, `B H^n`;
- only the selected specialization `P_a=x`, `Q_b=c y`;
- all other layers as independent symbolic coefficients;
- every coefficient of `S_0,...,S_5` from `f_xg_y-f_yg_x`;
- every possible simultaneous resonant term;
- individual above-resonance vanishing checks.

## 2. Exact saturation and elimination

For each generated system, the checker adds an auxiliary variable `z` and the
equation

```text
z*A*B*c-1=0.
```

A Gröbner basis over the exact rational polynomial ring is computed in grevlex
order. Containment of one proves that the coefficient ideal has no point over
the algebraic closure with the required nonzero top coefficients and selected
resonant scalar. Root charts similarly impose a nonzero projective root
coefficient by setting it to one.

The two equal-weight systems are generated independently in `H`-adapted
coordinates. The `(2,3)` system first derives the exact integrated `S_1` formula
and checks the `-8B g^2/(3A)` coefficient before eliminating the remaining
ideal.

## 3. Bounded run

Command:

```text
python3 research/issues/defect-5-independent-review/review_validate_defect5_independent.py \
  --max-weight 96
```

Observed output:

```text
review mode: independent-review
reviewed candidate: 2eeb36d232366d124b5a66774b29769ec1eba43d
primitive weights enumerated (1 <= p <= q <= 96): 2806
exponent-one descents reclassified: 817
empty common-root supports rejected: 10065
supported no-descent arithmetic cases: 342
unequal projective charts eliminated exactly: 338
unequal saturated ideals: 338
equal-weight saturated ideals: 2
derived family signatures (a,p,rho): 9
zero layers generated: 771
systems with multiple possible resonant brackets: 6
largest saturated input: 15 equations, 19 variables
semantic corruptions detected: 9
source/target orientation checks: 2
exact rational/algebraic Keller-Rees trials: 15
formal complete-staircase survivors: 0
independent defect-five review checker: PASS
mathematical authority: HUMAN RECONSTRUCTION, NOT BOUNDED CHECK COUNTS
```

The exact rational/algebraic trials include coefficients in `Q(sqrt(2))` and
check the Rees identity on independently constructed triangular Keller
automorphisms across several primitive weights.

## 4. Simultaneous resonances and zero layers

The generated scan finds exactly six unequal systems with more than one
potentially nonzero resonant bracket. In each, `S_5` retains the second scalar
term. It also generates 771 literal zero layers in the `N=96` run. The checker
verifies every generated bracket with `i+j>5` is individually zero.

## 5. Formal levels

A support-realizable arithmetic case is not a coefficient solution. A
coefficient solution would be stronger: because all above-resonance brackets
vanish individually, setting all deeper layers to zero would produce actual
polynomials with `J=1` in normalized coordinates. The explicit polynomial graded
inverse would then give an actual Keller pair in original coordinates.

No generated no-descent system reaches coefficient consistency. There are no
formal full-staircase survivors.

## 6. Mutation program

The checker intentionally corrupts and detects:

- the Jacobian sign;
- the Rees exponent;
- the target component sign;
- determinant compensation;
- graded layer preservation;
- complete-top cancellation;
- source-weight orientation;
- simultaneous-resonance retention;
- the correct top exponent in the `(a,b)=(2,3)`, `w=(2,3)` exception.

## 7. Review of prior checker evidence

The post-candidate local-adversarial checker contains a concrete support bug in
its `(2,3)`, `w=(2,3)` model:

```text
Q_0=B x^2     # weighted degree 4
```

but the normalized system has `d_Q=q+b=6`, `rho=2`, `n=3`, hence

```text
Q_0=B x^3     # weighted degree 6.
```

The prior checker still reports an inconsistent ideal, but for the wrong finite
system. This defect is confined to non-authoritative regression evidence. The
pinned human derivation states `2Af-3Bv=0`, which uses `B x^3`, and the
construction checker builds `B H^n=B x^3`. The independent checker includes a
specific mutation control for this error and eliminates the correct system.

## 8. Authority and unbounded limit

The finite scan is falsification evidence only. It cannot prove that no new
family appears above weight 96. Unbounded completeness is supplied separately by
the human inequalities and divisibility argument:

```text
p<=a<=4,
unequal no-descent roots contain no y-monomial,
p divides a,
p divides q+5-a.
```

Those conditions derive the complete infinite family list without a search
bound. The exact checker then independently tests large finite prefixes and all
finite support exceptions.
