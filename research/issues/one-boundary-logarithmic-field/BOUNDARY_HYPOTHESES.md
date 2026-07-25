# Boundary hypotheses and scope

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `OBLF-H0` through `OBLF-H8`

## 1. Ambient Keller normalization

Throughout the packet, unless a countermodel is explicitly being discussed,
we use the following data.

- `OBLF-H0` — `F=(P,Q):U=A2_source -> X=A2_target` is a polynomial map over
  `C` with `dP wedge dQ = dx wedge dy`.
- `OBLF-H1` — `K=C(P,Q)`, `L=C(x,y)`, `O` is the integral closure of
  `B=C[P,Q]` in `L`, `Y=Spec(O)`, and `pi:Y->X` is finite.
- `OBLF-H2` — the Zariski-Main map `j:U->Y` is the specified open immersion;
  the ring map is `O -> C[x,y]`.

`Y` is normal and integral by construction. Smoothness of `Y` is never used
unless stated separately.

## 2. Distinct one-component conditions

The phrase *one boundary* can hide several inequivalent assertions. This
packet keeps them separate.

- `OBLF-H3` — the reduced support of `D=Y-j(U)` is one irreducible divisor
  `D0`. The boundary scheme need not be reduced.
- `OBLF-H4` — `pi` is generically ramified along `D0`.
- `OBLF-H5` — the reduced target branch locus is one irreducible curve
  `C=V(g)`. This is an additional hypothesis; it is not inferred merely from
  `OBLF-H3`.
- `OBLF-H6` — `C` is smooth, or generically smooth, as explicitly stated in a
  subclass. This does not imply that `D0` or `Y` is smooth.
- `OBLF-H7` — the normalization of `C` is rational with one puncture at
  infinity. This does not imply that `C` is smooth or isomorphic to `A1`.
- `OBLF-H8` — an actual nontrivial algebraic `G_m` action on `X` preserves
  `C`. A regular logarithmic derivation is not a substitute for this action.

The main ramified subclass theorem uses `H0` through `H5` and `H8`. The
unramified exclusion uses `H0` through `H3` together with the absence of all
codimension-one ramification, and does not use `H4`, `H5`, or `H8`.

## 3. Branch, ramification, and boundary

Let `R_pi` be the support of the relative different on `Y` and let `Br_pi` be
its target image. Keller étaleness on `U` gives

```text
R_pi subset D.
```

The reverse containment need not hold: a component of `D` can represent
unramified sheet loss. Likewise, a target branch component is an image in
`X`, not a component of `D` itself. All logarithmic lifting criteria refer to
`Br_pi,red`; all source-open invariance criteria refer to `D`.

Under `H3` and `H4`, `D0` is the unique codimension-one component of the
ramification support. If an extended connected algebraic group action
preserves the ramification support, it therefore preserves `D0` and hence its
complement `U`. This is the only uniqueness argument used in the terminal
ramified theorem.

## 4. Smooth curves versus coordinate curves

The following implications are not used without their hypotheses.

- A smooth irreducible affine plane curve need not be `A1`.
- A rational curve with one place at infinity can be singular.
- An abstract copy of `A1` embedded in `A2_C` is a coordinate line only after
  applying the Abhyankar-Moh embedding theorem.
- Such a polynomial target automorphism changes the displayed pair `(P,Q)`.
  It preserves the abstract base ring and normalization, and multiplies the
  Keller determinant by the nonzero constant Jacobian of the automorphism;
  it is not treated as an identity in the original coordinates.

## 5. Divisors and ideals

For a normal affine surface `Y`, a reduced irreducible divisor is represented
by a height-one prime `p_D`. A regular derivation `delta` preserves it exactly
when

```text
delta(p_D) subset p_D.
```

This can be tested after localizing at the generic point. Codimension-two
points add no second pole condition because normal rings are intersections of
their height-one localizations. A nonnormal boundary image can nevertheless
have conductor descent conditions; those conditions concern the induced
field on the curve, not regularity of the ambient derivation on normal `Y`.

## 6. Exact-symplectic scope

The polynomial identity

```text
P dQ + y dx = dH
```

is used with complete Laurent expansions along `D0`. One-boundary geometry
adds common pole support, global coefficient functions on the normalization
of `D0`, and conductor/puncture compatibility. It does **not** turn zero
residue into vanishing of all negative coefficients, and no divisor is
principalized without a separate proof.

## 7. Terminal theorem dependency

The final implication invokes Shaska, arXiv:2607.20210v1, Theorem 3.3, only
under all of the following verified conditions:

1. an actual nontrivial algebraic `G_m` action exists on the target;
2. after a finite isogeny, it acts algebraically on `Y`;
3. `D0` and `U` are invariant;
4. the restricted source action is nontrivial;
5. `F` is equivariant.

Without these conditions this packet stops at the logarithmic, conductor, or
principal-part system.