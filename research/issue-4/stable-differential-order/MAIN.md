# Issue #4 — Finite Stable Differential Order Route

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** the stable-order implication is proved at candidate scope; existence remains open and is obstructed at every ramified height-one valuation.

## Identity and scope

- Repository: `snissn/planar-jacobian`
- Issue: `#4`, finite stable differential order
- Leaf: `research/leaf-packets/L02-stable-order.md`
- Branch: `issue-4/stable-differential-order-gpt56`
- Pinned rich baseline: `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`
- Base field: `C`
- Keller pair: `P,Q in C[x,y]` with `J(P,Q)=P_x Q_y-P_y Q_x=1`
- Base ring: `B=C[P,Q]`, identified with `C[U,V]`
- Fraction fields: `K=Frac(B)` and `L=C(x,y)`
- Finite normalization: `Cbar`, the integral closure of `B` in `L`

An **order** means a finite commutative `B`-subalgebra `M` of `L`, containing `B`, whose total quotient field is `L`. A finite `B`-module that is not closed under multiplication is not an order.

## Disposition

No finite stable order is constructed here. The packet gives two exact candidate results:

1. **Stable-order implication.** If a finite locally free `B`-order `M` in `L` is stable under both canonical derivations, then its trace discriminant is the unit ideal, `M/B` is finite etale, and `[L:K]=1`.
2. **Ramified-DVR obstruction.** At a height-one prime where `L/K` has ramification index greater than one, a derivation transverse to that prime preserves no full finite local lattice at all. Since the canonical pair contains a transverse derivation at every irreducible target divisor, any global stable order would already force absence of codimension-one ramification.

The second result is stronger than failure of the normalization: at a ramified DVR it excludes every valuation-bounded full module, even before asking for multiplicative closure.

## 1. Canonical derivations: signs and commutator

Define

```text
D_P =  Q_y partial_x - Q_x partial_y,
D_Q = -P_y partial_x + P_x partial_y.
```

Then

```text
D_P(P) = Q_y P_x-Q_x P_y = J(P,Q) = 1,
D_P(Q) = Q_y Q_x-Q_x Q_y = 0,
D_Q(P) = -P_y P_x+P_x P_y = 0,
D_Q(Q) = -P_y Q_x+P_x Q_y = J(P,Q) = 1.
```

Thus `D_P|_B=partial_P` and `D_Q|_B=partial_Q`. The commutator kills both generators:

```text
[D_P,D_Q](P)=0,
[D_P,D_Q](Q)=0.
```

Because `P,Q` are algebraically independent and `L/K` is finite separable in characteristic zero, every `K`-derivation of `L` vanishes. Hence

```text
[D_P,D_Q]=0.
```

This also gives an independent conceptual check of the coordinate calculation: the two fields are the lifts of the commuting target translations.

## 2. Trace compatibility for an invariant order

Let `delta` be either `partial_P` or `partial_Q`, and let `D` be the corresponding lift. Assume `M` is a finite locally free `B`-order and `D(M) subset M`.

Work over an open set on which `M` has basis

```text
e = (e_1,...,e_n)
```

written as a row vector. Define the connection matrix `A=(a_ij)` by

```text
D(e)=e A,
D(e_j)=sum_i a_ij e_i.
```

For `z in M`, let `M_z` be its multiplication matrix, so `z e=e M_z`. Applying `D` to this identity gives

```text
delta(M_z)=M_{D(z)}+[M_z,A].
```

Taking matrix traces kills the commutator:

```text
delta(Tr_{L/K}(z))=Tr_{L/K}(D(z)).
```

Multiplicative closure is used here. It ensures that multiplication by every `z in M` is a `B`-linear endomorphism of `M`, so its trace lies in `B`. A merely stable module has no such trace algebra.

## 3. Derivation matrix and determinant formula

Let

```text
G_ij = Tr_{L/K}(e_i e_j)
```

be the local trace Gram matrix. Trace compatibility and the Leibniz rule give

```text
delta(G_ij)
 = Tr(D(e_i)e_j)+Tr(e_iD(e_j)),
```

hence, in matrix form,

```text
delta(G)=A^T G+G A.
```

The generic trace pairing is nondegenerate because `L/K` is separable. Therefore `G` is invertible over `K`, and

```text
delta(det G)
 = det(G) Tr(G^{-1}delta(G))
 = det(G) Tr(G^{-1}A^T G+A)
 = 2 Tr(A) det(G).
```

The same identity follows integrally from the adjugate formula, so no inverse of `det G` is needed in `B`.

Under a basis change `e'=eU`,

```text
det(G')=det(U)^2 det(G),
```

with `det(U)` a local unit. Thus the local principal ideals `(det G)` glue to the trace-discriminant ideal sheaf, and the displayed formula proves

```text
delta(Disc(M/B)) subset Disc(M/B).
```

Applying this to both canonical derivations proves the exact content of CLM-011.

## 4. The only bi-translation-stable nonzero ideal is the unit ideal

Let `I` be a nonzero ideal of `B=C[P,Q]` stable under both partial derivatives. Choose a nonzero `f in I` of minimum total degree. If either `partial_P f` or `partial_Q f` is nonzero, it lies in `I` and has smaller total degree, a contradiction. Hence both partial derivatives vanish. In characteristic zero this forces `f` to be a nonzero constant. Therefore

```text
I=B.
```

The discriminant ideal is nonzero because the generic trace pairing of the finite separable field extension is nondegenerate. Consequently a stable order has unit discriminant.

## 5. Unit discriminant, finite etaleness, and degree one

The hypotheses used here are precise:

- `M` is a finite **locally free** commutative `B`-algebra;
- its generic algebra is the separable field `L`;
- its trace-discriminant ideal is the unit ideal.

For a finite locally free morphism, an everywhere nondegenerate trace pairing is equivalent to etaleness. Hence `Spec(M) -> Spec(B)=A^2_C` is finite etale.

Since `M` is a subring of the field `L`, it is a domain, so `Spec(M)` is connected. By the complex Riemann existence theorem for finite etale covers, this connected cover corresponds to a connected finite topological cover of `C^2`. The space `C^2` is simply connected, so the cover has one sheet. Thus

```text
rank_B(M)=[L:K]=1.
```

A unital finite locally free rank-one `B`-algebra is `B` itself. Therefore `M=B` and `L=K`.

This closes the implication recorded in CLM-013 at `candidate_proved` scope. It does **not** produce `M`.

## 6. Hidden hypotheses and exact replacements

### Local freeness versus torsion-freeness

Finite torsion-free modules over the regular surface `B` need not be locally free at closed points. The determinant calculation requires a finite projective module, equivalently local freeness, so that the connection has square matrices and the trace form has a determinant line. A sufficient replacement is: `M` finite and reflexive over `B`; on a regular surface a reflexive module is locally free. Passing to a double dual is not automatically harmless, because multiplicative closure and exact derivation stability must be reproved.

### Normality

Normality of `M` is not used in the discriminant criterion. The finite normalization `Cbar` is normal and, under the standard finite equidimensional surface hypotheses, is Cohen--Macaulay and finite locally free over the regular ring `B`. An arbitrary suborder need not be normal, Cohen--Macaulay, reflexive, or flat.

### Trace pairing

The trace is the field trace on the generic fiber, represented by multiplication on the order. Separability is essential for generic nondegeneracy. Characteristic zero supplies separability here.

### Multiplicative closure

Closure under multiplication is indispensable. It places all multiplication matrices and traces in `B` and makes `Spec(M)` a finite cover. A stable finite module without an algebra structure cannot support the stated discriminant-to-etale argument.

### Connectedness

Finite etale algebras can be products. Connectedness follows here only because the order is a subring of the field `L`.

### Base field

The degree-one conclusion uses the triviality of connected finite etale covers of `A^2_C`. It is not a field-independent assertion.

## 7. The existence tension

Two obvious algebras occupy opposite sides of the gap:

- `C[x,y]` is exactly stable under `D_P,D_Q`, but its finiteness over `B` is the unresolved global issue; using that finiteness would already force the Keller map to be finite etale.
- `Cbar` is finite and locally free over `B`, but at a ramified height-one valuation the exact target translations acquire poles and do not preserve it.

The local theorem in `local-dvr-obstruction.md` shows that this is not repaired by choosing a clever bounded lattice. In a ramified extension, no full finite local lattice can be invariant under a transverse exact translation.

## 8. Keller-specific local consequence

Let `h(P,Q)` be an irreducible nonconstant polynomial and localize `B` at the height-one prime `(h)`. At least one of

```text
partial_P h, partial_Q h
```

is not divisible by `h`, hence is a unit in `B_(h)`. The corresponding canonical derivation is transverse to the divisor. If a valuation of `L` over `(h)` has ramification index `e>1`, the ramified-DVR theorem excludes every stable full lattice after localization. Therefore a global finite stable order can exist only if the finite normalization is unramified at every height-one prime.

The Keller identity used here is exactly the dual-frame identity

```text
D_P(P)=1, D_P(Q)=0,
D_Q(P)=0, D_Q(Q)=1.
```

It guarantees a transverse exact translation at every reduced target divisor. It does not cancel differential pole growth. In the Kummer model the only way to prevent that growth is `e=1`.

## 9. What is and is not established

Established as mutable candidates:

- the canonical signs and commutator;
- trace compatibility;
- the local matrix and determinant formulas;
- derivative simplicity of `C[P,Q]`;
- stable order implies finite etale and degree one;
- ramification forces unbounded differential pole growth on every full finite local lattice;
- all audited standard lattice constructions fail in the ramified model.

Not established:

- existence of a global finite stable order;
- absence of all ramification or nonproperness for an arbitrary planar Keller map;
- a proof of the planar Jacobian conjecture.

## Artifact map

- `local-dvr-obstruction.md`: local theorem, repeated-derivative formula, tame non-Galois, cusp, and boundary models.
- `construction-audit.md`: finite-generation, local-freeness, multiplication, matrices, discriminants, and mutations for each proposed construction.
- `source-bindings.md`: primary-source theorem bindings and hypothesis map.
- `adversarial-review.md`: blocking self-audit and promotion boundary.
- `HANDOFF.md`: smallest next calculation and exact continuation state.
