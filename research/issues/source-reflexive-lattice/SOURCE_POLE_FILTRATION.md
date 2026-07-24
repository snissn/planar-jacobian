# Source Pole Filtration

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-004`, `SRL-005`, `SRL-009`

## 1. Boundary audit

Let

```text
j: U=Spec(A) -> Y=Spec(O)
```

be the Keller open immersion, with ring map

```text
O -> A=C[x,y].
```

The complement `D=Y\U` need not be assumed pure. Write

```text
D_div = E_1 union ... union E_r
```

for its height-one irreducible components and let `Z` denote the union of components of codimension at least two.

On a normal noetherian surface:

- rational functions and reflexive rank-one modules are determined at height one;
- removing `Z` alone does not change regular functions;
- if `D` were nonempty but had no height-one component, then `Gamma(U,O_U)=Gamma(Y,O_Y)=O`; because both schemes are affine and the open immersion is induced by the same ring, `U=Y`, contradiction.

Thus every nonempty affine complement in this setup has at least one divisorial component, although lower-dimensional pieces may occur in addition. The pole filtration consumes `D_div`; `Z` contributes no independent pole index.

## 2. Correct divisorial modules

For a multi-index

```text
m=(m_1,...,m_r) in N^r,
```

define the reflexive divisorial sheaf

```text
M_m = O_Y(sum_i m_i E_i)
```

inside the constant sheaf `L`. Explicitly, its local sections are rational functions `f` satisfying

```text
v_F(f) + sum_i m_i*1_(F=E_i) >= 0
```

for every prime divisor `F` of `Y`.

This definition does not require the boundary to be Cartier. Each `M_m` is coherent, rank one, reflexive, and full as an `O`-module. Since `Y` is affine and finite over `Spec(B)`,

```text
Gamma(Y,M_m)
```

is a finite `O`-module and hence a finite `B`-module. Under the maintained normal-surface package it is maximal Cohen--Macaulay over the regular surface `B`, hence locally free as a `B`-module.

If one wants a single integer index, put

```text
D_red = E_1+...+E_r,
M_n = O_Y(nD_red).
```

Because the number of components is finite, the diagonal sequence is cofinal in the multi-index system.

## 3. Exact union theorem (`SRL-004`)

Inside `L`,

```text
A
 = Gamma(U,O_U)
 = union_(m in N^r) Gamma(Y,M_m)
 = union_(n>=0) Gamma(Y,O_Y(nD_red)).
```

### Proof

A rational function is regular on `U` exactly when it has nonnegative valuation at every prime divisor whose generic point lies in `U`. Its negative divisor therefore has support only among the finitely many `E_i`, and every individual rational function has finite pole order. Choosing `m_i >= -v_{E_i}(f)` places it in `M_m`. Conversely, every section of `M_m` has no poles away from the omitted divisors and is regular on `U`.

The codimension-two subset `Z` does not appear because normality gives the height-one intersection description of regular functions.

## 4. Every omitted divisor supports a source pole

Let `q_i subset O` be the height-one prime of `E_i`. Since `E_i` is absent from `Spec(A)`, no prime of `A` contracts to `q_i`, so

```text
q_i A = A.
```

Choose a finite relation

```text
1 = sum_l c_l a_l,       c_l in q_i, a_l in A.
```

Every `c_l` has positive `E_i`-valuation. If all `a_l` had nonnegative valuation, the right side would have positive valuation, impossible. Hence some element of `A` has a pole along `E_i`.

Taking its powers shows that `A` has arbitrarily negative `E_i`-valuation. Therefore:

- `A` is not a finite `O`-module when the divisorial boundary is nonempty;
- the directed pole union cannot stabilize at a finite stage;
- every finite `B`-submodule of `A` has a lower valuation bound at each `E_i`.

## 5. One-step pole growth

Fix a boundary component `E` above a target divisor `(h)`, and let `e=v_E(h)` be its ramification index. Choose a canonical derivation `D` with

```text
D(h) in B_(h)^x.
```

After the usual tame local base change, write

```text
h=s^e,
D(s)=a/(e s^(e-1)),       a=D(h) in R^x.
```

For a pure pole `s^(-m)` with `m>0`,

```text
D(s^(-m)) = -(m/e) a h^(-1)s^(-m).
```

Thus

```text
v_E(D(s^(-m))) = -m-e.
```

More generally, for `f=s^(-m)u` with `u` a unit, the derivative of `s^(-m)` is the unique term of lowest valuation; differentiating `u` contributes terms at least one `s`-power higher. Therefore the same valuation formula holds.

Globally this means that if a section has pole allowance `m_E` at `E`, a transverse canonical translation can require allowance `m_E+e`. At components where the translation is tangent, its normal contribution is zero, but the canonical pair always contains a transverse member.

## 6. Repeated escape (`SRL-005`)

Repeated differentiation gives

```text
D^n(s^(-m))
 = [product_(r=0)^(n-1)(-m/e-r)] a^n h^(-n)s^(-m)
   + higher-valuation terms.
```

Every factor is nonzero in characteristic zero. Hence

```text
v_E(D^n(s^(-m))) = -m-ne -> -infinity.
```

Consequences:

1. no fixed `M_m` containing a pole along `E` is stable under the transverse canonical derivation;
2. no finite collection or finite intersection of pole-bearing stages becomes stable;
3. commutativity of `D_P,D_Q` does not bound the growth, because iterating the one transverse member already escapes;
4. the Keller identity supplies no uniform `m` preserved by both fields;
5. Noetherian stabilization is unavailable because the iterates do not lie in one fixed finite ambient module.

For `e=1`, this is the elementary escape of `partial_s` on `s^(-m)`. Ramification makes the drop per iterate larger, but is not needed for the pole-stage obstruction.

## 7. Finite stable submodules of the source

### Theorem 7.1 (`SRL-009`)

Let `N subset A` be a finite `B`-submodule stable under both `D_P,D_Q`. Then

```text
N subset O.
```

In particular, if `O subset N`, then `N=O`; no proper finite source-pole overmodule of `O` is stable.

### Proof

A finite `B`-module has a lower valuation bound after localization at every target height-one prime. If an element of `N` had negative valuation at a boundary component `E`, choose the canonical translation transverse to its image divisor. Repeated escape would give elements of `N` with valuation tending to minus infinity, contradiction. Thus every element of `N` has nonnegative valuation at all boundary divisors. It is already regular at the height-one points of `U`, because it lies in `A`. Normality of `Y` now gives membership in the intersection of all height-one local rings, namely `O`.

### Corollary 7.2

A full finite stable module extracted from `j_*O_U` cannot use any actual source pole. It is a sublattice of the normalization. Applying the multiplier-ring theorem converts it to a finite stable order. Thus the source open immersion does not bypass the predecessor stable-order problem.

## 8. Unramified and ramified cases separated

- **Ramified boundary:** the predecessor local theorem excludes every full finite stable lattice, including sublattices of `O`.
- **Unramified nonproper boundary:** `O` itself is stable, but every proper pole-bearing stage fails. The model `O=C[t,z]`, `A=C[t,t^(-1),z]` is the exact control.
- **No divisorial boundary:** normal Hartogs gives `A=O`, so the source algebra is finite over `B`; in the Keller setting the stable-order implication then forces degree one.

The class-level result is therefore sharp: it eliminates the coherent source-pole-filtration construction class, not the possibility of an unramified normalization lattice.
