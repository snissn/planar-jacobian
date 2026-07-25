# Countermodels and hypothesis separators

> Authority: `MUTABLE_NONAUTHORITATIVE`

Each model below records the exact Keller-specific hypothesis that is absent.
None is presented as a counterexample to the planar Jacobian conjecture.

## 1. Cyclic cover of a semi-invariant branch

Let

```text
Y_e = Spec C[P,Q,s]/(s^e-g(P,Q)),  e>1.
```

If `g` is reduced, the map `Y_e->A2_(P,Q)` is generically etale and ramified
along `s=0`. If a target Euler field satisfies `E(g)=d g`, its rational lift is

```text
E_tilde(s)=(d/e)s.
```

After multiplying weights by `e`, this integrates to an algebraic torus action
on the cover. Thus semi-invariant cyclic covers demonstrate the
finite-isogeny mechanism of `OBLF-04`.

They are not Keller source models. The finite map is ramified along `s=0`, and
on the complement `s` is a nonconstant unit. Hence `Y_e-(s=0)` is not
`A2`, whose only units are constants.

## 2. Weighted cusp

For

```text
g=P^a-Q^b,
```

the Euler field is regular, semisimple, and conductor-compatible, while the
Hamiltonian field restricts on the normalization to

```text
-t^((a-1)(b-1)) partial_t.
```

The latter is not locally finite for `a,b>=2`. This model separates

```text
regular logarithmic lift
```

from

```text
semisimple or locally finite lift.
```

A cyclic cover of the cusp still fails the Keller-source condition from
Section 1.

## 3. Smooth non-coordinate curve with no torus symmetry

Consider the smooth affine elliptic curve

```text
g=Q^2-P^3+P=0.
```

Its projective completion is an elliptic curve with one point removed. The
Hamiltonian field

```text
H_g=2Q partial_P+(3P^2-1) partial_Q
```

is a nonzero logarithmic field. A nontrivial `G_m` action preserving the affine
curve would extend to its smooth projective completion and fix the missing
point, but the automorphism group of an elliptic curve fixing a point is
finite. Hence this branch has no nontrivial torus symmetry.

This is a control against the implication

```text
M_g nonzero or free => M_g contains a semisimple integral field.
```

No finite Keller normalization with this branch is constructed.

## 4. Local tangency without global semisimplicity

For any reduced plane curve, the Hamiltonian field is globally tangent. At each
smooth point, many additional local tangent fields exist. The elliptic example
shows that this local and module-theoretic abundance need not globalize to a
torus action. The missing hypothesis is algebraic local finiteness with
integral weights.

## 5. Regular logarithmic field that does not preserve the source open

Let

```text
Y=A2_(s,t),
pi(s,t)=(P,Q)=(s^e,t),
D_ram={s=0},  E={t=0},
delta=s partial_s+partial_t.
```

The induced target field is

```text
V=eP partial_P+partial_Q,
```

which is logarithmic along `P=0`, and `delta` is regular and tangent to
`D_ram`. But

```text
delta(t)=1 notin (t),
```

so `E` is not preserved. The open complement of both divisors is `(C*)^2`, not
the Keller source `A2`. This model identifies exactly why an unramified
boundary component cannot be ignored.

## 6. Equivariant finite cover that is not Keller

The map

```text
(s,z) |-> (P,Q)=(s^e,z)
```

is finite and equivariant for diagonal torus actions, but

```text
dP wedge dQ=e s^(e-1) ds wedge dz
```

is not a nonzero constant multiple of `ds wedge dz` for `e>1`. Equivariance of
a finite cover alone does not force degree one; the Keller hypothesis is used
only at the terminal theorem.

## 7. Zero residue with a higher pole

At a boundary valuation take

```text
x=pi^(-1),  H=x^m.
```

Then

```text
dH=-m pi^(-m-1)dpi.
```

The logarithmic residue is zero and the higher principal part is nonzero. This
is a local exact-symplectic control, not a finite normalization or a Keller
map. It falsifies only the proposed residue-to-regularity implication.

## 8. Coordinate-line cover and the unit obstruction

For a connected finite cover ramified only over `P=0`, one boundary component
above the line gives a positive multiple of that component as `div(P)`. On its
complement, `P` is a nonconstant unit. Such a complement cannot be `A2`.
This is the elementary unit shadow of the coordinate-line case of `OBLF-05`.
It uses the one-component support; with several components, different
valuations can occur.

## 9. Countermodel matrix

| Model | Logarithmic field | Algebraic action | Preserves displayed open | Keller source |
|---|---:|---:|---:|---:|
| Semi-invariant cyclic cover | yes | after isogeny | ramified complement yes | no |
| Weighted cusp Hamiltonian | yes | no | not specified | no model supplied |
| Smooth affine elliptic branch | yes | no torus | not specified | no model supplied |
| Ramified plus unramified boundary | yes on ramified divisor | field may integrate locally | no | no |
| `(s^e,z)` cover | yes | yes | yes | no |
| Exact Laurent pole | exact form | no action | not applicable | no |

The matrix prevents any control example from being promoted into a
Keller-specific obstruction without the missing hypotheses.