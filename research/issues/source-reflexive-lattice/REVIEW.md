# Declared Adversarial Review

> **Review mode:** `local-adversarial-review`
> **Reviewed revision:** `8ad9d542e5177a3240ad6c1f02b8b75e7657a085`  
> **Candidate aggregate SHA-256:** `963a7f5b7c30d033574b16a1d5dfcec8742ec85edf682cea316dc9bfbdd6e659`  
> **Disposition:** `PASS_FOR_MUTABLE_MAINLINE_INTEGRATION`  
> **Promotion disposition:** `BLOCK`  
> **Authority after review:** `MUTABLE_NONAUTHORITATIVE`

## 1. Scope of review

The review covers the exact files listed in
`CANDIDATE_MANIFEST.sha256` at the reviewed revision.  It does not review the
later synchronization edits, this review record itself, or any theorem beyond
the packet's stated characteristic-zero finite-normalization scope.

The same assistant constructed and adversarially reviewed the candidate in declared
`local-adversarial-review` mode. Repository governance permits this fallback
when no distinct reviewer is available, but it is not independent scientific
acceptance and cannot promote any claim to `reviewed_scoped`. The mode-name
correction in packet metadata is editorial and does not alter the pinned
candidate theorem bytes.

## 2. Attack: ring orientation and boundary purity

**Attempted failure.**  Reverse the Zariski-Main ring map, or silently replace
`Y\U` by a pure divisor.

**Result.**  The packet consistently uses `O -> A`.  It separates the full
closed complement from its divisorial part and invokes normal-surface
Hartogs extension only for rational functions.  The proof does not require
purity of the whole complement.  If no divisorial component exists, the two
affine coordinate rings agree and the open immersion is an isomorphism.

**Disposition.**  Pass.

## 3. Attack: fixed-derivation equivalence

**Attempted failure.**  A non-normal or non-reflexive lattice might evade the
Kummer obstruction, or logarithmic tangency might fail to preserve the
normalization after a residue-field extension.

**Result.**  The forward implication uses only valuation boundedness of a
finite full lattice.  Strict henselization and projection to a ramified
factor preserve finiteness, fullness, and stability.  The converse treats the
unramified residue extension by etale lifting and the tame ramified factor by
`t=u s^e`; `delta(t) in (t)` makes `D(s)/s` regular.  Normality then recovers
`O` by intersection of its height-one localizations.

**Correction already incorporated before pinning.**  “No ramification” is
stated as unramifiedness of the full DVR extension, not merely the numerical
condition `e=1`.

**Disposition.**  Pass within the declared excellent characteristic-zero
hypotheses.

## 4. Attack: two-derivation strengthening

**Attempted failure.**  Both partials of an irreducible branch equation might
vanish generically, or one derivation might suffice globally.

**Result.**  In characteristic zero a nonconstant irreducible polynomial
cannot divide both lower-degree partials.  Hence the canonical pair always
contains a transverse member.  The control `h=Q=s^e` shows why either
individual canonical derivation can be tangent and harmless; both, or one
specified transverse derivation, are essential.

The implication from height-one unramifiedness to degree one additionally
uses the finite-flat surface package, purity, and connected finite-etale
cover triviality.  Those are explicit dependencies rather than consequences
of the residue calculation alone.

**Disposition.**  Pass; no unconditional no-ramification theorem is claimed.

## 5. Attack: intrinsic fractional spectrum

**Attempted failure.**  Change the uniformizer, complete, introduce a
nontrivial separable residue extension, or shift the lattice.

**Result.**  The semisimplified tame spectrum is identified with the intrinsic
value-group quotient `(1/e)Z/Z`.  Uniformizer and lattice changes alter
representatives by integers; completion preserves ramification data; strict
henselization separates the residue extension into `f` copies.  The packet
does not claim that all regular nilpotent correction terms vanish before
semisimplification.

**Disposition.**  Pass.

## 6. Attack: cancellation between `D_P` and `D_Q`

**Attempted failure.**  Shift the two residue coordinates independently, use
commutativity to cancel poles, or use only the determinant residue.

**Result.**  The pair is the normal covector `(h_P,h_Q)` times one scalar class
`j/e`.  A normal/tangent frame gives `(j/e,0)`.  A lattice shift changes a
character by an integral multiple of that same normal covector, not by two
independent integers.  The tame residue matrices commute but retain their
eigenvalue classes.  The determinant sum `(e-1)/2` is integral for odd `e`,
which is an explicit countercontrol against determinant-only reasoning.

**Correction already incorporated before pinning.**  The commutator argument
is stated in tame normal form rather than relying on a potentially ambiguous
“divisible by `h`” operator statement.

**Disposition.**  Pass.

## 7. Attack: source-pole union and finite stages

**Attempted failure.**  Use codimension-two points, claim a pole module is not
finite over `B`, invoke Noetherian stabilization, or hope commutativity gives
a uniform stage.

**Result.**  Height-one valuation inequalities give the exact multi-index
union and the diagonal union.  Coherence and `B`-finiteness follow from
normality, affineness, and finiteness of `Y/B`.  `B`-local freeness is stated
only under the finite-flat normal-surface package and is justified through
depth two.  The pole-shift vectors add under mixed iterates; the modules
containing the iterates are not one fixed Noetherian ambient module.

At a ramified component, the predecessor no-lattice theorem excludes every
finite full stage.  At an unramified omitted component, a transverse member
of the etale frame raises any genuine negative pole by one.  The source
conductor is zero because an omitted height-one prime supplies elements with
unbounded negative valuation.

**Correction already incorporated before pinning.**  The local-freeness
statement now exposes its finite-flat dependency and depth argument.

**Disposition.**  Pass.

## 8. Attack: multiplier ring bridge

**Attempted failure.**  The multiplier ring might be nonfinite, have generic
field smaller than `L`, lose derivation stability, or cease to be a ring after
reflexive closure.

**Result.**  It embeds in the finite module `End_B(M)`; clearing denominators
shows generic field `L`; the Leibniz identity proves stability; and the
reflexive hull is the intersection of height-one localized rings.  Over the
regular surface `B`, that reflexive order is locally free.  Thus the
predecessor trace/discriminant theorem applies.

For rank-one reflexive fractional `O`-modules, height-one localization proves
`(I:I)=O`, so the construction does not secretly generate a different stable
order from a divisorial candidate.

**Disposition.**  Pass.  The bridge is conditional on the still-missing
finite stable module.

## 9. Attack: exact symplectic overreach

**Attempted failure.**  Treat the Laurent boundary model as a polynomial
Keller counterexample, or infer that an exact primitive eliminates all
principal parts.

**Result.**  The control explicitly lives on `G_m x A^1` and has Laurent
`Q`; it is not a polynomial Keller pair on `A^2`.  It proves only that the
local identities `dP wedge dQ=dx wedge dy` and an exact primitive relation can
coexist with a ramified omitted divisor.  The packet separately cites the
full principal-part warning from issue #5.

**Disposition.**  Pass.

## 10. Countercontrol coverage

The reviewed bytes include:

- `t=s^e`;
- tame non-Galois cubic ramification;
- cusp branch and logarithmic Euler field;
- several boundary components;
- unramified nonproper boundary;
- exact versus logarithmic derivations;
- a nonstabilizing source-pole union;
- characteristic-`p` coefficient collapse; and
- the Laurent exact-symplectic boundary model.

The symbolic scripts reproduce the displayed Kummer iterates, determinant
residue sum, cusp tangent combination, pole shifts, Laurent Jacobian, and
exact primitive identity.

## 11. Remaining blockers

1. No finite pair-stable source-derived module is constructed.
2. The primary-source theorem bindings have not received an independent
   source-by-source review.
3. The packet classifies divisorial/reflexive source-pole constructions; it
   does not rule out every conceivable finite non-divisorial construction.
4. No claim here proves the planar Jacobian conjecture.

## 12. Final review disposition

The candidate is coherent and sufficiently scoped for preservation on
`main` as a mutable obstruction packet.  No fatal error was found in the
reviewed argument under its stated hypotheses.

Promotion, freeze, or `reviewed_scoped` status is **BLOCKED** because the
review is not independent and the background source bindings remain
reviewable.  Mainline integration is transport, not acceptance.
