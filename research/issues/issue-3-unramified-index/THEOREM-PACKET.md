# Theorem Packet: Index, Ramification Adaptation, Globalization, and Degree One

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
```

## 1. Setup and the correct height-one object

Let

```text
B = C[P,Q] = C[u,v],   K = Frac(B),   L = C(x,y),
O = Cbar = the integral closure of B in L,
Y = Spec(O).
```

Assume the finite-normalization factorization from `CLM-003`, and write `n=[L:K]`. The extension is separable because the Keller map is generically étale in characteristic zero.

### 1.1 Finite local freeness at the scope used below

The normalization `O` is finite locally free of rank `n` over `B`. Here is the argument at the exact scope consumed in this packet. At a height-one prime of `B`, the finite torsion-free module `O_p` is free over the DVR `B_p`. At a maximal ideal `m` of `B`, every localization `O_q` over `m` is a two-dimensional normal local domain, hence `S2` and therefore Cohen--Macaulay. A regular system of parameters of the regular local ring `B_m` is a system of parameters in every `O_q`; Cohen--Macaulayness makes it an `O_q`-regular sequence. Thus `depth_{B_m}(O_m)=2`. The Auslander--Buchsbaum formula over the two-dimensional regular local ring `B_m` gives projective dimension zero, so `O_m` is free. Hence `O` is finite locally free.

This proof is included so that the determinant/Fitting formulas do not silently consume the still-separate boundary audit in `L12`. No smoothness of `Y` is used.

For a height-one prime `p` of `B`, the relevant localization is

```text
O_p := O tensor_B B_p.
```

This is a finite **semilocal** algebra over the DVR `B_p`. Its maximal ideals are the height-one primes `q` of `O` lying over `p`, and each `O_q` is a DVR. Generation must be tested on the entire semilocal algebra `O_p`, not separately after projecting to each `O_q`.

The distinction is essential. For a DVR `A` with uniformizer `pi`, put `S=A x A` and `alpha=(0,pi)`. Each projection of `A[alpha]` to a factor is surjective, but

```text
A[alpha] = {(a,b) in A x A : a == b mod pi} != S.
```

The failure is the collision of the two residual sheets. A prime-by-prime test on the normalization factors misses it; the semilocal `B_p`-algebra detects it.

## 2. Integral primitive elements and the index module

Let `theta in O` be integral and primitive, meaning `K(theta)=L`. Its monic minimal polynomial `f_theta(T)` over `K` belongs to `B[T]`: its coefficients are integral over the integrally closed domain `B`, and hence lie in `B`. Monic division then gives

```text
R_theta := B[theta] = B[T]/(f_theta),
```

with free `B`-basis `1,theta,...,theta^(n-1)`.

Define the index module

```text
M_theta := O / R_theta,
```

as a finite torsion `B`-module. It is not naturally an `O`-module, which is another reason the base-prime semilocalization is the correct test.

The zeroth Fitting ideal

```text
I_theta := Fitt^B_0(M_theta)
```

is the index ideal. On an open set where `O` is free, choose a basis `e_1,...,e_n` and let `A_theta` be the inclusion matrix whose columns are the coordinates of

```text
1, theta, ..., theta^(n-1)
```

in that basis. Then, on that open set,

```text
I_theta = (det A_theta).
```

Without a chosen basis, `det A_theta` is the determinant section of

```text
det(R_theta) -> det(O).
```

Because `B=C[u,v]` has trivial Picard group, this determinant line is principal; its generator is unique up to `C*`.

For every height-one `p` of `B`,

```text
ord_p(I_theta) = length_{B_p}(O_p / B_p[theta]).
```

Thus the index divisor is

```text
Ind(theta) = sum_{ht(p)=1} length_{B_p}(O_p/B_p[theta]) [p].
```

## 3. Necessary-and-sufficient local criterion

### Proposition 3.1

For a height-one prime `p` of `B`, put `A=B_p`, `S=O_p`, `k=kappa(p)`, and let `bar(theta)` denote reduction modulo the maximal ideal of `A`. The following are equivalent:

1. `A[theta]=S`.
2. `(M_theta)_p=0`.
3. `I_theta A=A`.
4. The determinant of `1,theta,...,theta^(n-1)` in any `A`-basis of `S` is a unit.
5. `k[bar(theta)] = S/pS`.

#### Proof

The first four equivalences are the square-presentation/Fitting criterion over the DVR `A`. For (1) versus (5), reduce the inclusion `A[theta] subset S` modulo `p`. If the reductions agree, the finite `A`-module `S/A[theta]` satisfies `M=pM`; Nakayama gives `M=0`. The converse is immediate.

### Unramified specialization

If `O_p/B_p` is finite étale, then

```text
S/pS = product_r k_r
```

with finite separable residue extensions `k_r/k`. The criterion says that `theta` must generate every `k_r/k` **and** the corresponding minimal polynomials must be pairwise coprime. After extending to an algebraic closure of `k`, this is exactly pairwise distinctness of all geometric sheet values.

### Ramified specialization

At a ramified prime, pairwise distinct residual values are impossible inside an inertia orbit and are not the right condition. The full nonreduced Artin algebra `S/pS` must be generated. This includes both residue-field separation between different primes above `p` and a uniformizer direction inside each ramified factor.

## 4. Trace, discriminant, different, conductor, and Vandermonde

Let `Tr=Tr_{L/K}`. For a finite locally free order `A` in `L`, its discriminant is the determinant of the trace pairing. With the inclusion matrix above,

```text
Gram(R_theta) = A_theta^T Gram(O) A_theta,
```

and therefore

```text
disc(R_theta/B) = I_theta^2 disc(O/B)                     (4.1)
```

as ideals, up to the harmless unit determined by basis choices. At a height-one prime,

```text
v_p(disc(R_theta/B))
  = v_p(disc(O/B)) + 2 length_{B_p}(O_p/B_p[theta]).       (4.2)
```

For the monogenic order,

```text
Omega_{R_theta/B} = R_theta/(f_theta'(theta)) dtheta,
Different(R_theta/B) = (f_theta'(theta)).                  (4.3)
```

For the normal order `O`, write

```text
O^vee = {z in L : Tr(zO) subset B}.
```

The normal different is the inverse of this trace-dual lattice, interpreted divisorially. The inclusion `R_theta subset O` reverses under trace duality:

```text
O^vee subset R_theta^vee,
```

and the local lattice-index length is the same as that of `O/R_theta`. Formula (4.2) is the determinant form of this statement.

The conductor

```text
f_theta = (R_theta : O) = Ann_{R_theta}(O/R_theta)
```

has the same height-one support as the index module. It records where the monogenic order fails to be the normalization; it need not equal the Fitting ideal.

Consequences:

- At a ramified `p`, `disc(O/B)` already has the intrinsic different exponent. An additional factor in `disc(R_theta/B)` is index support.
- At an unramified `p`, `disc(O/B)` is a unit, so

```text
v_p(disc(f_theta)) = 2 length_{B_p}(O_p/B_p[theta]).
```

Every discriminant zero there is an accidental collision of an otherwise étale sheet configuration.

## 5. Simultaneous ramified height-one generation

### Lemma 5.1 — semilocal DVR monogenicity

Let `A` be a DVR with infinite perfect residue field `k`, fraction field `F`, and let `E/F` be finite separable. Let `S` be the semilocal integral closure of `A` in `E`, assumed finite over `A`. Then there exists `alpha in S` with

```text
S=A[alpha].
```

#### Proof

Write the special fiber as

```text
S/pi S = product_i S/q_i^(e_i).
```

Each factor is a local Artin `k`-algebra with principal maximal ideal and finite separable residue field `k_i/k`.

Choose a primitive residue element `beta_i` for `k_i/k`. Because `k_i/k` is separable, formal etaleness lifts the coefficient field `k_i` through the nilpotent ideal. If `tau_i` generates the principal maximal ideal, then

```text
S/q_i^(e_i) = k_i[tau_i]/(tau_i^(e_i)).
```

Put `z_i=beta_i+tau_i`. Let `g_i` be the separable minimal polynomial of `beta_i`. Inside the subalgebra `k[z_i]`, the element `g_i'(z_i)` is a unit. Finite Newton iteration, which terminates because the maximal ideal is nilpotent, constructs the unique root `beta_i' in k[z_i]` of `g_i` congruent to `z_i` modulo the maximal ideal. Hence

```text
tau_i=z_i-beta_i' in k[z_i],
beta_i=beta_i' in k[z_i],
```

so `z_i` generates the local factor.

Let `h_i(T)` be the annihilator polynomial of `z_i`. Translating `z_i` by a constant translates the finite root set of `h_i`. Because `k` is infinite, choose constants so that these finitely many translated root sets are pairwise disjoint; equivalently, the translated `h_i` are pairwise coprime. The Chinese remainder theorem then gives one generator of the product special fiber. Lift it to `S` and apply Proposition 3.1.

This proof uses neither a Galois hypothesis nor total ramification.

### Theorem 5.2 — simultaneous finite-prime adaptation

Let `S_0` be any finite set of height-one primes of `B`. Then there is `theta in O` such that

```text
B_p[theta]=O_p  for every p in S_0.
```

If `S_0` is nonempty, this `theta` is automatically primitive. If `S_0` is empty and `n>1`, add one auxiliary unramified height-one prime before applying the construction.

#### Proof

For each `p_i in S_0`, Lemma 5.1 gives a generator in `O_{p_i}`. Clear a denominator not in `p_i`; multiplication by that denominator is multiplication by a unit in `B_{p_i}`, so obtain a global `a_i in O` that still generates `O_{p_i}`.

Write `p_i=(f_i)`, using that `B=C[u,v]` is a UFD, and put

```text
h_i = product_{j != i} f_j,
theta = sum_i h_i a_i.
```

At `p_i`, every summand except `h_i a_i` vanishes modulo `p_i`, while `h_i` is a unit. Proposition 3.1 gives `B_{p_i}[theta]=O_{p_i}`. Equality at one prime forces the generic power span to have rank `n`, hence `K(theta)=L`.

### Corollary 5.3 — `CLM-029`

The ramified height-one set is finite because it is contained in the support of the nonzero discriminant ideal. Taking `S_0` to be that set proves that one integral primitive element generates all ramified height-one semilocalizations simultaneously.

### Limitation

The theorem patches a **prescribed finite set**. It gives no monotone control of new index primes. Reapplying it to the current index support may move the support rather than decrease it; the rank-three countermodel proves that termination cannot be expected algebraically.

## 6. Exact `R1/S2` globalization

### Theorem 6.1

Let `theta in O` be integral and primitive. If

```text
B_p[theta]=O_p
```

for every height-one prime `p` of `B`, then

```text
B[theta]=O.
```

#### Proof

Set `R=B[theta]=B[T]/(f_theta)`. Since `B[T]` is regular and `f_theta` is a nonzerodivisor, `R` is a hypersurface Cohen–Macaulay domain. In particular, `R` is `S2`.

Let `r` be a height-one prime of `R`, and put `p=r cap B`. Because `R/B` is integral and both are domains, incomparability rules out `p=(0)`, and dimension preservation gives `ht(p)=1`. By hypothesis, `R_p=O_p`. Localizing at the prime corresponding to `r` gives

```text
R_r = O_q
```

for a height-one prime `q` of `O`. The right side is a DVR because `O` is normal. Thus `R` is `R1`.

For completeness, the `R1+S2` conclusion can be seen directly. If `z in Frac(R)` lies in every `R_r` for `ht(r)=1`, the denominator ideal

```text
J={a in R : az in R}
```

is not contained in a height-one prime. If `z` were not in `R`, then `J` would be proper of height at least two. The `S2` condition supplies a regular sequence `a,b in J`. Since `az,bz in R` and `b(az)=a(bz)`, regularity of `b` modulo `a` forces `az in aR`, hence `z in R`, a contradiction. Therefore `R` is the intersection of its height-one DVR localizations and is integrally closed.

So `R` is normal. It contains `B`, has fraction field `L`, and is therefore the integral closure `O`.

In the present affine-plane base one can also see the last step through the index determinant: finite local freeness makes the inclusion `R -> O` a map of equal-rank vector bundles. Height-one equality says its determinant has no irreducible factor. Since the only units of `B` are `C*`, the determinant is a unit and the map is an isomorphism. The `R1/S2` proof above is retained because it is the exact normalization argument needed without relying on a chosen global module trivialization.

## 7. Degree one without circularity

### Theorem 7.1

Assume the Keller open immersion

```text
j: X=Spec(C[x,y]) -> Y=Spec(O)
```

and suppose `O=B[theta]`. Then `[L:K]=1`.

#### Proof

Let `f=f_theta` be the degree-`n` monic minimal polynomial. From the monogenic presentation,

```text
Omega_{O/B} = O/(f'(theta)) dtheta.
```

Restriction of relative differentials along the open immersion gives

```text
j^* Omega_{O/B} = Omega_{C[x,y]/B}.
```

The Keller Jacobian condition makes the right side zero. Hence `f'(theta)` restricts to a unit of `C[x,y]`, and therefore to a constant `c in C*`.

If `n>1`, the polynomial `f'(T)-c` has degree strictly less than `f` and vanishes at `theta`. This contradicts minimality of `f`. Thus `n=1`.

No degree-one statement is used in the globalization proof; the open immersion and the vanishing of relative differentials enter only after `O=B[theta]` has been established.

## 8. A closed restricted theorem in degree two

### Proposition 8.1

Every finite locally free rank-two `B`-algebra is globally monogenic.

#### Proof

The unit section splits as a direct summand: because `2` is invertible, `(1/2)Tr_{O/B}:O->B` is a retraction of `B*1 -> O`. Hence `O/B*1` is a projective rank-one, therefore invertible, `B`-module. Since `Pic(B)=0`, choose `theta` whose class is a basis. Then `O=B direct-sum B theta`, so multiplication expresses `theta^2` in that basis and `O=B[theta]`.

Consequently, a Keller normalization of field degree two is impossible by Theorem 7.1. Rank three is the first degree in which a locally monogenic finite-flat algebra can fail to have a global power basis.

## 9. Affine-transition restricted theorem and its boundary

### Proposition 9.1

Let `{U_i}` be a Zariski cover of all of `Spec(B)`. Suppose `O|_{U_i}=O_{U_i}[theta_i]` and on overlaps

```text
theta_j = a_ij theta_i + b_ij,
```

with `a_ij` invertible and `b_ij` regular. Then `O` is globally monogenic.

#### Proof

The linear coefficients define a `G_m` cocycle. `Pic(B)=0` trivializes it. After rescaling the `theta_i`, the remaining transition functions are additive. Because `Spec(B)` is affine, `H^1(Spec(B),O_B)=0`, so the additive cocycle is a coboundary. Translating the local generators then produces one global `theta`.

### Required qualification

If the cover exists only on `Spec(B)` minus a codimension-two set, Hartogs extension of individual regular functions does **not** by itself trivialize the additive torsor; `H^1` of a punctured affine surface need not vanish. The affine-transition route is proved only when the cocycle is defined on a cover of the whole base or is independently shown to extend there. This qualification blocks the unmodified wording of `CLM-033`.
