# The logarithmic module for one irreducible plane curve

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary label: `OBLF-01`

Let

```text
B = C[P,Q],  g in B irreducible and nonconstant,
A = B/(g).
```

Write

```text
M_g = Der_C(B)(-log g)
    = {a partial_P + b partial_Q : a g_P + b g_Q is in (g)}.
```

No smoothness of `g=0` is assumed.

## 1. Finite presentation

For every logarithmic pair `(a,b)` there is a unique `c in B` such that

```text
a g_P + b g_Q = c g.
```

Consequently projection to the first two coordinates identifies `M_g` with

```text
Syz_B(g_P,g_Q,-g)
 = {(a,b,c) in B^3 : a g_P+b g_Q-cg=0}.
```

There is also an exact sequence

```text
0 -> M_g -> B^2 -> J_g -> 0,                 (1.1)
```

where the last map is `(a,b) |-> a g_P+b g_Q mod g` and

```text
J_g=(g_P,g_Q)A subset A.
```

Because `g` is irreducible in characteristic zero, `A` is a one-dimensional
domain and `J_g` is a nonzero torsion-free ideal of `A`.

## 2. Projectivity and freeness

### Theorem `OBLF-01`

`M_g` is a projective `B`-module of rank two and therefore a free `B`-module
of rank two.

### Proof

Localize (1.1) at a maximal ideal `m` of `B`. The regular local ring `B_m` has
depth two. The nonzero ideal `(J_g)_m` is either zero after localization away
from the curve, or is a torsion-free module over the one-dimensional local
domain `A_m`; in the latter case it has depth one. The depth lemma gives

```text
depth (M_g)_m = 2.
```

Auslander-Buchsbaum over the regular local ring `B_m` then gives projective
dimension zero. Thus `M_g` is locally free. Its generic rank is two. Finally,
Quillen-Suslin makes every finite projective module over `C[P,Q]` free. `square`

Equivalently, on the smooth surface `A2`, the logarithmic tangent sheaf of a
reduced curve is reflexive; in dimension two a reflexive sheaf is locally
free. The proof above records the affine module calculation directly.

## 3. Saito determinant criterion

Let

```text
delta_i = a_i partial_P + b_i partial_Q,  i=1,2,
```

belong to `M_g`. Then they form a `B`-basis of `M_g` if and only if

```text
a_1 b_2 - a_2 b_1 = c g                 (1.2)
```

for some `c in C*`. This is the plane-curve case of Saito's determinant
criterion. The reducedness of `g` is essential. The primary source is K.
Saito, *Theory of logarithmic differential forms and logarithmic vector
fields*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. 27 (1980), 265-291,
DOI 10.15083/00039637.

## 4. Distinguished elements

### Hamiltonian field

For every `g`,

```text
H_g = g_Q partial_P - g_P partial_Q
```

satisfies `H_g(g)=0`. It is always logarithmic. This proves existence of a
nonzero element of `M_g`, but says nothing about local finiteness,
completeness, or algebraic integration.

### Euler-like field

If, in some polynomial coordinates `(u,v)`, `g` is weighted homogeneous of
weight `d` for integer weights `(m,n)`, then

```text
E = m u partial_u + n v partial_v,
E(g)=d g.
```

This field is semisimple, locally finite, and integral-weight. In favorable
quasihomogeneous cases `(E,H_g)` satisfies (1.2) and is a basis.

### Locally nilpotent field

Suppose `delta in M_g` is nonzero and locally nilpotent. It integrates to an
algebraic `G_a` action preserving `(g)`. Since `G_a` has no nontrivial
characters, a generator of the principal prime ideal can be chosen invariant.
Rentschler's theorem puts the action, after a polynomial automorphism, in the
form

```text
delta = f(u) partial_v,   ker(delta)=C[u].
```

Irreducibility then forces `g` to be a coordinate polynomial `u-c`. Thus:

```text
nonzero locally nilpotent element of M_g
=> g=0 is a coordinate line after a target automorphism.       (1.3)
```

The exact source is R. Rentschler, *Operations du groupe additif sur le plan
affine*, C. R. Acad. Sci. Paris Ser. A-B 267 (1968), A384-A387. The theorem
is used only over a characteristic-zero field.

### Semisimple field

A semisimple locally finite field with integral weights is the infinitesimal
generator of an algebraic `G_m` action. Its classification and its relation to
`g` are treated in [`SEMISIMPLE_CLASSIFICATION.md`](SEMISIMPLE_CLASSIFICATION.md).

## 5. Explicit bases

### Coordinate line

For `g=P`,

```text
M_g = B(P partial_P) direct_sum B(partial_Q).
```

The first generator is semisimple; the second is locally nilpotent.

### Polynomial graph

For `g=P-h(Q)`, a basis is

```text
delta_1 = g partial_P,
delta_2 = h'(Q) partial_P + partial_Q.
```

The determinant is `g`. Although every smooth polynomial graph is a coordinate
line after the triangular change `u=P-h(Q), v=Q`, neither displayed generator
must be useful in the original Keller coordinates.

### Weighted cusp

Let

```text
g=P^a-Q^b,  a,b>=2,  gcd(a,b)=1.
```

Then

```text
E = bP partial_P + aQ partial_Q,
H_g = -b Q^(b-1) partial_P - a P^(a-1) partial_Q
```

are logarithmic and

```text
det(E,H_g) = -ab g.
```

They form a basis. The Euler field integrates to `G_m`; the Hamiltonian field
is generally not locally finite.

## 6. What freeness does not prove

Freeness of `M_g` does not produce a canonical semisimple summand. A free basis
can consist of nonlinear, noncomplete fields. Nor does freeness identify the
boundary with the branch curve, preserve the source open, or constrain the
higher exact-symplectic principal parts. Those are separate equations.