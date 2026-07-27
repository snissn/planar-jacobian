# Case Table

## 1. Canonical anchor systems

All rows use `P_a=x`, `Q_b=c y`, and `A B c!=0`.

| key | `(m,n)` | `(a,b)` | `w` | `rho` | top forms | decisive equations | disposition |
|---|---|---|---|---:|---|---|---|
| I | `(2,3)` | `(3,3)` | `(1,3)` | 2 | `A x^4`, `B x^6` | `4Af-6Bv=0`, `-2vf=0`, `4Ah-5ve+3uf=0`, `4Ac-4vg+3uh+2rf=0` | `v=f=h=0`, then `Ac=0`; impossible |
| II | `(2,3)` | `(5,1)` | `(1,8)` | 3 | `A x^6`, `B x^9` | `6Ac=0` | impossible at `S_1` |
| III | `(2,3)` | `(5,1)` | `(5,14)` | 5 | `A x^2`, `B x^3` | `2Ac=0` | impossible at `S_1` |
| IV | `(3,2)` | `(5,1)` | `(1,3)` | 2 | `A x^6`, `B x^4` | `6Ac-4Bv=0`, `2cv=0` | `v=0`, then `Ac=0`; impossible |

The complete equations, including `S_6`, are in
[`DEFECT6_REES_SYSTEM.md`](DEFECT6_REES_SYSTEM.md). Every saturated full ideal
is `(1)`.

## 2. Complete normalized first-wall table

The symbols refer to the layer notation in the complete systems.
“Earlier zeros” are the coefficients that must vanish so that the displayed
wall is the first wall incident to the anchor.

| key | wall | branch | earlier/current zero data | declared nonzero edge data | adjacent faces `(P^u,Q^u)` | defect | face obstruction |
|---|---|---|---|---|---|---:|---|
| I | `(1,4)` | `Q`-only | `v=0` | `f!=0` | `(A x^4, B x^6+f x^2y)` | 5 | `4Af=0` |
| I | `(1,4)` | `P`-only | `f=0` | `v!=0` | `(A x^4+v y, B x^6)` | 5 | `-6Bv=0` |
| I | `(1,4)` | shared | none | `v f!=0` | `(A x^4+v y, B x^6+f x^2y)` | 5 | `4Af-6Bv=0`, `-2vf=0` |
| I | `(1,5)` | `Q`-only | `v=f=0` | `h!=0` | `(A x^4, B x^6+hxy)` | 4 | `4Ah=0` |
| I | `(1,6)` | `Q`-only | `v=f=h=0` | required `c!=0` | `(A x^4, B x^6+c y)` | 3 | `4Ac=0` |
| II | `(1,9)` | `Q`-only | none | required `c!=0` | `(A x^6, B x^9+c y)` | 5 | `6Ac=0` |
| III | `(1,3)` | `Q`-only | none | required `c!=0` | `(A x^2, B x^3+c y)` | 1 | `2Ac=0` |
| IV | `(1,4)` | `Q`-only | `v=0` | required `c!=0` | `(A x^6, B x^4+c y)` | 5 | `6Ac=0` |
| IV | `(1,4)` | shared | none | `v c!=0` | `(A x^6+v x^2y, B x^4+c y)` | 5 | `6Ac-4Bv=0`, `2cv=0` |

Every face obstruction is collected at its exact exponent vector. Saturating by
all declared nonzero entries yields the unit ideal in every row. The full
anchor Rees ideal remains the unit ideal after imposing each branch's zero and
nonzero conditions.

## 3. Coverage matrix

| required orientation/case | coverage |
|---|---|
| source order `p<q` | canonical rows I–IV |
| source order `p>q` | determinant-one source signed swap of every row |
| equal source weights | arithmetically impossible (`5rho=8`) |
| component order `(2,3)` | rows I–III and raw rows 1–8 |
| component order `(3,2)` | row IV and raw rows 9–16; target signed swaps also checked |
| origin transition | no case: the exhaustive root support is always a nonzero monomial |
| `x`-axis transition | all nine normalized wall rows |
| `y`-axis transition | source signed swaps of the nine rows |
| component fails to share vertex | all `P`-only and `Q`-only rows |
| simultaneous zero layers | row III; `P_1,...,P_4,P_6` and `Q_2,...,Q_4,Q_6` are literal zero |
| resonant lower layers | rows I and IV retain all `S_6` simultaneous brackets (`c-v ell`, `c-z ell`) |
| nonresonant lower layers | rows II and III and the remaining layers in I/IV |
| scalar retention | `c` appears through the complete sequence and is saturated as nonzero |
| constant-bracket layer | every system includes `S_6=1` |

## 4. Global-minimum reading of the wall table

Once the independently reviewed defect-five theorem is integrated, a globally
minimal noninvertible Keller pair has defect at least six at every primitive
positive weight. Every first adjacent wall in the table has defect at most
five. Thus the two-wall geometry alone contradicts the global premise.

The full Rees calculation is stronger: it excludes the anchor systems even
without invoking the low-defect theorem at the adjacent wall.

## 5. Residual list

There is no residual coefficient ideal, no exceptional orientation, and no
formal or polynomial-support survivor. Requested outcomes B–D are therefore
not needed; outcome A holds.
