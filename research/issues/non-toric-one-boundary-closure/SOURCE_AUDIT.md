# Source audit

> Authority: `MUTABLE_NONAUTHORITATIVE`

## 1. Pinned repository dependencies

This packet was constructed from

```text
main@652a5e252626fa5816445651245e8a8946cee53e.
```

The load-bearing internal inputs are:

- `research/issues/one-boundary-logarithmic-field/BOUNDARY_HYPOTHESES.md` for
  the exact one-boundary distinctions;
- `.../PRINCIPAL_PARTS.md` for the coefficient equations and the predecessor
  leading relation;
- `.../CONDUCTOR_AND_PUNCTURES.md` for curve normalization and finite conductor
  quotients;
- `.../LOGARITHMIC_MODULE.md` and `.../SEMISIMPLE_CLASSIFICATION.md` for the
  separation between logarithmic, locally finite, and algebraic fields;
- `research/issue-5/PRINCIPAL_PARTS.md` for the canonical lift signs and tame
  height-one tangency criterion;
- `research/leaf-packets/L11-exact-symplectic-boundary.md` for the rule that
  all principal parts, not only residues, must be retained;
- `research/tracks/m-filtered-equivariance.md` and the issue #17 freeze record
  for the exact reviewed defect-at-most-four scope.

The defect-five candidate is not consumed. Issue #38 was open when the base was
pinned.

## 2. Primary algebra sources

The following sources support only standard algebraic infrastructure; every
new coefficient identity and obstruction is proved in this packet.

1. **Complete equicharacteristic DVRs.** The Cohen structure theorem in the
   regular complete local case identifies a one-dimensional complete regular
   local ring containing `Q` with a power-series ring over a coefficient field:
   Stacks Project, Tag `0C0S`.
2. **Extensions of DVRs.** A target uniformizer pulls back as a unit times the
   `e`-th power of a source uniformizer: Stacks Project, Tag `09E4`.
3. **Tameness in residue characteristic zero.** The definition makes every
   finite separable height-one extension tame in residue characteristic zero,
   and Abhyankar's lemma permits the finite unramified/root extractions used in
   the normal form: Tags `09E9`, `0BRM`, and `0EXW`.
4. **Trace.** Field trace and separability are recorded in Stacks Project,
   Section `0BIE`. The identity

   ```text
   d Tr_(L/K)(a)=Tr_(L/K)(d a)
   ```

   used here follows directly after passing to a separable closure and summing
   the `K`-embeddings; no stronger trace theorem is invoked.
5. **Curve normalization.** One-dimensional normalization is integral with
   finite fibres and normalized affine pieces are Dedekind: Tag `0C45`.
   For finite-type complex curves, finiteness follows from the Nagata property.
6. **Conductor.** The conductor is the annihilator of the finite normalization
   quotient and is an ideal on both rings; the standard sheaf description is
   displayed in Stacks Project, Section `0C6L`.

## 3. Internally proved steps

No external source is used for:

- the sign in `P dQ+y dx=dH`;
- the order-`e` target two-form estimate;
- the normalization `s=x^(-1/m)` after a finite coefficient extension;
- the all-order recursion `d c_(m+r)=-beta_r/m`;
- the resonant equation `c_m=0`;
- normalized branch exactness `P dQ=dR`;
- the two explicit non-toric branch calculations;
- the support mutation explaining why a bounded weight does not follow.

Each is rechecked by `validate_laurent_conductor.py` where it is symbolic.

## 4. External theorem deliberately not used

The new Liouville-exactness theorem does not invoke the recent equivariant
Keller preprint used by the predecessor torus subclass. That theorem remains a
dependency only for the already integrated torus exclusion. Therefore a future
review can adjudicate `NTLC-01` through `NTLC-08` independently of that
external source.

## 5. Source-risk register

- The finite coefficient extension is formal-local; algebraization is not
  inferred.
- Trace proves exactness on the normalized target function field, not automatic
  descent of the primitive to a singular coordinate ring.
- The conductor class is finite but is not automatically a contradiction.
- Formal models do not establish polynomial or Keller realization.
- Passing symbolic validators checks identities, not the global geometry or the
  planar Jacobian conjecture.
