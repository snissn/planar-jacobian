# Case Table

## 1. Transformation-class comparison

| Case | Allowed transformations | Exact result | Status |
|---|---|---|---|
| `A_N`, determinant-one linear | source/target `SL_2` | `mu=N^2-1` | proved internally |
| `A_N`, affine | compensated affine source/target | `mu=N^2-1` | proved internally |
| `A_N`, triangular target | `(u,v)->(u,v-u^N)` | `kappa_(N,1)=0` | explicit identity |
| `A_N`, tame | affine plus elementary triangular | `mu=0` | explicit shear |
| any automorphism, full | arbitrary polynomial target | `mu=0` via inverse | exact but circular as detector |
| arbitrary Keller pair, affine | all affine orientations | no universal bound five | falsified by actual `A_N`, `N>=3` |
| arbitrary Keller pair, tame/full | all plane polynomial automorphisms | `mu<=5` unresolved | global bridge remains open |
| undeclared `mu` | transformation class omitted | not a defined invariant | rejected |

## 2. Fixed representative

| Newton configuration | Finite test | Exact conclusion |
|---|---|---|
| positive common-fan rays present | regularize adjacent cones | minimum occurs on a finite positive ray set |
| coordinate quadrant is the sole cone | test `(1,1)` | exact primitive-positive minimum |
| cone adjacent to an axis | test first positive regular ray | axis coefficient is nonnegative for Keller pairs |
| nonunimodular cone | insert Euclidean regular rays | lattice points are not omitted |
| support changes after transformation | rebuild Minkowski polygon and fan | prior weight test set is invalidated |

## 3. Positive-face common-power cases

Assume a hypothetical noninvertible Keller pair. The reviewed defect-four
theorem gives `kappa_w>=5` for every primitive positive weight.

| Face data | Consequence | Descent/core disposition |
|---|---|---|
| `(1,n)` at a defect-minimizing weight | complete top target shear | forbidden by global minimality |
| `(m,1)` at a defect-minimizing weight | transposed complete shear | forbidden by global minimality |
| `m,n>=2` at a minimizing weight | no elementary power shear | retained core |
| exponent one at a nonminimizing weight | strict local defect decrease | may remain above global minimum |
| adjacent edges share nonzero vertices in both polygons | coprime pairs agree | exact compatibility |
| adjacent edges meet at origin | coprime pairs may differ | necessary exception |
| either component face is a vertex | both are vertices with monomial root | inspect next Rees stair |
| either component face is an edge | both are parallel edges | lengths recover coprime pair |
| partial top cancellation only | weighted degree may remain | not certified descent |

## 4. Exact sparse classes and formal templates

| Class/template | Complete equations or search | Outcome |
|---|---|---|
| `B_N`: `P=ax+by^N`, full chain in `Q` | `ac=1`; adjacent recurrence | `Q=cy+lambda P^N`; shear to defect zero |
| `B_N` missing an interior chain term | same full recurrence | inconsistent with nonzero endpoint chart |
| `A_N` | specialization of `B_N` | actual Keller map; affine minimum `N^2-1` |
| complete `(2,3)` no-shear template with tops `a x^2,b x^3` | saturated full Jacobian ideal | unit ideal |
| all ordered two-term support pairs, total degree `<=5` | 44,100 support pairs | exact bounded enumeration |
| high-defect, face-compatible two-term pairs | 387 transpose-reduced saturated systems | no formal Keller survivor |

## 5. Minimal-counterexample tuple

| Coordinate | Reason retained | Exact use |
|---|---|---|
| `kappa_w` | primary descent coordinate | complete-top shear lowers it at selected weight |
| `deg P+deg Q` | bounds support triangle | second lexicographic coordinate |
| support cardinality | detects cancellation and holes | third coordinate |
| positive compact-edge count | face complexity | fourth coordinate |
| twice Minkowski area | lattice integer/global geometry | fifth coordinate |
| `d_P(w)+d_Q(w)` | selected-weight tie break | sixth coordinate |
| boundary valuation count | model-dependent | omitted |
| stabilizer/transformation count | may be infinite | omitted |

## 6. Fixed-defect authority

| Defect | Authority used here | Consequence |
|---:|---|---|
| `0..4` | independently reviewed fixed-weight theorem | unconditional exclusion of noninvertible pair |
| `5` | local-adversarial candidate only | any exclusion is conditional |
| `>=6` | no fixed-weight theorem consumed | retained |

## 7. Requested disposition mapping

| Requested disposition | Result |
|---|---|
| 1. universal `mu<=5` | not proved |
| 2. every degree/Newton-minimal counterexample has such a weight | not proved |
| 3. substantial named class | **proved for `B_N`, with defect zero** |
| 4. support alone cannot force affine bound five | strengthened to actual Keller automorphisms `A_N` |
| 5. smaller exact invariant | directed lexicographic Newton core isolated |
| 6. finite explicit global list | not obtained; fixed-support weight list is finite |
| 7. proposed scalar inadequate | **proved by transformation-class separation** |

The packet's primary constructive disposition is 3, accompanied by the exact
class-dependence diagnosis in 7 and the fixed-representative reduction in 5.
