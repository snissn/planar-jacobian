# Local Residue Theorem and Codimension-One Equivalence

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-001`, `SRL-002`  
> **Characteristic:** equicharacteristic zero for the obstruction and the stated tame residue formula.

## 1. Local setup

Let `R` be an excellent DVR containing a characteristic-zero field, with fraction field `K`, uniformizer `t`, and residue field `kappa`. Let

```text
delta: R -> R
```

be a derivation transverse to the closed point:

```text
delta(t) in R^x.
```

Let `L/K` be a finite separable field extension and let `D` be the unique extension of `delta` to `L`. For a valuation `w` of `L` above the `t`-adic valuation, write

```text
S = O_w,       e = e(w/t),       f = [kappa(w):kappa]
```

for the valuation ring, ramification index, and residue degree.

A **full finite `R`-lattice** is a finite torsion-free `R`-submodule `Lambda subset L` satisfying

```text
Lambda tensor_R K = L.
```

Over a DVR it is automatically free. Multiplication is not assumed.

## 2. Sharp local theorem

### Theorem 2.1 (`SRL-001`, local form)

The following are equivalent at the fixed branch `w`.

1. There is a full finite `R`-lattice `Lambda subset L` with `D(Lambda) subset Lambda` after projection to the `w`-factor.
2. The ramification index is `e=1`.
3. The integral closure factor `S` is preserved by `D`.

The implication `1 => 2` needs only the one derivation `delta` transverse to `t=0`. The implication `2 => 3` uses separability of the residue extension; this is automatic in characteristic zero. The implication `3 => 1` uses `Lambda=S` in the local factor.

### Proof of `1 => 2`

Pass faithfully flatly to the strict henselization of `R`. Derivations extend uniquely through the ind-etale base change, the finite separable algebra decomposes into field factors, and projection of a stable full lattice to a factor is again stable and full. Idempotents are killed by derivations because

```text
D(e)=D(e^2)=2eD(e).
```

Characteristic zero makes the ramification tame. In a ramified factor, after absorbing a unit by Hensel's lemma, choose a uniformizer `s` with

```text
t=s^e.
```

Writing `a=delta(t)`, one has

```text
D(s) = a/(e s^(e-1)) = (a/e)t^(-1)s.
```

Every full finite lattice is commensurable with `S`, so for some integer `N`,

```text
t^N s in Lambda.
```

Repeated differentiation has a unique lowest-valuation term

```text
D^n(t^N s)
 = [product_(r=0)^(n-1)(N+1/e-r)] a^n t^(N-n)s
   + terms of larger s-valuation.
```

Every coefficient is nonzero when `e>1`, because `N+1/e-r` is never zero. Hence

```text
v_s(D^n(t^N s)) = e(N-n)+1 -> -infinity.
```

A finite lattice has a lower valuation bound, contradiction. Therefore `e=1`.

### Proof of `2 => 3`

When `e=1` and the residue extension is separable, `S/R` is unramified. After strict henselization the factor is a copy of the base DVR, and the extension of `delta` preserves it. Descent gives

```text
D(S) subset S.
```

Equivalently, formal etaleness gives the unique lift of the base derivation to the unramified algebra.

### Proof of `3 => 1`

Take `Lambda=S`. It is finite over `R`, full in its field factor, and stable.

## 3. Completion and strict henselization audit

Strict henselization and completion play different roles.

- **Strict henselization:** separates residue-field factors and turns tame ramification into the Kummer form after extracting roots of units. It is an ind-etale, faithfully flat base change. Stability base-changes, and nonexistence after this base change implies nonexistence before it.
- **Completion:** is optional for the valuation argument. If used, excellence preserves finiteness of normalization, and the completed factor again has the same ramification index. A stable finite lattice completes to a stable finite lattice. The repeated-derivative contradiction therefore survives completion.
- **Residue extensions:** before strict henselization, an unramified part of degree `f` remains. It changes multiplicities in the residue spectrum, not the fractional classes. In characteristic zero every finite residue extension arising here is separable.

No assertion uses a Galois hypothesis.

## 4. Intrinsic fractional residue spectrum

The residue classes are not defined by choosing the displayed Kummer basis. They are the exponents of the induced regular-singular differential module.

Choose any local equation `t` of the base divisor and any transverse derivation `delta`. Define the normalized logarithmic operator

```text
E_delta = (t/delta(t)) D.
```

It satisfies `E_delta(t)=t`. In the tame normalization it preserves an integral logarithmic lattice, for example `S`. Since `E_delta(R) subset tR`, it induces a `kappa`-linear residue endomorphism

```text
Res_w(E_delta): S/tS -> S/tS.
```

After extending the residue field algebraically, define

```text
Spec_frac(w) = eigenvalues(Res_w(E_delta)) modulo Z,
```

counted with multiplicity.

This is coordinate independent:

1. replacing `t` by `u t` with `u` a unit changes `E_delta` by an operator divisible by `t`, so the residue is unchanged;
2. replacing the logarithmic lattice shifts residue eigenvalues by integers, hence does not change their classes in `Q/Z`;
3. replacing the transverse derivation and renormalizing to `E(t)=t` gives the same normal operator modulo the maximal ideal;
4. strict henselization only splits the unramified multiplicity.

In the tame branch of index `e`,

```text
Spec_frac(w)
 = f copies of {0, 1/e, 2/e, ..., (e-1)/e} in Q/Z.
```

Thus

```text
Spec_frac(w)={0 with multiplicity f}
```

if and only if `e=1`. Integer shifts from conductor, different, or pole powers permute representatives but cannot erase a nonzero class.

## 5. Global canonical-frame equivalence

Let `k` be a characteristic-zero field, let

```text
B=k[P,Q],   K=Frac(B),   L/K finite separable,
O=normalization of B in L.
```

Assume `O` is finite over `B`. Let `D_P,D_Q` be the lifts of `partial_P,partial_Q`.

### Theorem 5.1 (`SRL-001`, global form)

The following are equivalent.

1. There exists a full finite reflexive `B`-lattice `M subset L` stable under both `D_P` and `D_Q`.
2. Every height-one valuation of `L` over `B` has ramification index one.
3. The normalization `O` is stable under both `D_P` and `D_Q`.

Under the maintained normal-surface hypotheses, `O` and every finite reflexive `B`-module in the statement are locally free over `B`.

### Proof of `1 => 2`

Let `p=(h)` be a height-one prime of `B`. In characteristic zero, an irreducible `h` cannot divide both `h_P` and `h_Q`. Thus at least one of

```text
partial_P h, partial_Q h
```

is a unit in `B_p`. Localizing `M` at `p` gives a full finite lattice stable under a transverse lifted derivation. The local theorem forces every branch above `p` to have `e=1`.

This is why both canonical derivations are required globally. Stability under `D_P` alone detects only divisors along which `partial_P h` is a unit; it says nothing about a divisor defined by a polynomial in `Q` alone. At a fixed divisor, one transverse derivation is enough.

### Proof of `2 => 3`

For every height-one prime `q` of `O`, the local extension `O_q/B_p` is unramified, where `p=q cap B`. Each base derivation therefore preserves `O_q`. Since `O` is normal,

```text
O = intersection_(ht(q)=1) O_q  inside L.
```

The lifted derivations preserve every factor in the intersection, hence preserve `O`.

### Proof of `3 => 1`

Take `M=O`. It is finite, full, reflexive, and stable.

## 6. Relation to finite etaleness and degree one

The theorem is a codimension-one equivalence. In the present surface setting it feeds directly into the predecessor result:

```text
no height-one ramification
  => O stable under D_P,D_Q
  => finite locally free stable order
  => unit discriminant
  => finite etale
  => degree one over C.
```

The packet does not prove the first line for an arbitrary Keller map. It proves that constructing the desired stable lattice is not a weaker route around ramification: it is equivalent to eliminating ramification in codimension one.

## 7. Exact characteristic-zero boundary

Characteristic zero is used in four load-bearing places:

1. `L/K` and residue extensions are separable;
2. every finite ramification is tame and `e` is invertible;
3. Kummer reduction `t=s^e` is available after the stated etale base changes;
4. the repeated-derivative factors do not vanish after finitely many iterations.

In characteristic `p`, even when `p` does not divide `e`, a factor in the length-`p` product can vanish modulo `p`; the derivation may become `p`-nilpotent on a branch. No characteristic-positive analogue is claimed here without additional hypotheses.
