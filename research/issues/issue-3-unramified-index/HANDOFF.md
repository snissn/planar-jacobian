# Handoff — Issue #3 / L01

```text
authority: MUTABLE_NONAUTHORITATIVE
engineering_status: DEVELOPMENT
execution_validity: NOT_A_SCIENTIFIC_EXECUTION
protocol_verdict: null
scientific_inference: scoped obstruction and narrowed successor only
```

- **Branch:** `issue-3/unramified-index-gpt56`
- **Pinned base:** `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`
- **Disposed leaf:** `L01-unramified-index-elimination`
- **Successor:** `L14-keller-index-form-unit`

## Exact disposition

The original question splits into three statements.

1. **Finite ramification adaptation is valid.** For every finite set of
   height-one base primes, one integral primitive element generates the whole
   semilocal normalization over each selected DVR. In particular, one element
   generates all ramified height-one semilocalizations.
2. **Codimension-one equality globalizes.** If one element generates at every
   height-one base prime, the hypersurface order is `S2` and `R1`, hence equals
   the normalization. In the Keller setting, the minimal-polynomial
   derivative then forces degree one without circularity.
3. **Purely algebraic unramified elimination is false.** A smooth rational
   rank-three normal finite-flat algebra is locally monogenic on the entire
   base, has squarefree tame branch with a fixed unramified sheet over each
   branch component, and contains an open affine plane, yet its index form
   never represents a unit.

The remaining theorem must use etaleness of the specified Keller source.

## Strongest countermodel

Let `B=C[u,v]` and let `O` have basis `1,w,e` with

```text
w^2=w-u e,
we=-uv,
e^2=v(w-1).
```

Then

```text
Phi(X,Y)=-(uX^3+X^2Y+vY^3),
Disc(O/B)=-v(4+27u^2v).
```

The algebra is connected, smooth, normal, finite flat, rational, locally
monogenic everywhere, and generically non-Galois. Both branch components are
simple: the cubic has one double root and one simple root at each generic
branch point.

No `x,y in C[u,v]` satisfy `Phi(x,y) in C*`. Setting `u=0` would force a
nonconstant linear polynomial in `v` to be a square. Thus every
ramification-adapted element has nonempty index support at unramified generic
points.

For

```text
theta_lambda=w+lambda e,
```

one has

```text
ind(theta_lambda)=-(u+lambda+lambda^3v).
```

The collision line moves with `lambda` and never disappears.

The surface contains

```text
X_0=Y-V(u,1-w) isomorphic to A2_{u,s},
```

and the finite map restricts to

```text
(u,s) |-> (u,us^3-s^2),
J=s(3us-2).
```

Hence the open plane is not an etale source. This is why the model is not a
Keller counterexample.

## Banked candidate theorems

- Exact semilocal special-fiber generation criterion.
- Fitting/index length and square-discriminant formulas.
- One primitive element simultaneously adapted at any finite set of
  height-one base primes.
- Height-one generation implies global equality by `R1/S2`.
- Global monogenicity of a Keller normalization implies degree one.
- Every rank-two finite locally free algebra over `C[P,Q]` is globally
  monogenic.
- Whole-base affine-linear primitive transitions globalize; a punctured-base
  cover is insufficient without cocycle extension.

## Countercontrols retained

- `A x A` over a DVR: factorwise projection is not semilocal generation.
- Diagonal cubic: locally but not globally monogenic; mutation depends on
  `lambda^3`.
- Rational corank-two cubic: square-zero embedding-dimension-two special
  fiber.
- Biquadratic Galois cover: exact Vandermonde collision line.
- Tame non-Galois DVR extension: local monogenicity with mixed residue degree
  and ramification.
- Smooth rational fixed-sheet cubic: open affine plane present, source
  etaleness absent.

## Smallest unresolved calculation

The first exact successor is the **rank-three Keller binary-index-form unit
problem**.

Assume a hypothetical rank-three Keller normalization is finite locally free.
Use `(1/3)Tr` to split

```text
O=B direct_sum E,
rank_B(E)=2.
```

For `s in E`, define the intrinsic cubic index section

```text
Phi(s)=det(1,s,s^2).
```

In a local frame `s=Xe_1+Ye_2`, this is a binary cubic. Ramification
adaptation supplies a global section with

```text
gcd(Phi(s),Disc(O/B))=1.
```

The smallest remaining task is:

```text
Use the actual open immersion A2_source -> Y together with
J(P,Q)=1 on A2_source to prove that Phi(s) is a nonzero constant
for some integral section s.
```

Equivalently, find one exact differential, canonical-derivation, boundary, or
fixed-sheet identity implied by source etaleness that excludes the explicit
pattern

```text
uX^3+X^2Y+vY^3
```

and its moving lines `u+lambda+lambda^3v`.

A proof in rank three is a rigorous restricted theorem even if higher ranks
remain open. A Keller-compatible countermodel would need to retain the
specified etale open `A2_source`; the present algebraic countermodel does not.

## Validation commands

```bash
python3 -m compileall -q scripts research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 scripts/validate_repository.py
python3 scripts/frontier.py
git diff --check
```

The symbolic verifier recomputes associativity, index determinants, trace
discriminants, the Galois Vandermonde identity, the mutation family, and the
open-plane Jacobian. These are process checks, not theorem acceptance.

## Review state

The constructor adversarial pass reports no known internal blocker after
corrections, but it is not independent. Freeze or promotion remains blocked
pending independent review of the load-bearing local patching,
globalization, and fixed-sheet countermodel arguments.

## Stop-rule status

```text
SATISFIED — SCOPED ALGEBRAIC OBSTRUCTION.
```

The generic moving-index bridge is false. The positive ramification-adaptation
and globalization sublemmas are banked, and the Keller etale-source successor
is isolated exactly.
