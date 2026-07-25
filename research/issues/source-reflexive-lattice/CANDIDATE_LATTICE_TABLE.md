# Canonical Candidate Lattice Audit

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claim:** `SRL-009`

All rows are evaluated as `B`-modules inside `L`.  “Full” means generic fiber
`L`; “stable” means exact stability under both `D_P,D_Q`, not logarithmic
stability.

| Candidate | Finite over `B` | Reflexive / locally free | Full | Algebra | Local residues at `e>1` | Multiplier ring | Disposition |
|---|---:|---|---:|---:|---|---|---|
| `O` | yes | normal surface; `B`-locally free | yes | yes | `0,1/e,...,(e-1)/e` | `O` | stable iff no height-one ramification |
| `A=C[x,y]` | not known | unresolved as `B`-module | yes | yes | regular on `U`, unbounded at boundary | `A` | exactly stable but finiteness is the missing theorem |
| trace dual `Hom_B(O,B)` | yes | `B`-locally free; rank-one reflexive over `O` | yes | generally no | same classes, integer-shifted | `O` | duality does not remove ramification |
| inverse different | yes | rank-one reflexive fractional `O`-ideal | yes | generally no | same classes | `O` | stable only if the transverse obstruction is absent |
| relative canonical module | yes | rank-one reflexive; equals the dual in finite-flat Gorenstein base setting | yes | no in general | same classes | `O` | determinant/canonical language does not produce an order |
| finite-order conductor power | yes | reflexive hull locally free | yes | sometimes | integer shifts of `j/e` | contained in / returns a finite order | no transverse stable member at ramification |
| source conductor `(O:A)` | zero for proper divisorial boundary | — | no | ideal | — | — | cannot approximate `A`; equals `O` only when `U=Y` |
| `O_Y(sum m_iE_i)` | yes | rank-one reflexive over `O`, locally free over `B` | yes | no if a genuine pole is allowed | same fractional classes; pole shift grows | `O` | every ramified stage fails; positive unramified pole stages also escape |
| fractional colon `(O:h^mO)` | yes | `h^{-m}O`; reflexive | yes | no for `m>0` | integer-shifted | `O` | no improvement |
| colon taken inside `O` | yes | `O` | yes | yes | normalization spectrum | `O` | notation then gives only `O`, because `h^mO subset O` |
| finite intersection of divisorial modules | yes | reflexive after double dual | usually yes | generally no | same value-group classes | `O` after rank-one reflexive hull | excluded by local no-lattice theorem if stable is claimed |
| determinant line `det_B(M)` | yes | rank-one `B`-module | no: lies in `wedge^n_K L`, not `L` | no | sum `(e-1)/2`, which may be integral | not applicable | loses individual characters; cannot be an order |
| multiplier ring of a finite full module | yes | reflexive closure locally free | yes | yes | inherits stability obstruction | itself | converts module stability into the predecessor stable-order route |
| differential saturation of a finite stage | no fixed finite bound | ind-object only | yes generically | after infinite closure | pole order tends to infinity | typically nonfinite | forbidden infinite union |

## Local matrices in the tame model

For

\[
R\subset S=R[s]/(s^e-t),
\]

the normalization basis `1,s,...,s^(e-1)` has transverse connection matrix

\[
\frac1t\operatorname{diag}
\left(0,\frac1e,\ldots,\frac{e-1}{e}\right).
\]

Multiplication by `t^N`, a conductor power, or a different/canonical factor
adds integers to the diagonal entries.  The classes modulo `Z` are unchanged.

For the trace dual,

\[
S^\vee=(e s^{e-1})^{-1}S,
\]

one may use basis `(1/e)s^{j+1-e}`; the residues are

\[
\frac{j+1-e}{e},\qquad j=0,\ldots,e-1,
\]

which is the same multiset modulo `Z`.

## Exact classification lesson

Every canonical rank-one coherent candidate is finite because `Y` is finite
over the affine base, and reflexive because it is divisorial on a normal
surface.  Those good coherence properties do not imply exact differential
stability.  Stability at a transverse ramified valuation would already force
the fractional spectrum to vanish, hence `e=1`.
