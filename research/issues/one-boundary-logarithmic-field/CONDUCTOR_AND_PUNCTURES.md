# Boundary normalization, conductor, and punctures

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary label: `OBLF-08`

The ambient surface `Y` is normal, but a boundary curve or its target image can
be singular. Normality of `Y` therefore does not remove the curve-level
conductor problem.

## 1. Normalization of a boundary curve

Let `C=V(g)` be an irreducible target branch curve and let

```text
nu:C_tilde -> C
```

be its normalization. On an affine chart write

```text
A_C = C[p(t),q(t)] subset A_bar,
```

where `A_bar` is the coordinate ring of the normalized affine curve. The
conductor is

```text
c = {a in A_C : a A_bar subset A_C}.
```

It is an ideal of both rings, and `A_bar/c` is finite-dimensional over `C` for
a finite birational normalization of curves.

A derivation `theta` of `Frac(A_C)` descends to `A_C` exactly when

```text
theta(A_C) subset A_C.                           (3.1)
```

If it preserves both `A_C` and `A_bar`, it automatically preserves the
conductor, because for `c in conductor` and `s in A_bar`,

```text
theta(c)s = theta(cs)-c theta(s) in A_C.
```

Conversely, for a derivation already regular on `A_bar`, descent can be tested
on generators of the finite algebra modulo `c`. Thus conductor compatibility
is a finite linear condition in the quotient `A_bar/c`; it is not an extra
height-one pole condition on normal `Y`.

## 2. Smooth component

If `C` is smooth, `A_C=A_bar` locally and the conductor is the unit ideal.
There is no conductor obstruction. The remaining questions are:

- whether the logarithmic field is locally finite and integral-weight;
- whether its target action lifts;
- whether the source-open boundary is invariant; and
- whether the exact-symplectic pole coefficients satisfy the global puncture
  conditions.

Smoothness alone does not produce a torus action. A smooth affine plane curve
of positive genus, for example, need not admit any nontrivial `G_m` action.

## 3. Weighted cusp

Take

```text
g=P^a-Q^b,  a,b>=2, gcd(a,b)=1,
P=t^b, Q=t^a.
```

Then

```text
A_C=C[t^a,t^b] subset C[t]=A_bar.
```

The numerical semigroup conductor is

```text
c_0=(a-1)(b-1),
conductor = t^(c_0) C[t].                       (3.2)
```

The weighted Euler field

```text
E=bP partial_P+aQ partial_Q
```

restricts to

```text
E(t)=t.                                         (3.3)
```

It preserves `C[t^a,t^b]`, every semigroup degree, and the conductor. It is
semisimple and integral-weight, so a ramified one-boundary Keller model with
this reduced branch is excluded by `OBLF-05`.

The Hamiltonian field

```text
H_g=-b Q^(b-1) partial_P-a P^(a-1) partial_Q
```

restricts to

```text
H_g(t)=-t^((a-1)(b-1)).                         (3.4)
```

For `c_0>=2`, its iterates on `t` have strictly increasing degree and span an
infinite-dimensional vector space. It is regular and conductor-compatible but
not locally finite. Formula (3.4) exhibits the exact separation between a
logarithmic field and an algebraic torus generator.

## 4. Tangencies and several preimages over one image point

At a singular point of `C`, several branches of `C_tilde` can lie over the
same image point. Descent requires the values and finite jets prescribed by
the conductor quotient to match. For a node this begins with equality of
values on the two branches; for a cusp it is the semigroup-gap condition in
`C[t]/t^(c_0)`.

A target logarithmic field may be tangent to each normalized branch and still
fail to descend if these finite jet conditions are not preserved. Conversely,
when a target field is already a derivation of the singular coordinate ring,
its lift to the normalization preserves the conductor automatically. The
ambient surface derivation and the curve-image derivation must not be confused.

## 5. Pullbacks of the Keller functions

At the generic boundary divisor of `Y`, `P,Q` are regular while `x,y` can have
poles. Restricting the Laurent coefficients to the normalization of the
boundary gives rational functions

```text
p_i(t), q_i(t), x_i(t), y_i(t), h_i(t).
```

The coefficients that represent regular functions on the singular boundary
must satisfy the conductor descent conditions (3.1). Principal coefficients of
`x,y,H` need not descend as regular boundary functions; they are sections of
the corresponding normal-bundle powers and can have poles at punctures of the
normalized boundary. The finite conductor quotient records their matching at
singular image points.

## 6. Punctures and moment conditions

Let `C_bar` be a smooth projective completion of `C_tilde`, and let

```text
S=C_bar-C_tilde
```

be the puncture set. Every rational differential on `C_bar` satisfies the
global residue theorem. If `S` consists of one point and the differential has
no other poles, its residue at that point is zero. This is only a residue
condition: differentials such as `d(t^(-m))` have arbitrary higher poles and
zero residue.

For a fixed pole bound, descent and exactness produce a finite moment system:

1. conductor congruences in `A_bar/c`;
2. prescribed principal parts at the points of `S`;
3. zero-residue equations for exact logarithmic terms;
4. the coefficient identities from `PRINCIPAL_PARTS.md`.

The dimension of the space of higher principal parts is generally positive.
One place at infinity does not force their vanishing.

## 7. Rational one-place subclasses

The exact dispositions are:

- **smooth `A1`**: Abhyankar-Moh makes the branch a coordinate line after a
  target automorphism; the torus obstruction excludes the ramified
  one-boundary model;
- **weighted cusp**: equations (3.2)-(3.4) apply; the Euler action excludes the
  model, while the Hamiltonian illustrates non-local-finiteness;
- **singular non-weighted one-place curve**: no torus action is inferred. The
  surviving problem is the finite conductor/principal-part system for each
  fixed semigroup and pole type.

This packet does not classify all one-place plane curves or bound their
semigroups.