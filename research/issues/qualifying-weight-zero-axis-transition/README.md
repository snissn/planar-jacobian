# Defect-Six Zero/Axis Transition for the Minimal Common-Power Core

```text
authority: MUTABLE_NONAUTHORITATIVE
role: research-worker
task_issue: 41
owned_path: research/issues/qualifying-weight-zero-axis-transition/
review_mode: local-adversarial-review
```

## Exact bounded disposition

This packet proves requested disposition **A** for the stated first terminal
configuration.

> **Theorem `ZAT-D6-NO-TRANSITION`.** Let `F=(P,Q)` be a normalized planar
> Keller pair over a characteristic-zero field, let `w=(p,q)` be primitive and
> positive, and suppose the actual grading defect is
> `kappa_w(P,Q)=6`. If the coprime common-power exponents of the complete top
> forms are `(2,3)` or `(3,2)`, then the complete defect-six Rees equations are
> inconsistent.

Consequently, under the global-minimal-counterexample assumptions in issue #41,
there is no defect-minimizing `{2,3}` face at defect six. In particular there is
no adjacent pair-changing transition through the origin, an axis vertex, or a
failure to share a nonzero component vertex. The complete transition list is
empty.

This is stronger than merely excluding a pair change, but it is restricted to
actual defect six and the coprime pair `{2,3}`. It is not a general defect-six
theorem.

## Proof architecture

The proof uses the full constant-bracket staircase rather than only `S_0` and
`S_1`.

1. The Rees identity gives

   ```text
   S_s=sum_(i+j=s) J(P_i,Q_j)=0, 0<=s<6,
   S_6=1.
   ```

   Hence some `J(P_a,Q_b)=c!=0` with `a+b=6`.
2. Determinant-one source and target transformations arrange `p<=q` and
   normalize the selected layers to

   ```text
   P_a=x,  Q_b=c y,
   ```

   without erasing `c` or changing layer indices.
3. If the top common root has weighted degree `rho`, then the selected degrees
   are `m rho-a` and `n rho-b`, in one of the two source-weight orders. A
   monomial of the nonconstant root implies `min(p,q)<=rho`; therefore
   `rho<=6`. Exact integer enumeration gives 16 raw orientations and, modulo
   the declared determinant-one signed source and target swaps, four normal
   forms.
4. In all four normal forms the common root has one monomial, so the top anchor
   is a nonzero coordinate-axis vertex. The full supported layers `P_0,...,P_6`
   and `Q_0,...,Q_6`, including literal zero layers, produce four explicit
   coefficient systems. Each contradicts `A B c!=0` before or at `S_3`.
5. For completeness, the checker enumerates every possible first adjacent wall
   incident to the normalized axis anchor. It finds nine coefficient branches;
   every adjacent-face ideal and every full Rees ideal saturates to the unit
   ideal. The source signed swap covers the opposite axis. No origin-anchor
   case exists.

The analytic proof of exhaustiveness is in
[`ANALYTIC_CLASSIFICATION.md`](ANALYTIC_CLASSIFICATION.md). The exact systems
are in [`DEFECT6_REES_SYSTEM.md`](DEFECT6_REES_SYSTEM.md).

## Main issue-local statements

- `ZAT-D6-ORIENT` — the exact arithmetic orientation space has 16 raw cases and
  four determinant-one normal forms;
- `ZAT-D6-REES` — every one of the four complete defect-six Rees systems is
  inconsistent after saturation by the leading coefficients;
- `ZAT-D6-WALL` — all nine normalized first-wall branches are inconsistent at
  the adjacent face equation and at the complete anchor staircase;
- `ZAT-D6-NO-TRANSITION` — the requested `{2,3}` pair-changing zero/axis
  transition cannot occur;
- `ZAT-D6-CHECK` — two independent exact implementations reproduce the
  arithmetic and symbolic classification and reject deliberate mutations.

These are issue-local labels. This worker packet allocates no `CLM-*` or proof
graph identifier.

## Dependency boundary

The contradiction is a fixed-weight defect-six calculation. The global
minimal-counterexample corollary additionally uses:

- the independently reviewed defect-at-most-four theorem;
- the exact independent acceptance of the fixed-weight defect-five theorem;
- the qualifying-weight packet's lexicographic minimal-counterexample setup,
  common-power lemma, and nonzero-shared-vertex constancy result.

The one-boundary Laurent/conductor packet is consumed only as a warning: a
positive Newton weight is a toric support datum and is not automatically the
valuation of every non-toric normalization boundary. This packet proves no
monomialization or no-escape theorem.

At construction time the serialized integration of predecessor PRs had not yet
landed on `main`; the scientific dependencies were read from their exact
validated heads. [`HANDOFF.md`](HANDOFF.md) records the required transplant and
base refresh before integration.

## Symbolic evidence

[`defect6_transition_checker.py`](defect6_transition_checker.py) independently
constructs every raw orientation, every supported Rees layer, `S_0` through
`S_6`, all nine normalized transition branches, saturations by declared
nonzero coefficients, and eight semantic mutations. Its default exact run
reports:

```text
defect-six zero/axis transition checker: PASS
raw orientations: 16
canonical cases: 4
transition branches: 9
negative mutations: 8
exact assertions: 74
```

[`review_defect6_transition.py`](review_defect6_transition.py) imports none of
the construction checker. It independently rederives the 16 orientations,
rebuilds the four full systems, verifies four decisive subideals, and tests nine
review mutations.

Computation is regression and falsification evidence. The finite search is
exhaustive only because the analytic argument proves `rho<=6` and proves that
the generated layer supports are complete.

## Artifact map

- [`DEFINITIONS.md`](DEFINITIONS.md) — weights, layers, transitions, scalar and
  transformation conventions;
- [`TRANSITION_NORMAL_FORMS.md`](TRANSITION_NORMAL_FORMS.md) — exact orientation
  reduction and two-wall support geometry;
- [`DEFECT6_REES_SYSTEM.md`](DEFECT6_REES_SYSTEM.md) — complete `S_0,...,S_6`
  systems;
- [`CASE_TABLE.md`](CASE_TABLE.md) — orientation, wall, and disposition tables;
- [`ANALYTIC_CLASSIFICATION.md`](ANALYTIC_CLASSIFICATION.md) — theorem and
  exhaustive proof;
- [`COUNTERMODELS.md`](COUNTERMODELS.md) — nearest support/formal mutations and
  the exact condition each fails;
- [`REVIEW.md`](REVIEW.md) — pinned local-adversarial review;
- [`VALIDATION.md`](VALIDATION.md) — commands, bounds, outputs, and limitations;
- [`HANDOFF.md`](HANDOFF.md) — integration-maintainer handoff;
- [`INTEGRATION.json`](INTEGRATION.json) — issue-owned integration contract.

## Scientific nonclaims

This packet does not prove a general defect-six theorem, termination for
arbitrary common-power cores, existence of a universal qualifying weight,
monomialization of non-toric normalization boundaries, or `JC_2`. It does not
infer that all positive faces share one global common composite. Passing
symbolic checks or eventual transport to `main` does not promote the theorem
beyond its recorded review status.
