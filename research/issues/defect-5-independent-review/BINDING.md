# Exact Review Binding

## 1. Repository and revisions

- Repository: `snissn/planar-jacobian`
- Review issue: `#38`
- Review-owned path: `research/issues/defect-5-independent-review/`
- Latest live `main` resolved before construction:
  `652a5e252626fa5816445651245e8a8946cee53e`
- Scientific candidate commit:
  `2eeb36d232366d124b5a66774b29769ec1eba43d`
- Candidate tree: `c2b111ecf070eac1f59c7bb505e82820563ef3cd`
- Candidate base: `99c90e393cde7f15e34aaae3726c4d4ab305e0fb`
- Candidate inventory SHA-256:
  `333614389c339f4a3383856de2dfc5b977dc5dd6a6520f176b25c7116d861d12`

The candidate commit is not an ancestor of current `main`; it is a scientific
construction commit on an issue branch based at the stated candidate base. The
human scientific documents were transported to current `main` without byte
changes. Review is bound to the scientific candidate, not to the later
integration merge as a substitute.

## 2. Reviewed scientific blobs

| Candidate path under `research/issues/defect-5-rees/` | Candidate blob | Blob on live `main` | Binding result |
|---|---|---|---|
| `README.md` | `20e5f1e5c2c0a06f044e31b2abf27d9f499506b2` | same | exact |
| `FOUNDATIONS.md` | `7ee1ae5f7fff3b34a73fee5819d35c91c531c026` | same | exact |
| `TRANSFORMATIONS.md` | `4869da7f6d9a68e84d0cbe69fa621d20dcfa4b65` | same | exact |
| `DERIVATION.md` | `97eeac0375ead289b0c87646e34b0e2b99411988` | same | exact |
| `CASE_TABLE.md` | `e21969832bb6c8214e772f214fd352b0e786686d` | same | exact |
| `COUNTERMODEL_SEARCH.md` | `d7f8b56ce0ac9a50b0f283a861cb7d78e2adcba3` | same | exact |
| `VALIDATION.md` | `e7770db79053ff2835d59550d1602eec9558d8eb` | same | exact |
| `validate_defect5.py` | `e702b0114642c20b71111b702ef883d6473e84d5` | `166574d3585bed6df23ed12763b823a4b83a935d` | syntax-only correction |

The candidate validator blob contains the syntactic typo `for equations`; live
`main` changes only that token sequence to `for eq in equations`. This correction
makes the candidate checker executable but is not accepted as theorem authority.
The human mathematical blobs are unchanged.

## 3. Later review and transport artifacts

The following are later than the pinned scientific candidate and are not treated
as candidate-proof authority:

- `research/issues/defect-5-rees/REVIEW.md`, blob
  `1d046b6edb27beff53e21b82e18302858c87fc30`, records a
  `local-adversarial-review` by the constructing agent;
- `research/issues/defect-5-rees/review_validate_defect5_adversarial.py`, blob
  `f7028320374a5284a0edb8834e01adc082806dd8`, is supporting regression code;
- `research/issues/defect-5-rees/HANDOFF.md`, blob
  `0e8ca9c1c76339d56929e7977d88e9c2dae359f9`, is transport and successor prose;
- `research/issues/defect-5-rees/INTEGRATION.json`, blob
  `cf9e07676bbf9009f2f3c554e80b37ca7dd1bfff`, is integration metadata;
- shared ledgers, proof graph, queue, leaf packet, track, generated views, root
  `README`, and `STATUS` were synchronized on main after construction.

Those later artifacts were read for scope and provenance. Their conclusions were
not assumed in the reconstruction.

## 4. Dependency binding

The only prior theorem consumed after strict descent is the fixed-weight
defect-at-most-four theorem:

- reviewed candidate: `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`;
- independent-review integration revision:
  `7dada3a5d0c6c0bf0f40208b30215c495e17ee28`;
- disposition: `ACCEPT`;
- canonical scope: `CLM-060`, `reviewed_scoped`;
- exact implication: for a primitive positive weight, `kappa_w<=4` implies that
  the planar Keller pair is a polynomial automorphism.

No external literature theorem is load-bearing in the defect-five reconstruction.

## 5. Immutability boundary

This review adds only files under
`research/issues/defect-5-independent-review/`. It does not edit:

- any candidate proof or candidate checker;
- claim ledgers or proof graphs;
- work queues or issue indexes;
- leaf packets or tracks;
- generated views;
- root `README.md` or `STATUS.md`;
- governance or the permanent Actions workflow.
