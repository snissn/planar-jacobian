# Exact Countermodel and Falsification Search

## 1. Authority and level separation

`validate_qualifying_weight.py` is an exact regression and falsification tool.
Every output is classified at one of four levels.

1. **Support level:** finite exponent sets, Newton polygons, fan rays, and
   support-function defects.
2. **Formal-layer level:** all coefficient equations of `J(P,Q)=1` for a
   declared ansatz, with required nonzero charts imposed by saturation.
3. **Polynomial level:** an explicit coefficient assignment in `C[x,y]`.
4. **Keller level:** exact symbolic verification of `J=1` and, when claimed, an
   explicit inverse or triangular factorization.

A vanishing top bracket is never reported as a Keller realization by itself.

## 2. Primitive-weight campaign

Default bounds are

```text
1<=p,q<=96, gcd(p,q)=1,
2<=N<=10.
```

This gives 5,611 primitive positive weights. For every `A_N`, the campaign
examines both affine source orientation types and all affine target degree
patterns, for 100,998 exact weight evaluations. It verifies

```text
mu_aff(A_N)=N^2-1.
```

The unbounded proof is in `TRANSFORMATION_ORBIT.md`; enumeration is a regression
against omitted orientations and arithmetic errors.

### Omitted-weight mutation

For a selected `A_N`, the script removes the exact rays `(N,1),(1,N)` from the
weight library. The reported minimum strictly increases. This detects a search
that silently tests only standard or low-slope weights.

## 3. Transformation library

The executable transformation checks contain exactly the operations needed for
the scoped claims:

- identity and both source-weight orientations;
- arbitrary affine target degree patterns;
- signed target swap, with a mutation showing the unsigned swap sends `J=1` to
  `J=-1`;
- determinant-one target shear `Q->Q-P^N` for `A_N`;
- complete chain shear `Q->Q-lambda P^N` for `B_N`.

The affine local minimum is recorded before the nonlinear target shear, and
defect zero after it. This distinction detects accidental enlargement of the
transformation class.

The script does not apply Laurent changes, formal automorphisms without a
polynomial inverse, completion-valued Hamiltonian exponentials, or
uncompensated scalings.

## 4. Finite-fan campaign

The script constructs `N(P)+N(Q)` exactly, extracts closed-positive normal rays,
and regularizes every nonunimodular cone by an integer Euclidean subdivision.
It compares the finite theorem's candidate set with brute force on 5,611
primitive weights for 24 actual tame Keller maps.

Default comparison count:

```text
24 fixed representatives,
134,664 finite-versus-brute weight comparisons.
```

The random portion has a fixed seed; the initial maps include both `A_N` and
their sheared representatives. No floating-point convexity or angle test is
used.

## 5. Exhaustive finite-support campaign

The default search takes every lattice monomial in

```text
i,j>=0, i+j<=5
```

and every two-element support. There are 21 monomial points, 210 two-term
supports, and

```text
210^2=44,100
```

ordered support pairs.

For each pair the script:

1. checks the exact axis coefficients of `kappa`; a negative axis coefficient
   rules out a Keller realization because positive weights approaching that
   axis would have negative defect;
2. computes the exact primitive-positive minimum from the regular fan;
3. retains local minima with all defects at least six;
4. imposes necessary common-power compatibility in every positive fan chamber
   and on every positive wall;
5. constructs the complete four-coefficient Jacobian system for each surviving
   pair;
6. saturates by the product of all four declared support coefficients.

The default counts are:

```text
axis-admissible pairs:                    43,650
pairs with exact fixed-support minimum>=6: 32,887
face-compatible high-defect pairs:            639
transpose-reduced saturated systems:          387
formal Keller survivors:                        0
```

For a face of a two-term polynomial, common-power support compatibility is
exact: if both faces are vertices, the exponent vectors must be parallel; if
both are two-term edges, a nontrivial proper power would have additional
binomial support, so coprime powers force exponent pair `(1,1)` and identical
edge supports. A one-edge/one-vertex face is impossible.

This is a finite computer-assisted exclusion for the declared degree-five,
exactly-two-term universe. It is not extrapolated to larger or denser supports.

## 6. Complete binomial-chain equations

For every `2<=N<=8`, independent symbols are used in

```text
P=a x+b y^N,
Q=c y+sum q_k x^k y^(N(N-k)).
```

The program expands the **complete** polynomial `J(P,Q)-1` and checks that the
coefficient system is exactly the constant equation plus the adjacent
recurrences. It then substitutes the closed-form solution and verifies

```text
Q=c y+(q_N/a^N)P^N,
J(P,Q)=1 when ac=1.
```

The default run checks 42 complete coefficient equations.

### Missing-support campaign

For each `N<=8`, every subset of the interior chain positions is enumerated
while retaining both endpoints. There are 254 patterns. The recurrence forces
all chain coefficients nonzero, so every actual hole is rejected on the
nonzero-endpoint chart.

## 7. Complete low-degree no-shear template

The search also considers

```text
P=a x^2+p10 x+p01 y+p00,
Q=b x^3+q20 x^2+q11 x y+q02 y^2+q10 x+q01 y+q00.
```

All coefficients of `J(P,Q)-1` are imposed, together with

```text
z a b-1=0.
```

The saturated Groebner basis over the rationals is the unit ideal. Thus no
formal pair in this complete `(2,3)` template survives the nonzero top chart.
This is a bounded formal exclusion, not a theorem for all common-power
`(2,3)` supports.

### Saturation mutation

Deleting `zab-1` makes the ideal nonunit because the advertised top
coefficients may vanish. The script requires this semantic change, detecting a
search that forgot to impose its nonzero chart.

## 8. Adjacent-edge compatibility campaign

For all coprime pairs in `[1,5]^2` and bounded nonzero shared root vertices, the
program solves

```text
v_P=m h=m' h',
v_Q=n h=n' h'.
```

It checks 1,881 nonzero-vertex solutions and confirms equality of the coprime
pairs. A separate zero-vertex control allows incompatible pairs, verifying that
the nonzero hypothesis is essential.

## 9. Actual high-defect affine local minima

For every `3<=N<=10`, `A_N` is recorded simultaneously as:

```text
support level: affine minimum N^2-1>=8;
formal level: complete chain recurrence solved;
polynomial level: explicit coefficients;
Keller level: J=1 and explicit inverse;
adjacent-edge level: lengths (1,N), powers (1,N);
after declared target shear: defect 0.
```

Thus the affine-only bounded-orbit claim is falsified at the strongest level,
but no `A_N` survives the declared complete-top triangular shear.

## 10. Reproduction

From the repository root:

```bash
python3 research/issues/qualifying-weight-descent/validate_qualifying_weight.py
python3 research/issues/qualifying-weight-descent/validate_qualifying_weight.py \
  --max-weight 128 --max-n 12 --fan-instances 32 \
  --support-degree 5 --json
```

Generated JSON and logs are transient and are not committed.

## 11. Exact limitation

The campaign does not enumerate the full polynomial automorphism group, all
finite supports of unbounded degree, or all correction layers of a common-power
core with `m,n>=2`. Its strongest negative finding is:

```text
within the declared bounded support/formal library, every actual affine local
minimum is eliminated by a complete-top target shear, and no high-defect
exactly-two-term formal Keller pair survives through total degree five.
```

The surviving global obstruction is termination/existence of complete-top
descents for arbitrary supports and the no-escape bridge from positive toric
weights to normalization-boundary valuations.
