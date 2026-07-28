# Case table

> Authority: `MUTABLE_NONAUTHORITATIVE`

| Case | Exact test | Disposition | Dependency / nonclaim |
|---|---|---|---|
| Unique boundary, generically unramified | purity and connected finite étale cover | excluded by predecessor packet | `CLM-071`; not reproved here |
| Ramified branch preserved by nontrivial target `G_m` | actual action, finite-isogeny lift, source-open invariance | excluded by predecessor packet | `CLM-070`; conditional on its cited equivariant Keller theorem |
| Pole-supported ramified branch with nonzero normalized `[P dQ]` | residue or de Rham class | **excluded by `NTLC-04/06`** | new substantial non-toric subclass |
| Rational normalized branch | all residues of `P dQ` | residue-free iff rationally exact | later conductor and higher recursions remain |
| Smooth exact three-puncture branch (5.1) | `P dQ=dR` | survives order zero | non-toric; no locally finite logarithmic field from current data |
| Singular exact branch | `R in Abar` and class in `Abar/A_C` | finite conductor class recorded | nonzero class is an exclusion only when the declared gluing problem requires target descent |
| Fixed type with first nonexact `beta_r` | equation `d c_(m+r)=-beta_r/m` | inconsistent at finite order `r` | explicit differential obstruction |
| All `beta_r` exact | recursive coefficients exist up to constants | formal all-orders survivor | algebraization and polynomial realization not implied |
| Neither `x` nor `y` has a pole at `E` | hypothesis `NTLC-H5` fails | outside this packet | no automatic proof that this case is empty |
| Candidate pole weight with `kappa<=4` | compute all monomials of `P,Q` | automorphism | reviewed fixed-weight theorem |
| Candidate pole weight with `kappa=5` | compute all monomials of `P,Q` | conditional automorphism only | issue #38 is open on the pinned base |
| Arbitrary `e,m`, local equations only | formal controls | no uniform local bound | does not prove actual Keller types unbounded |
| Full one-boundary class | all rows plus algebraization/support topology | open | no general theorem or finite list claimed |

## First supported disposition

The packet returns disposition 4 from the requested list:

```text
a substantial named one-boundary subclass is excluded.
```

The excluded subclass is the **Liouville-nonexact non-toric class**. The packet
also achieves disposition 8 at a smaller boundary:

```text
the remaining pole-supported class reduces to normalized Liouville exactness,
finite conductor/gluing data, all higher differential classes beta_r,
polynomial algebraization, and global Newton-support control.
```

It does not return a finite list because no uniform bound on ramification,
poles, conductor, punctures, semigroup generators, genus, or branch
multiplicity is proved.
