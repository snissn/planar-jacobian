# Countermodels and Mutation Controls

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims tested:** `SRL-001`–`SRL-009`

These models are controls for the construction class. They are not asserted to be Keller counterexamples.

## 1. Tame Kummer branch: `t=s^e`

Let

```text
R=C[t,u]_(t),
S=R[s]/(s^e-t),
e>1.
```

For the transverse and tangential translations,

```text
D_t(s)=1/(e s^(e-1)),
D_u(s)=0.
```

The normalization, every fractional ideal, every conductor order, and every bounded pole stage has the nonintegral spectrum

```text
{0,1/e,...,(e-1)/e} mod Z.
```

A full finite lattice is valuation bounded, while repeated `D_t`-iteration on `t^Ns` or on a pole `s^(-m)` tends to valuation `-infinity`. This is the primary ramified control.

## 2. Tame non-Galois extension

Use the cubic

```text
z^3-3z-t=0.
```

Its generic discriminant is `27(4-t^2)`, so it is not a generic Galois cover. At `t=2`, write

```text
z=-1+s,
t=2+tau,
tau=s^2(s-3).
```

Then

```text
D_t(s)=1/[3s(s-2)],
v_s(D_t^n(s))=1-2n.
```

After henselization the unramified sheet separates, while the ramified quadratic factor retains the no-lattice obstruction. Galois symmetry is irrelevant.

## 3. Cusp branch

Let

```text
h=P^2-Q^3,
s^e=h.
```

The canonical residue pair is

```text
Res(hD_P)=2P R_e,
Res(hD_Q)=-3Q^2 R_e.
```

At the generic point of the cusp both coefficients are units. The tangential weighted field

```text
3P partial_P+2Q partial_Q
```

is logarithmic and lifts regularly, but each exact translation remains transverse in a nonzero normal direction. Checking only the singular closed cusp point misses the generic divisorial obstruction.

## 4. Several boundary components

Take the normal double cover

```text
s^2 = P(P-Q^2)(P-Q^3).
```

Each component has a local tangent field, but no nonzero affine-linear target field is tangent to all three. For the canonical frame this is not a problem: at every component the gradient is nonzero and one exact translation is transverse. A finite stable lattice must survive every component simultaneously, so one ramified component is enough to rule it out.

For source poles along several components, use multi-index stages

```text
O_Y(m_1E_1+...+m_rE_r).
```

A transverse field increases the relevant coordinate of the pole vector without any bound from commutativity.

## 5. Unramified but nonproper boundary

Let

```text
Y=Spec C[t,z],
U=D(t)=Spec C[t,t^(-1),z],
O=C[t,z],
A=C[t,t^(-1),z].
```

There is no ramification: `e=1`, and `O` is stable under `partial_t,partial_z`. Nevertheless

```text
M_m=t^(-m)O
```

is not stable under `partial_t` for any `m>0`, because

```text
partial_t^n(t^(-m))
 = (-m)(-m-1)...(-m-n+1)t^(-m-n).
```

The union of the `M_m` is `A` and never stabilizes. This separates two assertions:

- absence of ramification permits the pole-free stable lattice `O`;
- nonproper source poles still do not fit in a finite exact-stable stage.

## 6. Logarithmic versus exact stability

In the same unramified model,

```text
t partial_t(t^(-m))=-m t^(-m),
```

so every `M_m` is stable under the logarithmic field `t partial_t`. It is not stable under `partial_t`.

In the ramified Kummer model,

```text
tD_t(s^j)=(j/e)s^j,
```

so the normalization is logarithmically stable with fractional residue. This mutation proves that a Deligne/logarithmic lattice is not a solution to the exact-translation problem.

## 7. Source-pole union with no stabilization

Whenever one source element `a` has `v_E(a)<0`, its powers satisfy

```text
v_E(a^n)=n v_E(a) -> -infinity.
```

No finite `O`-module contains all powers, and no finite `B`-module contains all differential iterates under a transverse field. The ascending union can be stable as an algebra only because it abandons finite generation.

This refutes every use of Noetherian stabilization that does not first place all stages in one fixed finite ambient module.

## 8. Exact form with zero logarithmic residue and a higher pole

Let a boundary parameter satisfy `x=s^(-1)` and choose a polynomial on the source

```text
H=x^m,       m>=1.
```

Then

```text
dH=-m s^(-m-1)ds.
```

Its logarithmic residue is zero, but its higher principal part is nonzero. Thus exactness of the Keller primitive cannot eliminate the higher poles used by the source filtration or the ramified lift.

## 9. Characteristic-positive mutation

For `p` not dividing `e`, the characteristic-zero coefficient

```text
product_(r=0)^(p-1)(1/e-r)
```

vanishes modulo `p`. A repeated derivative can become `p`-nilpotent. The stopping index depends on `p` and gives no uniform characteristic-zero lattice bound. Primes dividing `e` are wild and lie outside the tame theorem.

## 10. Ring-orientation trap

The correct open immersion is induced by

```text
O -> A.
```

Writing `A->O` would reverse the scheme map and falsely suggest that source poles are integral elements of the normalization. Every pole-module and conductor calculation in this packet uses `O subset A subset L` and the scheme map `Spec(A)->Spec(O)`.
