# Issue #3 Mainline Integration Validation

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Validation scope:** repository transport and exact symbolic identities only  
> **Scientific promotion:** none

## Branch comparison

Before this record was added, the integration head was
`ed37087a1924ff17c33dfb71c1e3325afb5658d3`.

The GitHub adapter comparison against `main` returned:

```text
status: ahead
behind_by: 0
ahead_by: 8
merge_base: 7dada3a5d0c6c0bf0f40208b30215c495e17ee28
changed files: 18
```

The integration therefore excludes the unrelated history of the original
rich-baseline branch and is a direct descendant of current `main`.

## Blob-preserving transport

The eleven original issue-scoped files were inserted by their Git blob SHAs,
not reconstructed manually. Their source identities are recorded in
`PROVENANCE-MANIFEST.md`. `MAINLINE-SYNC.md`, the compact track, leaf packet,
ledger, program, status, and README are current-main reconciliation files.

## Exact symbolic recomputation

The calculations in `verify_index_models.py` were independently executed with
SymPy after transport. All assertions passed, including:

```text
smooth rational fixed-sheet model:
  Phi=-(u*x^3+x^2*y+v*y^3)
  Disc=-v*(4+27*u^2*v)
  Phi(1,lambda)=-(u+lambda+lambda^3*v)
  open-plane Jacobian=s*(3*u*s-2)

diagonal rank-three model:
  Phi=-(t*x^3+(t^2+1)*y^3)
  Disc=-27*t^2*(t^2+1)^2

rational corank-two model:
  Phi=-(u*x^3+v*y^3)

biquadratic model:
  index=-4*c^2*(u-c^2*v)
  Vandermonde=64*c^2*u*v*(u-c^2*v)
```

The associativity checks, characteristic polynomial, discriminant/index-square
identity, and Vandermonde identity all passed.

## Automated repository checks

The GitHub adapter returned no configured combined-status checks for the
pre-validation integration head. This is recorded as absence of configured
status checks, not as a green CI result.

## Scientific inference

These checks establish transport integrity and recompute the declared finite
algebra identities. They do not independently accept the local algebra proofs,
normality arguments, `R1/S2` theorem, or any claim about the planar Jacobian
conjecture.