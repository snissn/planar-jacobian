# Local DVR Obstruction to Exact Translation-Stable Lattices

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`  
> **Scope:** characteristic-zero DVRs and the canonical target translations after height-one localization.

## 1. Local no-lattice theorem

### Theorem

Let `R` be an excellent equicharacteristic-zero DVR with fraction field `K`, uniformizer `t`, and derivation `delta:R -> R` such that

```text
delta(t) in R^x.
```

Let `L/K` be finite separable and let `D` be the unique extension of `delta` to `L`. If `Lambda subset L` is a finite full `R`-lattice,

```text
Lambda tensor_R K = L,
```

and `D(Lambda) subset Lambda`, then every extension of the `t`-adic valuation to `L` has ramification index one.

Equivalently, if one extension valuation has ramification index `e>1`, no finite full `R`-lattice is `D`-stable. This conclusion is stronger than a no-order statement: multiplicative closure is not assumed.

### Reduction to the tame Kummer factor

Characteristic zero makes every finite ramification tame. Pass to a strict henselization of `R`, extend the derivation through the ind-etale base change, and decompose the finite separable algebra into field factors. Completion is optional and is not used in the valuation argument. Projection of a stable full lattice to any factor is again a stable full lattice. Derivations kill the product idempotents, because

```text
D(e)=D(e^2)=2eD(e)
```

and `2e-1` is a unit with square one.

For a ramified factor with ramification index `e`, write `t=u s^e` with `s` a uniformizer and `u` a unit. The factor is henselian with separably closed residue field; since `e` is invertible, Hensel's lemma gives an `e`-th root of `u`. After rescaling `s`,

```text
t=s^e
```

Write `a=delta(t)`, a unit. Then

```text
D(s)=a/(e s^(e-1))=(a/e)t^(-1)s.
```

### Commensurability and repeated differentiation

Let `S` be the valuation ring of the Kummer factor. Every full finite `R`-lattice is commensurable with `S`, so there are integers `N,N'` with

```text
t^N S subset Lambda subset t^(-N') S.
```

In particular `t^N s in Lambda`. The first derivative is

```text
D(t^N s)=(N+1/e)a t^(N-1)s.
```

Inductively, the lowest-valuation term of `D^n(t^N s)` is

```text
c_n a^n t^(N-n)s,
c_n=product_(j=0)^(n-1)(N+1/e-j),
```

and all other terms have strictly larger `s`-valuation. The terms produced by differentiating `a` stay one `t`-power higher because `D(a) in R`. Since `e>1`, none of the rational numbers `N+1/e-j` is zero. Therefore

```text
v_s(D^n(t^N s))=e(N-n)+1,
```

which tends to minus infinity. This contradicts the lower valuation bound on `Lambda`.

### Differential escape invariant

For the ramified branch, the witness `t^N s` has linear escape

```text
v_s(t^N s)-v_s(D^n(t^N s))=ne.
```

Thus the normalized escape slope is

```text
gamma_s(D)=lim_n [v_s(t^N s)-v_s(D^n(t^N s))]/n=e.
```

The equivalent regular-singular invariant is the nonintegral residue class `1/e mod Z` in the Kummer connection. Either form measures the unavoidable differential pole growth. A stable valuation-bounded lattice would require zero escape.

## 2. Basic two-variable model

Take

```text
R=C[t,u]_(t),
L=K(s),
t=s^e,
e>1.
```

The two base derivations extend as

```text
D_t(s)=1/(e s^(e-1))=(1/e)t^(-1)s,
D_u(s)=0.
```

For every integer `N`,

```text
D_t^n(t^N s)
 = product_(j=0)^(n-1)(N+1/e-j) t^(N-n)s,
D_u(t^N s)=0.
```

The `D_u` matrix is harmless; the exact transverse translation `D_t` creates the obstruction.

## 3. Normalization lattice

Let

```text
S=R[s]/(s^e-t)
```

with basis

```text
1,s,...,s^(e-1).
```

It is finite free of rank `e`, is a domain, is multiplicatively closed, and has total quotient field `L`. In this basis,

```text
A_t=diag(0,1/(et),2/(et),...,(e-1)/(et)),
A_u=0.
```

Thus `S` is not `D_t`-stable. The polynomial discriminant is

```text
Disc(S/R)=c_e t^(e-1),
c_e=(-1)^[e(e-1)/2+e-1] e^e in C^x.
```

Its derivative is

```text
partial_t Disc=(e-1)c_e t^(e-2),
```

which is outside `(Disc)` for `e>1`. This is the local shadow of the global discriminant argument.

## 4. Conductor orders

For `N>=1`, define

```text
M_N=R+t^N S.
```

A free `R`-basis is

```text
1,b_1,...,b_(e-1),
b_j=t^N s^j.
```

Multiplication is explicit:

```text
b_i b_j = t^N b_(i+j)                 if i+j<e,
b_i b_j = t^(2N+1)                    if i+j=e,
b_i b_j = t^(N+1)b_(i+j-e)            if i+j>e.
```

Hence `M_N` is a finite free order with total quotient field `L`; its conductor in `S` is `t^N S`. The derivation matrices are

```text
A_t=diag(0,(N+1/e)/t,...,(N+(e-1)/e)/t),
A_u=0.
```

The discriminant is

```text
Disc(M_N/R)=c_e t^[(e-1)(2N+1)].
```

Neither the matrix nor the discriminant is regular under `partial_t`. Increasing the conductor only increases the discriminant exponent and shifts residues by integers; it never removes the fractional classes `j/e mod Z`.

## 5. Tame non-Galois cubic

Consider the degree-three extension over `C(t,u)` defined by

```text
z^3-3z-t=0.
```

Its discriminant is

```text
27(4-t^2),
```

which is not a square in `C(t)`, so the generic cubic is non-Galois. At `t=2`, set

```text
z=-1+s,
t=2+tau.
```

Then

```text
tau=s^3-3s^2=s^2(s-3),
dtau/ds=3s(s-2),
D_t(s)=1/[3s(s-2)].
```

At the ramified branch `s=0`,

```text
v_s(D_t^n(s))=1-2n.
```

The third sheet is unramified and separates after henselization; the ramified quadratic factor still has the same no-lattice obstruction. This verifies that Galois symmetry is irrelevant.

## 6. Cusp branch model

Let

```text
B=C[p,q],
h=p^2-q^3,
S=B[s]/(s^e-h).
```

In the basis `1,s,...,s^(e-1)`, the exact translation matrices are

```text
A_p=diag_j(2jp/(e h)),
A_q=diag_j(-3j q^2/(e h)),
```

where `j=0,...,e-1`. The discriminant is

```text
c_e h^(e-1).
```

At the generic point of the irreducible cusp divisor, both `p` and `q` are units, so the displayed matrices have genuine simple poles. The closed cusp point, where both numerators vanish, cannot repair a global lattice: localization at the generic point already contradicts stability.

The weighted logarithmic Euler field

```text
E=3p partial_p+2q partial_q
```

satisfies

```text
E(h)=6h,
E(s)=(6/e)s.
```

Thus `S` is stable under `E` but not under either exact translation. This is the required mutation separating logarithmic stability from translation stability.

## 7. Boundary-coordinate mutation

Let `p=s^(-e)` near a compactification boundary `s=0`. Then

```text
partial_p(s)=-(1/e)s^(e+1),
```

which is regular at that boundary. This does not produce a finite `C[p]`-order. Put `z=s^(-1)`; then `z` is integral over `C[p]` with

```text
z^e=p,
partial_p(z)=1/(e z^(e-1)).
```

The finite affine normalization is `C[z]`, and the pole reappears at the affine divisor `p=0`. Replacing `partial_p` by a vector field that vanishes at infinity changes exact translation stability into logarithmic or higher-vanishing stability and is not an admissible substitution.

## 8. Positive unramified control

If a finite DVR algebra is etale, every base derivation extends uniquely and preserves the algebra. After a strict henselian base change it is a product of copies of the base DVR, and the connection matrices are regular. Thus the obstruction detects ramification rather than finite degree by itself.

## 9. Keller application at height one

Let `h(P,Q)` be irreducible. In characteristic zero, `h` cannot divide both of its partial derivatives. Therefore at least one of

```text
partial_P h,
partial_Q h
```

is a unit in `B_(h)`. The corresponding canonical derivation is transverse. If a valuation of `L` above `(h)` has `e>1`, the theorem excludes a stable localization of any global finite full lattice. Consequently exact stability under both `D_P,D_Q` forces every height-one ramification index to be one.

This is the exact Keller-specific identity available locally: a globally defined commuting frame dual to `dP,dQ`. It exposes ramification; it does not cancel it.
