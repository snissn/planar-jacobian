# Canonical Candidate Lattice Audit

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claim:** `SRL-007`  
> **Local test model:** `R=C[t,u]_(t)`, `S=R[s]/(s^e-t)`, `D_t(t)=1`, `D_u(t)=0`.

For a branch of index `e`, the common fractional spectrum means

```text
Sigma_e = {0,1/e,...,(e-1)/e} mod Z.
```

| Candidate | Finite over `B` | Reflexive / locally free | Full | Algebra | Local derivation / spectrum | Exact disposition |
|---|---:|---:|---:|---:|---|---|
| Normalization `O` | yes | reflexive; locally free under surface hypotheses | yes | yes | `D_t(s^j)=j/(et)s^j`; spectrum `Sigma_e` | stable iff no height-one ramification |
| Source algebra `A=C[x,y]` | finiteness unknown | unresolved as `B`-module | yes | yes | both canonical derivations preserve it | using it as finite order assumes the missing finiteness |
| Inverse different `D_(O/B)^(-1)` | yes | reflexive fractional ideal | yes | generally no | Kummer exponent `1-e`; same `Sigma_e` | fails at ramification; equals `O` in the etale case |
| Trace dual `Hom_B(O,B)` | yes | reflexive; locally free under maintained hypotheses | yes | generally no | same as inverse different when finite flat | duality does not remove residues or supply multiplication |
| Relative canonical module | yes | reflexive; invertible in Gorenstein locus | yes | no canonical algebra | same divisorial shift as trace dual | not an order; stable only after unramifiedness |
| Finite-suborder conductor power `R+t^NS` | yes | free in DVR model | yes | yes | residues `N+j/e`; fractional part `Sigma_e` | genuine order, never exact-stable for `e>1` |
| Source conductor `(O:A)` | zero if divisorial boundary exists | not full | no | ideal | powers of a source pole force every nonzero conductor element to fail | cannot supply a lattice |
| Divisorial pole module `O_Y(sum m_iE_i)` | yes | coherent reflexive; locally free over regular `B` | yes | only at zero pole vector | transverse iteration drops valuation by `e` each time | every pole-bearing stage fails, even for `e=1` |
| Uniform stage `O_Y(mD_red)` | yes | same | yes | no for `m>0` | `D(M_m)` requires `M_(m+e)` locally at a transverse branch | no uniform stable `m` |
| Colon `(O:h^mO)` | yes; equals `h^(-m)O` | reflexive | yes | no for `m>0` | residues `-m+j/e`; same `Sigma_e` | integer shift only; not stable |
| Reflexive hull of `(O:h^mO)` | same module in normal setting | reflexive | yes | no | unchanged | no repair |
| Finite intersection of divisorial modules | yes | reflexive after double dual | if declared full | rarely | local intersection is another bounded lattice | ramified no-lattice theorem; pole-bearing source escape otherwise |
| Determinant `det_B(O)` | yes, rank-one `B`-line | invertible over `B` | not a lattice in `L` canonically | no | connection trace only; lives in `wedge^n_K L` | cannot be used as an order without extra noncanonical identification |
| Multiplier ring of a full reflexive lattice | yes | reflexive, hence locally free over regular surface | yes | yes | stable whenever the lattice is stable | converts any successful module to predecessor stable order |
| Multiplier ring of a source-pole module | yes | equals `O` | yes | yes | inherits normalization spectrum `Sigma_e` | returns `O`, not a new order |
| Differential saturation of any pole stage | not finite in boundary model | no fixed finite ambient module | yes as union | closure enlarges union | valuations tend to `-infinity` | forbidden infinite union; no Noetherian stabilization |
| Logarithmic/Deligne lattice | yes locally | locally free | yes | not generally | stable under `tD_t`; residue `Sigma_e` | logarithmic stability is strictly weaker than exact translation stability |

## 1. Explicit local matrices

### Normalization

In the basis `1,s,...,s^(e-1)`,

```text
A_t = diag(0,1/(et),..., (e-1)/(et)),
A_u = 0.
```

### Fractional ideal `s^mS`

In the basis `s^m,...,s^(m+e-1)`,

```text
A_t = diag((m+j)/(et))_(0<=j<e),
A_u = 0.
```

Modulo integers the eigenvalue multiset is always `Sigma_e`.

### Colon module

Since

```text
(S:t^NS)=t^(-N)S=s^(-eN)S,
```

its representatives are

```text
-N+j/e.
```

### Inverse different and trace dual

For `t=s^e`,

```text
Different = (e s^(e-1)),
S^vee = (e s^(e-1))^(-1)S.
```

Ignoring the unit `e`, this is `s^(1-e)S`; representatives are

```text
(1-e+j)/e,
```

which permute `Sigma_e` modulo `Z`.

### Conductor order

For

```text
C_N=R+t^NS,
```

use the basis

```text
1,t^Ns,...,t^Ns^(e-1).
```

The nontrivial diagonal entries are

```text
(N+j/e)/t.
```

The fractional classes remain nonzero when `e>1`.

## 2. Multiplicative closure audit

- `O`, `A`, conductor orders, and multiplier rings are algebras.
- A nonzero positive pole module is not an algebra because squaring doubles the allowed pole.
- The trace dual, inverse different, and canonical module are fractional ideals, not generally rings.
- Finite intersections can be rings only after a separate multiplication proof.
- Determinant lines have no natural multiplication in `L`.

## 3. Stability circularity audit

Every canonical candidate falls into one of four exact classes:

1. `O`: finite order, but stability is equivalent to no height-one ramification;
2. pole-bearing modules: finite and reflexive, but transverse iterations escape;
3. dual/determinant constructions: finite, but lack multiplication and retain the same residues;
4. `A` or differential saturation: stable, but not known finite and in boundary cases provably an unbounded union.

Thus none constructs the required order without already supplying the missing unramifiedness or finiteness conclusion.
