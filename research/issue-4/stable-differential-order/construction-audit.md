# Audit of Proposed Stable-Order Constructions

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`

Throughout the local tests,

```text
R=C[t,u]_(t),
S=R[s]/(s^e-t),
e>1,
D_t=partial_t,
D_u=partial_u.
```

The basis and matrices are those computed in `local-dvr-obstruction.md`.

## 1. Audit table

| Construction | Finite/full | Locally free | Algebra/order | Exact stability | Discriminant/control | Disposition |
|---|---:|---:|---:|---:|---|---|
| `C[x,y]` | not known finite over `B` | yes as its own ring, unresolved over `B` | yes | yes | would already imply finiteness route | circular as an order candidate |
| normalization `Cbar` / local `S` | yes | yes under finite-normalization surface hypotheses | yes | no if ramified | `c_e t^(e-1)` | fails at ramification |
| bounded pole `t^(-N)S`, `N>0` | yes as module | yes | no | no | fractional scaling only | not an order |
| conductor order `R+t^N S` | yes | yes | yes | no | `c_e t^[(e-1)(2N+1)]` | exact counterfamily |
| differential saturation of `S` | full | no finite bound | algebra after closure, but unbounded | formally stable only after infinite union | pole order tends to infinity | forbidden ascending union |
| trace dual / inverse different | yes, fractional | yes | no | no | unit times `t^(1-e)` | duality does not solve multiplication |
| relative canonical module | yes, fractional | yes in Gorenstein model | no as algebra | no | same as inverse different | same failure |
| conductor/canonical products | finite for fixed exponent | often free | sometimes an order | no | residue classes unchanged | integer shifts cannot cancel `j/e` |
| finite intersections of fractional ideals | yes | yes over DVR | rarely an order | no full stable member exists | valuation bounded | excluded by no-lattice theorem |
| regular-singular/Deligne lattice | yes as connection lattice after log change | yes | not generally an algebra | stable for `tD_t`, not `D_t` | residue `j/e mod Z` | logarithmic only |
| characteristic-`p` reduction | finite per prime | model-dependent | model-dependent | iteration may terminate mod `p` | no uniform char-zero bound | no lift obtained |

## 2. Polynomial source algebra

`A=C[x,y]` is a `B`-subalgebra with total quotient field `L`, and both canonical derivations are polynomial vector fields, so

```text
D_P(A) subset A,
D_Q(A) subset A.
```

The missing property is precisely finite generation as a `B`-module. If `A` were finite over `B`, the Keller morphism would be finite etale and the degree-one route would already be available. Therefore declaring `A` to be the desired order assumes the load-bearing finiteness conclusion.

## 3. Normalization and bounded poles

The normalization `S` is finite free with basis `1,s,...,s^(e-1)`, is multiplicatively closed, and has the correct field. Its matrices are

```text
A_t=diag(0,j/(et)),
A_u=0.
```

It fails exact stability for `e>1`.

For fixed `N>0`, the fractional module `t^(-N)S` is finite free and full. In the basis

```text
t^(-N),t^(-N)s,...,t^(-N)s^(e-1)
```

its matrices and fractional discriminant are

```text
A_t=diag((-N+j/e)/t)_(j=0,...,e-1),
A_u=0,
Disc(t^(-N)S/R)=c_e t^[e-1-2Ne].
```

It is not an algebra, because

```text
(t^(-N)S)^2=t^(-2N)S not subset t^(-N)S.
```

More generally, every finite `R`-algebra contained in `L` is integral over `R` and therefore lies inside the integral closure `S`; negative valuation poles cannot occur in a local order at all.

## 4. Differential saturation and the fixed-ambient requirement

Starting with `S`, define a formal ascending sequence

```text
Sat_0=S,
Sat_(n+1)=Sat_n+D_t(Sat_n).
```

It contains

```text
D_t^n(s)=product_(j=0)^(n-1)(1/e-j)t^(-n)s.
```

The valuation is `1-en`, so the sequence leaves every fixed finite lattice. Hence:

- no single finite ambient `R`-module contains all terms;
- Noetherian stabilization is inapplicable;
- the infinite union is not an admissible finite order;
- taking multiplicative closure only enlarges the unbounded union.

This directly enforces the leaf's prohibition on an ascending pole-order union.

## 5. Conductor orders

For each `N>=1`,

```text
M_N=R+t^N S
```

is a genuine finite free order. Its basis, multiplication table, matrices, and discriminant are:

```text
basis: 1,t^N s,...,t^N s^(e-1),
A_t=diag(0,(N+j/e)/t)_(j=1,...,e-1),
A_u=0,
Disc(M_N/R)=c_e t^[(e-1)(2N+1)].
```

The exact failure mutation is `tD_t`: under the logarithmic field,

```text
tD_t(t^N s^j)=(N+j/e)t^N s^j,
```

so every `M_N` is logarithmically stable. Removing the factor `t` restores the forbidden pole. This family proves that deeper conductor does not approach exact stability.

## 6. Trace duals, inverse different, and canonical modules

For `S/R` defined by `X^e-t`, the different is

```text
D_(S/R)=(e s^(e-1)).
```

The trace dual is

```text
S^vee=D_(S/R)^(-1)=(e s^(e-1))^(-1)S.
```

An `R`-basis is

```text
c_j=(1/e)s^(j+1-e),
j=0,...,e-1.
```

The matrices are

```text
A_t=diag((j+1-e)/(et)),
A_u=0.
```

Its fractional discriminant is a unit times

```text
t^(1-e).
```

It is not closed under multiplication: the square of a lowest-valuation generator has valuation below the module. In this hypersurface/Gorenstein model the relative canonical module is the same trace-dual module, so canonical-module language does not repair either multiplication or exact stability.

Products with conductor powers shift all residues by integers. The fractional parts `j/e mod Z` remain unchanged, so no fixed conductor/different exponent removes the obstruction.

## 7. Intersections of finitely many fractional ideals

Over the DVR `S`, every fractional `S`-ideal is principal, of the form `s^m S`. A finite intersection is again one fractional ideal. An `R`-basis, the two matrices, and the fractional discriminant are

```text
s^m,s^(m+1),...,s^(m+e-1),
A_t=diag((m+j)/(et))_(j=0,...,e-1),
A_u=0,
Disc(s^m S/R)=c_e t^[e-1+2m].
```

No full such ideal is `D_t`-stable when `e>1`: among the `e` consecutive exponents is a class not divisible by `e`, and repeated differentiation of that basis element has unbounded negative valuation.

The broader no-lattice theorem removes the restriction to `S`-ideals. Any finite intersection that remains a full valuation-bounded `R`-lattice is excluded. An intersection can evade the theorem only by losing fullness or finite generation, neither of which is allowed.

## 8. Integrable connections and regular singular extension

In the normalization basis, the connection one-form for `D_t` is

```text
diag(0,1/e,...,(e-1)/e) dt/t.
```

It is regular singular. The residue eigenvalues are the fractional classes

```text
0,1/e,...,(e-1)/e modulo Z.
```

Changing a lattice shifts residue eigenvalues by integers but cannot make all nonzero fractional classes disappear. A logarithmic lattice exists and is explicit (`S` itself under `tD_t`), but an exact `D_t`-stable lattice would require removal of the pole, which the repeated-derivative theorem forbids.

Any global regular-singular extension method must therefore prove that every relevant ramification index is one. Assuming a pole-free connection extension is already assuming the local conclusion needed for finite etaleness.

## 9. Characteristic-`p` reductions

For a prime `p` not dividing `e`, reduction of the Kummer formula gives

```text
D_t^p(s)
 = product_(j=0)^(p-1)(1/e-j)t^(-p)s
 = 0
```

because one factor vanishes in `F_p`. Thus the characteristic-zero unbounded sequence can become `p`-nilpotent after reduction. The stopping index grows with `p` and provides no uniform characteristic-zero denominator or pole-order bound. Primes dividing `e` are wild/inseparable and do not model the characteristic-zero tame branch.

A useful mod-`p` argument would need a bound independent of `p` that descends to characteristic zero. No such bound is supplied by this construction.

## 10. Failure mutations

The following mutations are detected by the calculations:

1. **Sign reversal in `D_P` or `D_Q`:** breaks one of the identities `D_P(P)=1`, `D_Q(Q)=1`.
2. **Dropping multiplicative closure:** makes trace multiplication matrices undefined over the candidate module.
3. **Replacing `D_t` by `tD_t`:** turns the false exact-stability claim into a true logarithmic one; this is a semantic weakening.
4. **Claiming Noetherian stabilization:** fails because `D_t^n(s)` leaves every fixed finite ambient module.
5. **Treating a fractional dual as an order:** its square escapes the module.
6. **Assuming a non-Galois cover avoids the issue:** the cubic model retains the ramified quadratic local factor.
7. **Checking only the cusp singular point:** misses the generic height-one pole along the cusp divisor.
8. **Using regularity at target infinity:** changes coordinates and loses exact affine translation stability.
9. **Using mod-`p` nilpotence as a uniform bound:** the nilpotence index depends on `p` and has no characteristic-zero limit.
10. **Assuming etaleness to construct the lattice:** the positive unramified control is circular for the existence problem.

## 11. Exact conclusion of the construction audit

Every tested canonical finite lattice either:

- is a genuine order but fails exact stability;
- is stable only after replacing translations by logarithmic fields;
- is a finite module but not a subalgebra;
- or requires an infinite unbounded union.

At a ramified height-one valuation this failure is universal, not an artifact of the chosen basis. The smallest remaining existence question is therefore confined to proving or exploiting codimension-one unramifiedness without assuming finite etaleness or degree one.
