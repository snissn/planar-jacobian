# Handoff

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Role: `integration-maintainer`
> Construction role: `research-worker`
> Task issue: issue #5  
> Exact-symplectic coordination: issue #13  
> Owned path: `research/issues/non-toric-one-boundary-closure/`  
> Integration base: `72e09753d1a1523ff22b44093cc65e21384613fc`
> Candidate reviewed locally: `02321cf2a78989f8d3cc57872c1e76961d3cd0d1`

## 1. Exact result banked

The packet proves at mutable candidate scope:

```text
If a generically ramified boundary divisor has at least one source-coordinate
pole, then P dQ=dR in the function field of the normalized reduced target
branch.
```

The proof consumes the full issue #13 exact-symplectic data, not merely the
residue statement:

```text
dP wedge dQ=dx wedge dy,
P dQ+y dx=dH,
```

normalizes a pole coordinate to `x=s^(-m)`, solves every pre-ramification
coefficient of `y`, kills the unique logarithmic resonance, and traces the
order-zero tangential primitive down to the target branch.

Consequently every **Liouville-nonexact non-toric** branch is excluded. The
smooth branch `P(P-1)Q-1=0` is an explicit example, because normalized `P dQ`
has residues `+1` and `-1`.

## 2. Formal survivor

The smooth non-toric branch

```text
P Q^2(Q-1)^2+(Q-1)^2+Q^2=0
```

has normalization `Q=z`,

```text
P=d(1/z+1/(z-1))/dz,
P dQ=d(1/z+1/(z-1)).
```

It survives the order-zero obstruction. Arbitrary-index formal neighborhoods
and a field-generating rational Jacobian-one control survive all displayed
Laurent equations. Their exact failure is polynomial realization: the target
retains denominators such as `x^(-e)`. They are not actual Keller pairs.

## 3. Smallest remaining bridge: `NTLC-09`

The pole-supported non-toric class is reduced to the following exact sequence of
questions:

1. normalized Liouville exactness `P dQ=dR`;
2. the finite conductor/gluing class of `R` when target descent is required;
3. vanishing of every higher rational differential class `beta_r` in
   `d c_(m+r)=-beta_r/m`;
4. algebraization of the all-orders formal solution on the finite normalization;
5. realization of `P,Q,H` as polynomials in the actual source coordinates;
6. control of all Newton/Rees support layers sufficient to compute a primitive
   positive weight and its defect.

The recommended next calculation is the exact three-puncture survivor above:
prove that no polynomial Keller realization can have that normalized branch, or
produce the first higher `beta_r`/conductor obstruction forced by polynomial
realization. This is smaller than searching for another arbitrary logarithmic
field.

## 4. Weight handoff

The pole vector gives a candidate positive weight only when both coordinates
have poles. The packet proves no bound on

```text
kappa_w=d_P+d_Q-p-q,
```

because common-power cancellation does not control every polynomial monomial.
A future `kappa_w<=4` result may consume the independently reviewed defect-four
theorem. A future `kappa_w=5` result remains conditional: issue #38 was open on
the pinned base, and this packet does not rederive defect five.

## 5. Serialized shared deltas

The integration maintainer allocated the complete issue-local dependency chain
as `CLM-086` through `CLM-094` and serialized these shared changes:

- preserve the formal normal form, divisor-safe leading theorem, all-order
  recursion, Liouville exactness, conductor class, subclass exclusion,
  negative weight extraction, and realization controls;
- retain `CLM-094` as the open polynomial-algebraization and global-support
  bridge;
- advance L03 to `OPEN-ONE-BOUNDARY-POLYNOMIALIZATION` and update the issue #13
  exact-symplectic successor pointer;
- leave the general one-boundary program open;
- make no terminal edge to a qualifying-weight theorem or `JC_2`.

The issue-local statements and final canonical mappings are recorded in
`INTEGRATION.json`.

## 6. Review and validation

Review mode: `local-adversarial-review`.

```text
candidate_revision: 02321cf2a78989f8d3cc57872c1e76961d3cd0d1
disposition: ACCEPT_FOR_CANDIDATE_INTEGRATION
promotion_disposition: BLOCK_PROMOTION
```

Run from the repository root:

```bash
python3 -m compileall -q scripts research/issues
python3 research/issues/non-toric-one-boundary-closure/validate_laurent_conductor.py --max-e 6 --max-m 6 --order 10 --max-power 10 --json
python3 research/issues/non-toric-one-boundary-closure/verify_all.py
python3 scripts/validate_issue5_principal_parts.py
python3 research/issues/one-boundary-logarithmic-field/verify_all.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
```

Mainline completion is recorded only by a remote completion receipt after the
pull request reports `merged=true`, live `main` contains the intended revision,
critical files are refetched, and exact-main validation passes.
