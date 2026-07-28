# Foundations and the Literature-Bound Rank-Three Exclusion

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claims: R3BC-01, R3BC-02
base_commit: 652a5e252626fa5816445651245e8a8946cee53e
```

## 1. Exact Keller setup

Let

```text
A = C[x,y],
B = C[P,Q] = C[u,v],
K = Frac(B),
L = Frac(A) = C(x,y),
F=(P,Q): Spec(A) -> Spec(B).
```

Assume

```text
J(P,Q)=P_x Q_y-P_y Q_x in C*.
```

Then `P,Q` are algebraically independent, `B` is a polynomial ring in two
variables, and `F` is étale. In particular `F` is quasi-finite. Let `O` be the
integral closure of `B` in `L`; the predecessor packet uses the finite
normalization factorization

```text
Spec(A) -> Y=Spec(O) -> Spec(B),
```

where the first arrow is an open immersion and the second is finite. The
rank-three branch assumes

```text
[L:K] = rank_B(O) = 3.
```

The equality between rank and field degree is immediate for a finite torsion-free
`B`-module whose generic fiber is `L`.

The Orevkov terminal argument needs only the polynomial map, constant Jacobian,
and field degree. Finite local freeness, trace splitting, normality, connectedness,
and the source-open factorization are retained for the internal binary-cubic
calculations but are not additional hypotheses of the terminal contradiction.

## 2. Field degree equals generic sheet number

### Lemma 2.1 — finite localization

If `[L:K]=n<infinity`, there is `h in B-{0}` such that `A_h` is finite over
`B_h`.

### Proof of Lemma 2.1

The elements `x,y` are algebraic over `K`. For each one, choose a monic
polynomial over `K`, then clear all denominators except the leading coefficient.
After inverting the product `h` of those denominators, both `x` and `y` are
integral over `B_h`. Since `A_h=B_h[x,y]`, it is finite over `B_h`. Its generic
rank is `[L:K]=n`. ∎

### Lemma 2.2 — reduced generic fibers under the Keller hypothesis

After replacing `h` by a multiple, `A_h` is finite étale of rank `n` over
`B_h`. Hence every geometric fiber over `Spec(B_h)` has exactly `n` reduced
points.

### Proof of Lemma 2.2

The Jacobian determinant is a unit in `A`, so `Omega_{A/B}=0`. Localization
preserves this equality. A finite morphism of finite presentation with vanishing
relative differentials is unramified; after shrinking the regular target once
more to the finite-flat locus, it is finite étale. A finite étale algebra of
rank `n` over an algebraically closed residue field is the product of `n` copies
of that field. ∎

### Corollary 2.3

If `[L:K]=3`, the polynomial map `F:C2 -> C2` is three-sheeted in the standard
generic sense: a general target point has exactly three preimages.

This is the only bridge needed to apply Orevkov. It also separates generic sheet
number from global properness: the map may lose sheets over the nonproperness
locus, but that does not change its generic three-sheeted degree.

## 3. Primary literature terminal

### Orevkov's theorem

The primary publication record states:

> The Jacobian of a three-sheeted polynomial mapping `C2 -> C2` cannot be a
> constant.

Source:

- S. Yu. Orevkov, “On three-sheeted polynomial mappings of `C^2`,”
  *Mathematics of the USSR-Izvestiya* **29**:3 (1987), 587–596.
- DOI: `10.1070/IM1987v029n03ABEH000984`.
- Primary record: <https://www.mathnet.ru/eng/im1571>.

The exact source status and access limitations are recorded in
[`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md).

### Literature-bound application 3.1 — no rank-three planar Keller map

There is no polynomial map

```text
F=(P,Q): C2 -> C2
```

such that

```text
J(P,Q) in C*
and
[C(x,y):C(P,Q)] = 3.
```

### Proof

By Corollary 2.3, such a map is three-sheeted. The externally proved and
primary-source-audited theorem of Orevkov says the Jacobian of a three-sheeted
polynomial map cannot be constant. This contradicts `J(P,Q) in C*`. The
application is therefore `literature_bound`; the packet proves the
field-degree-to-sheet bridge but does not reprove Orevkov's theorem. ∎

### Corollary 3.2 — no actual rank-three Keller normalization

Under the finite-normalization hypotheses of the issue #3 program, the
additional assumption `rank_B(O)=3` is impossible.

### Scope note

This closes the rank-three leaf by exclusion, not by constructing a power basis.
The logical sentence

```text
for every rank-three Keller normalization O, there exists s with Phi(s) in C*
```

is vacuously true after the literature-bound application, but recording it as a
constructive unit-value theorem would be misleading. No section is produced and
no method is supplied for higher rank.

## 4. Conditional rank-three algebra retained from the predecessor

For the internal calculation, temporarily set aside the literature-bound
exclusion and assume a finite locally free rank-three normal `B`-algebra `O`
with generic field `L`. Since
`3 in C*`, trace splitting gives

```text
O = B . 1 direct_sum E,
E = ker(Tr_{O/B}).
```

The predecessor proves that `E` is a free rank-two `B`-module. For `s in E`,

```text
Phi(s) = 1 wedge s wedge s^2 in det(O)
```

becomes a binary cubic after a frame of `E` and a trivialization of `det(O)`.
Its value controls the exact order index:

```text
Fitt_0^B(O/B[s]) = (Phi(s)),
Disc(B[s]/B) = Phi(s)^2 Disc(O/B).
```

Thus `Phi(s) in C*` is equivalent to `B[s]=O`. The coefficient/content ideal,
finitely many gcd-one values, and generic primitivity are all weaker.

The next files sharpen this conditional algebra even though Orevkov has already
excluded its occurrence for a Keller source.

## 5. Dependency boundary

Inherited and not promoted here:

- the finite-normalization/open-immersion baseline (`CLM-003` and `L12`);
- finite local freeness in the predecessor's exact hypotheses;
- finite-prime semilocal adaptation (`CLM-029`);
- `R1/S2` globalization and the monogenic degree-one implication
  (`CLM-031`, `CLM-034`);
- the intrinsic binary cubic and differential congruence (`CLM-062`–`CLM-065`);
- boundary-only support of the relative different (`CLM-066`).

No assertion that `K_Y` equals the reduced boundary, that all ramification
indices are two, or that exactness removes higher principal parts is used.
