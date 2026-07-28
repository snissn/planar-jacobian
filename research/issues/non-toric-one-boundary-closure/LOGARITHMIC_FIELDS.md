# Logarithmic fields after Liouville exactness

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `NTLC-06` and `NTLC-09`

## 1. The logarithmic module remains separate

For an irreducible reduced target branch `g=0`, put

```text
M_g=Der_C(C[P,Q])(-log g)
   ={A partial_P+B partial_Q: A g_P+B g_Q in (g)}.
```

The predecessor packet proves at mutable candidate scope that `M_g` is a free
rank-two module and that

```text
H_g=g_Q partial_P-g_P partial_Q
```

is always logarithmic. None of these facts implies local finiteness. The new
condition

```text
P dQ=dR on the normalized branch                         (1.1)
```

is likewise a condition on a differential, not a construction of a complete
vector field.

A target derivation must still be classified separately as logarithmic,
Hamiltonian, locally nilpotent, locally finite, semisimple, integral
semisimple, or algebraically integrable. Only a locally nilpotent field gives a
`G_a` action, and only an integral semisimple locally finite field gives a
`G_m` action without further work.

## 2. Coordinate behavior of the Liouville class

The exactness obstruction is intrinsic to the displayed Keller target up to
polynomial target changes with constant Jacobian. If `(U,V)` is a polynomial
target coordinate pair with

```text
dU wedge dV=c dP wedge dQ,  c in C*,
```

then

```text
d(U dV-c P dQ)=0.
```

Polynomial de Rham exactness gives a polynomial `S(P,Q)` with

```text
U dV=c P dQ+dS.
```

Hence the vanishing of the normalized Liouville class is preserved, up to the
nonzero scalar `c`, by every polynomial target automorphism. It is not an
artifact of choosing one symplectic representative.

## 3. A practical presentation for branches linear in one coordinate

For

```text
g=A(Q)P+B(Q),  gcd(A,B)=1,
```

a logarithmic basis can be constructed explicitly. Choose `u(Q),v(Q)` satisfying

```text
u B congruent A' mod A,
v B congruent B' mod A,
```

put `c(P,Q)=u(Q)P+v(Q)`, and set

```text
a=(c(A P+B)-(A'P+B'))/A.
```

The congruences make the displayed quotient polynomial. Then

```text
delta_1=g partial_P,
delta_2=a partial_P+partial_Q
```

are logarithmic and

```text
det(delta_1,delta_2)=g.
```

Thus they form a Saito basis. This gives an exact symbolic description for the
smooth exact example below. The construction does not make `delta_2` locally
finite.

## 4. Liouville-nonexact smooth non-toric branch

For

```text
g_ne=P(P-1)Q-1,
P=z,
Q=1/(z(z-1)),
```

the normalized affine curve is `P1-{0,1,infinity}` and

```text
P dQ=(1/z-1/(z-1)-1/(z-1)^2) dz.                  (4.1)
```

The residues `+1` and `-1` show that (4.1) is not exact. Therefore `NTLC-04`
excludes this branch from a ramified pole-supported Keller boundary.

This branch is non-toric: after linearization, an invariant irreducible plane
curve for a nontrivial target torus is an axis, a same-sign binomial, or an
opposite-sign monomial curve. Their normalizations have at most two punctures;
the displayed three-puncture curve is not in that list.

## 5. Liouville-exact smooth non-toric survivor

Let

```text
R(z)=1/z+1/(z-1),
Q=z,
P=R'(z)=-1/z^2-1/(z-1)^2.
```

Eliminating `z` gives

```text
g_ex=P Q^2(Q-1)^2+(Q-1)^2+Q^2.                   (5.1)
```

The coefficient of `P` in (5.1) is nonzero at every point of the curve, because
`Q=0` and `Q=1` do not satisfy (5.1). Hence the curve is smooth and its
coordinate ring is

```text
C[Q,1/(Q(Q-1))].
```

It has normalization `P1-{0,1,infinity}` and satisfies exactly

```text
P dQ=dR.                                           (5.2)
```

It is non-toric for the same three-puncture reason. It therefore survives both
the predecessor torus obstruction and the new Liouville obstruction.

Moreover it has no nonzero locally finite logarithmic target field, conditional
only on the predecessor packet's Jordan-decomposition and plane-action
classification. A nonzero nilpotent Jordan part would give a `G_a` action and a
coordinate-line branch; a nonzero semisimple part would give a torus-preserved
branch. Both contradict the three-puncture normalization.

## 6. Exact remaining interface

For a Liouville-exact non-toric branch, the Laurent system supplies no canonical
locally finite element of `M_g`. The exact surviving alternatives are:

1. a higher recursion class `beta_r` is nonexact, excluding the fixed formal
   type at order `r`;
2. a declared conductor/gluing condition fails;
3. every differential class vanishes and a formal solution survives;
4. the formal solution fails algebraization or polynomial realization;
5. a separate global theorem controls Newton support and produces a qualifying
   weight;
6. a genuinely new locally finite logarithmic field is constructed from data
   beyond (1.1).

Regularity of `H_g`, freeness of `M_g`, and the existence of `R` are each
insufficient for alternatives 5 or 6.
