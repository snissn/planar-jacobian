# Exact geometry of the displayed branch

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `TPPR-01`, `TPPR-04`

Let

```text
g=P Q^2(Q-1)^2+(Q-1)^2+Q^2
A=C[P,Q]/(g).
```

## 1. Two exact unit certificates

In `C[P,Q]` one has

```text
Q(-P Q^3+2P Q^2-P Q-2Q+2)=1-g,                       (1.1)

(Q-1)(-P Q^2(Q-1)-2Q)=1-g.                            (1.2)
```

Consequently both `Q` and `Q-1` are units in `A`. In particular the coefficient
`Q^2(Q-1)^2` of `P` never vanishes on the affine branch.

## 2. Coordinate-ring identification

Solving the branch equation gives

```text
P=-((Q-1)^2+Q^2)/(Q^2(Q-1)^2).                        (2.1)
```

The maps

```text
A -> C[z,z^(-1),(z-1)^(-1)],
Q |-> z,
P |-> -1/z^2-1/(z-1)^2
```

and

```text
C[z,z^(-1),(z-1)^(-1)] -> A,
z |-> Q
```

are inverse by (1.1), (1.2), and (2.1). Hence

```text
A = C[z,z^(-1),(z-1)^(-1)].                           (2.2)
```

This proves irreducibility, normality, and smoothness without a Jacobian
singularity search. The smooth projective completion is `P1_z`, and the affine
curve is

```text
C = P1 - {0,1,infinity}.                               (2.3)
```

The normalization map supplied in the predecessor packet is therefore already
an isomorphism on the affine branch.

## 3. Exact primitive descends polynomially

Set

```text
R=(2z-1)/(z(z-1))=1/z+1/(z-1).
```

A polynomial representative in `A` is

```text
rho(P,Q)=-2P Q^3+3P Q^2-P Q-4Q+2.                    (3.1)
```

Substitution of (2.1) gives `rho=R`, and

```text
dR/dz=-1/z^2-1/(z-1)^2=P.                             (3.2)
```

Thus `P dQ=dR` in `Omega^1_(A/C)`. The primitive is not merely rational on the
normalization: it is the restriction of the target polynomial `rho(P,Q)`.

## 4. No polynomial curve enters the branch

### Theorem `TPPR-04`

Every morphism `gamma:A1->C` is constant.

### Proof

The pullback `q=gamma^*(Q)` is a unit of `C[t]` by (1.1), and `q-1` is a unit
by (1.2). Units of `C[t]` are nonzero constants, so `q` is constant and is not
`0` or `1`. Equation (2.1) then makes `gamma^*(P)` constant. `square`

This is exhaustive over polynomial maps of every degree. It is not a bounded
ansatz search.

## 5. Puncture mutations

- Filling only one puncture leaves an affine `G_m`; its coordinate or inverse is
  still a nonconstant unit, so every `A1->G_m` is constant.
- Filling two punctures leaves `A1`; the identity map is polynomial, so the
  obstruction correctly disappears.
- A rational map `P1-->C` is not the object excluded here. The load-bearing
  source theorem requires a polynomial morphism from `A1`.

No positive weight, Newton polygon, or monomialization is used in this
calculation.
