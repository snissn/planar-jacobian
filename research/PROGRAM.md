# Planar Jacobian Proof Program

> **Authority:** `MUTABLE_NONAUTHORITATIVE`

Let

```text
F=(P,Q): A^2_C -> A^2_C,     J(P,Q)=1,
A=C[x,y],                    B=C[P,Q],
K=Frac(B),                   L=Frac(A).
```

The program seeks a contradiction from `A != B` while keeping local étaleness, global nonproperness, and boundary sheet loss separate.

## Common geometric object

Let `Cbar` be the integral closure of `B` in `L`. Zariski's Main Theorem gives

```text
A^2 = Spec(A)  ->  Y=Spec(Cbar)  ->  A^2=Spec(B),
```

with an open immersion followed by a finite map. A counterexample would require a nonempty boundary `Y \ A^2` carrying all ramification and nonproperness.

The main proof lanes are different descriptions of the same obstruction:

- **finite normalization:** principalize the Kähler different or reduced branch divisor;
- **monogenicity/index form:** construct one integral primitive element whose index ideal is a unit;
- **canonical symmetry:** prove a pulled-back translation or Euler field is complete/locally finite;
- **generic fibers:** eliminate finite asymptotic punctures and puncture monodromy;
- **Brieskorn/Gauss--Manin:** produce one bounded coherent lattice in the target pencil;
- **weighted degeneration:** reduce an arbitrary map to an exactly graded Keller map without losing the constant-Jacobian term;
- **monodromy/Galois closure:** show fixed-sheet inertia and nonabelian gluing are incompatible with the affine-plane source.

None of the full bridge theorems is currently maintained as proved. Issue #3 does, however, close several conditional monogenicity steps and refute the purely algebraic genericity bridge at exact scope.

## Exact graded leverage

The primary new literature input is T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210. It proves that every nontrivially `G_m`-equivariant Keller endomorphism of `A^2` is an automorphism, for all sign patterns of source weights.

This suggests a filtered program: choose a positive primitive weight `w=(p,q)`, form the Rees deformation, and measure how many weighted layers separate the original map from exact grading.

For

```text
d_P = deg_w(P),
d_Q = deg_w(Q),
kappa_w = d_P + d_Q - p - q,
```

write

```text
Pcal(t,x,y)=t^{d_P} P(t^{-p}x,t^{-q}y),
Qcal(t,x,y)=t^{d_Q} Q(t^{-p}x,t^{-q}y).
```

The chain rule gives the exact identity

```text
J(Pcal,Qcal)=t^{kappa_w}.
```

Layer comparison yields the staircase equations recorded in [`tracks/filtered-equivariance.md`](tracks/filtered-equivariance.md).

## Current frontier

The conversation-derived argument claims that grading defects `0,1,2,3` can be reduced to the exactly graded case. That claim is **candidate**, not reviewed theorem authority.

Defect `4` is the first case containing a middle Wronskian correction. In the central resonance pattern, after normalizing the resonant coordinate pair, one encounters

```text
J(P_0,Q_2) + J(P_1,Q_1) + J(P_2,Q_0) = 0.
```

The term `J(P_1,Q_1)` can bend the line-pencil argument that works at lower defect. It is the active load-bearing obstruction.

## Moving-index disposition

Issue [#3](https://github.com/snissn/planar-jacobian/issues/3) audits the global primitive-element route in [`tracks/monogenicity-index-divisor.md`](tracks/monogenicity-index-divisor.md).

The correct height-one object is the entire semilocal algebra

```text
Cbar_p=Cbar tensor_B B_p,
```

not the separate DVR factors above `p`. For integral primitive `theta`, the index module and index ideal are

```text
M_theta=Cbar/B[theta],
I_theta=Fitt^B_0(M_theta),
```

with

```text
ord_p(I_theta)=length_{B_p}(Cbar_p/B_p[theta]),
Disc(B[theta]/B)=I_theta^2 Disc(Cbar/B).
```

The issue packet supplies candidate proofs that one element can generate every prescribed finite set of height-one semilocalizations, that generation at all height-one primes globalizes by `R1/S2`, and that a globally monogenic Keller normalization has degree one without circularity.

The generic algebraic elimination step is false. A smooth rational rank-three cover can be locally monogenic everywhere, have squarefree tame fixed-sheet branching and an open affine plane, yet have a universal index form that never represents a nonzero constant. The exact missing property in that model is etaleness of the specified open plane over the base.

The surviving bridge is therefore Keller-specific:

> Convert source etaleness on `A2 -> Y` into a unit-value theorem for the universal index form.

The first exact successor is the rank-three binary cubic index-form problem. Generic primitivity, distinct values on one fiber, parameter counts, class-group triviality, and local monogenicity are forbidden substitutes for the unit equation.

## Parallel sufficient criteria

The following are maintained only at the status assigned in [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md):

- principal Kähler different of the finite normalization;
- a unit-valued universal index form, hence a global monogenic normalization;
- global relative complete-intersection normalization;
- local finiteness of the canonical hyperbolic Euler field;
- local nilpotence/surjectivity of one canonical translation derivation;
- finiteness of one Brieskorn lattice in the affine target pencil;
- a simple component or trivial puncture monodromy;
- a filtration-compatible reduction lowering `kappa_w`.

Each would force invertibility, but the hypotheses are not presently known for every Keller pair.

## Stop rule

A research branch should stop when it has produced one of:

1. an independently checkable theorem covering a declared class;
2. a counterexample to a maintained candidate lemma;
3. a minimal blocked implication with all equivalent reformulations named;
4. a finite symbolic classification that is independently auditable.

Do not relabel the missing bridge as a lemma and treat it as proved.