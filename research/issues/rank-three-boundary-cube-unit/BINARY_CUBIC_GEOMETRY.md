# Binary-Cubic Geometry of Fixed Sections

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claims: R3BC-02, R3BC-04
```

## 1. Intrinsic index cubic

Retain the conditional finite locally free rank-three setup

```text
B=C[P,Q],
O=B direct_sum E,
rank_B(E)=2.
```

For `s in E`, define

```text
Phi(s)=1 wedge s wedge s^2.
```

After choosing a frame `(e1,e2)` of `E`, write `s=Ue1+Ve2`. If

```text
e1^2 = a0 + a1 e1 + a2 e2,
e1 e2 = b0 + b1 e1 + b2 e2,
e2^2 = c0 + c1 e1 + c2 e2,
```

then direct expansion gives, up to the fixed determinant trivialization,

```text
Phi(U,V)
 = a2 U^3
 + (2 b2-a1) U^2 V
 + (c2-2 b1) U V^2
 - c1 V^3.
```

A frame change by `M in GL_2(B)` substitutes `(U,V)M` into the cubic. The
binary-cubic discriminant transforms by

```text
Disc(Phi o M)=det(M)^6 Disc(Phi).
```

This covariance is checked symbolically in `verify_binary_cubic.py`.

## 2. Fitting and discriminant identities

The inclusion

```text
B[s] = Span_B(1,s,s^2) -> O
```

has a square rank-three presentation. Therefore

```text
Fitt_0^B(O/B[s])=(det(1,s,s^2))=(Phi(s)).
```

The trace-pairing Gram matrices satisfy

```text
Gram(1,s,s^2)=M_s^T Gram(O) M_s,
```

where `det(M_s)=Phi(s)`. Hence

```text
Disc(B[s]/B)=Phi(s)^2 Disc(O/B).
```

At a height-one prime `p`,

```text
v_p(Phi(s)) = length_{B_p}(O_p/B_p[s])
```

for a generically primitive section. In particular, `Phi(s)` is a unit at `p`
exactly when the reduction of `s` generates the entire special-fiber algebra.

The exact companion-algebra calculation is in `verify_index_and_fitting.py`.

## 3. The constant-level scheme

For `lambda in C*`, define the affine `B`-scheme

```text
X_lambda = Spec B[U,V]/(Phi(U,V)-lambda).
```

A section of `X_lambda -> Spec(B)` is exactly a pair `(U,V) in B^2` with
`Phi(U,V)=lambda`.

### Lemma 3.1 — unimodularity is automatic

If `Phi(U,V)` is a unit, then `(U,V)=B`.

### Proof

If a maximal ideal contained both `U` and `V`, homogeneity would put
`Phi(U,V)` in that maximal ideal, contradicting its being a unit. ∎

Thus the “unimodular vector” condition in the primary question is not an
additional constraint once the constant value is obtained.

## 4. Geometric fibers of `X_lambda`

Over an algebraically closed residue field of characteristic zero, the boundary
classification in `BOUNDARY_VALUATIONS.md` gives three models.

### 4.1 Three distinct linear factors

After `GL_2`, take

```text
Phi=U V (U+V).
```

Then

```text
U V (U+V)=lambda
```

is smooth and geometrically integral. Its projective closure is a smooth plane
cubic, hence a genus-one curve, and the affine curve removes the three points at
infinity cut out by the linear factors.

This is the fiber over the split étale locus. The family is not an affine-line
or multiplicative-group torsor; a global section is a genuine arithmetic problem
over `B`, not a consequence of `Pic(B)=0`.

### 4.2 One simple factor and one double factor

After `GL_2`, take

```text
Phi=U V^2.
```

The level curve is

```text
U V^2=lambda,
```

which is isomorphic to `G_m` by the coordinate `V`, with
`U=lambda V^{-2}`.

This model occurs at simple ramification. It has a canonical *shape*, but no
canonical integral choice of a unit `V` across unrelated boundary components.

### 4.3 A cube

After `GL_2`, take

```text
Phi=U^3.
```

Over `C`, `U^3=lambda` is the disjoint union of three affine lines, one for each
cube root of `lambda`. This is the totally ramified special-fiber shape. The
three components show that even the literal boundary cube does not select a
unique section without additional data.

The Jacobian/singularity ideals of all three `lambda=1` models are verified by
Gröbner bases in `verify_binary_cubic.py`.

## 5. Why a rational primitive direction is not a level section

Let `r in E_K` be primitive. Then `Phi_K(r) in K*`. To rescale `r` to the
constant level `lambda`, one needs `c in K*` satisfying

```text
c^3 Phi_K(r)=lambda.
```

Such a `c` exists only when `lambda/Phi_K(r)` is a cube in `K`. Thus a rational
primitive element, or a rational section of the complement `Phi != 0`, does not
supply a rational section of `X_lambda`.

Adding a base scalar to a primitive element also does not help: sheet differences,
and hence `Phi`, are unchanged.

## 6. Resolvent and monodromy

For a depressed cubic

```text
T^3+pT+q,
Delta=-4p^3-27q^2,
```

a Cardano quadratic resolvent can be written

```text
R(Z)=Z^2+qZ-p^3/27,
Disc(R)=-Delta/27.
```

The square class of `Delta` distinguishes the generic `A_3` and `S_3` cases.
Neither case provides a distinguished sheet:

- `S_3` is transitive and has no fixed sheet;
- `A_3` is still transitive;
- passing to the quadratic resolvent may reduce monodromy but does not produce
  an integral element whose fixed-section index is a unit.

A globally distinguished sheet would amount to a nontrivial factorization of
the generic cubic cover and is incompatible with connected cubic field degree.
Monodromy therefore supplies organization, not the missing integral section.

## 7. Connected components and obstruction classes

The constant-level family changes topology across the discriminant:

```text
three distinct factors -> punctured genus-one curve,
LM^2                  -> G_m,
L^3                   -> three A1 components.
```

Accordingly, there is no single torsor class in `H^1(B,G)` whose vanishing would
uniformly solve the section problem. In particular:

- `Pic(B)=0` does not trivialize the genus-one fibers;
- `H^1(B,O_B)=0` does not apply because primitive-section transitions need not
  be affine-linear on the full base;
- local sections at finitely many divisors do not control newly created
  codimension-one zeros.

The exact global search is isolated in `UNIT_VALUE_SEARCH.md`.
