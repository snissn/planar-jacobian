# Countermodel and realization ladder

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Label: `TPPR-07`

## 1. Levels

```text
L0  branch and coefficient identities
L1  all-orders formal Laurent neighborhood
L2  algebraic/formal finite cover
L3  finite normalization plus conductor and puncture gluing
L4  global polynomial P,Q,H in C[x,y]
L5  actual Keller map with the stated normalization boundary
```

## 2. Strong rational control

For any integer `e>1`, on the source function field `C(x,y)` set

```text
Q=-(1/e)y x^(e+1),
P=x^(-e)+R'(Q),
H=-(1/e)xy+R(Q),                                       (2.1)

R(z)=1/z+1/(z-1).
```

Direct differentiation gives

```text
J(P,Q)=1,
P dQ+y dx=dH.                                          (2.2)
```

Moreover `C(x,y)=C(x,Q)`, while

```text
P-R'(Q)=x^(-e).
```

Thus `C(x,y)/C(P,Q)` is generically the finite cyclic degree-`e` extension
obtained by adjoining an `e`-th root. With `t=x^(-1)`, the boundary `t=0` is

```text
Q=z,
P=R'(z).
```

This control has:

- the exact displayed normalized branch;
- exact constant Jacobian;
- the full source function field;
- a finite generic function-field extension;
- the full Liouville primitive identity;
- arbitrary ramification index.

Its exact failure is visible: `P` contains `x^(-e)` and denominators in `Q`,
while `H` contains denominators in `Q`. It is a rational/formal model below
`L4`, not a polynomial Keller map.

## 3. Ladder status

| level | status for displayed branch | first missing condition |
|---|---|---|
| `L0` | achieved | none |
| `L1` | achieved by predecessor and (2.1) | none |
| `L2` | achieved after adjoining the finite root parameter | global polynomial coordinates |
| `L3` | branch normalization is smooth; conductor class vanishes | global polynomial map |
| `L4` | impossible by `TPPR-05` | terminal contradiction |
| `L5` | impossible a fortiori | `L4` already fails |

The branch therefore does not furnish a Jacobian-conjecture counterexample.

## 4. Mutation controls

- **Nonexact differential:** replacing `P dQ` by `dz/z` introduces residue
  `1` at zero, so the predecessor recursion stops at order zero.
- **Denominator permission:** (2.1) survives, demonstrating that
  polynomiality is load-bearing.
- **No primitive:** dropping `H` does not create a polynomial realization;
  it only removes part of the Keller-derived evidence.
- **Second boundary:** does not change the component contradiction.
- **Formal/global confusion:** an identity in `C(z)((t))` is never labeled
  algebraic or polynomial without an explicit finite algebra and global
  substitution.
- **Conductor mutation:** `C[t^2,t^3] subset C[t]` has a nontrivial gap class.
- **Newton mutation:** no weight is inferred from the nonmonomial divisorial
  valuation.
