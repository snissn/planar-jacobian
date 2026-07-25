# Primary-Source Literature Audit

```text
authority: MUTABLE_NONAUTHORITATIVE
source_policy: primary sources for every load-bearing imported theorem
local_claims: R3BC-01, R3BC-07
```

## 1. Load-bearing source: Orevkov's degree-three theorem

### Bibliographic record

S. Yu. Orevkov,
“On three-sheeted polynomial mappings of `C^2`,”
*Mathematics of the USSR-Izvestiya* **29**:3 (1987), 587–596.

- DOI: <https://doi.org/10.1070/IM1987v029n03ABEH000984>
- Primary Math-Net record: <https://www.mathnet.ru/eng/im1571>
- Original Russian publication: *Izv. Akad. Nauk SSSR Ser. Mat.* **50**:6
  (1986), 1231–1240.

### Exact statement consumed

The primary publisher record states:

> The Jacobian of a 3-sheeted polynomial mapping `C^2 -> C^2` cannot be a
> constant.

No stronger statement is imported. In particular, this packet does not cite
Orevkov for arbitrary prime degree, for maps in higher dimensions, or for a
classification of nonproperness curves.

### Hypothesis map

| Orevkov hypothesis | Packet verification |
|---|---|
| polynomial map `C2 -> C2` | `P,Q in C[x,y]` |
| generically three-sheeted | `[C(x,y):C(P,Q)]=3`; finite-étale localization proves three reduced generic preimages |
| Jacobian constant | Keller assumption `J(P,Q) in C*` |

The field-degree-to-sheet bridge is proved directly in `FOUNDATIONS.md`; it is
not delegated to a secondary source.

### Audit limitation

The tool environment exposed the primary bibliographic page and exact abstract
statement, and identified both the English and Russian full-text PDFs. The
English PDF bytes were not machine-readable through the available web parser,
so this packet does not claim a line-by-line reconstruction of Orevkov's proof.
The theorem is therefore bound at `literature_bound` scope, not promoted as a
new internally proved theorem. An independent integrator may strengthen the
audit by obtaining the PDF and checking the proof text, but the exact published
statement already matches the application without a hypothesis gap visible in
the primary record.

## 2. Why the theorem is sufficient for this issue

The issue's rank-three normalization rank is the function-field degree. A
dominant generically finite polynomial map of degree three is finite over a
dense target open; the Keller condition makes that restriction étale. Hence
“rank three” and “three-sheeted” agree at the exact generic scope used by
Orevkov.

The theorem bypasses, rather than solves constructively, the fixed-section
binary-cubic equation. This distinction is recorded throughout the packet.

## 3. Rejected shortcut: a 2024 all-prime-degree preprint

### Source examined

Vered Moskowicz,
“There are no Keller maps having prime degree field extensions,”
arXiv:2407.13795v1 (16 July 2024):
<https://arxiv.org/abs/2407.13795>.

The preprint claims that no planar Keller map has prime field degree. Its first
case relies on the assertion that a MathOverflow answer proves the following
classification:

```text
if every nonconstant monomial x^i y^j is primitive over R,
then [C(x,y):R]=2.
```

### Primary MathOverflow source

The cited answer is Laurent Moret-Bailly's response to
“A subfield `R subset C(x,y)` with many generators `w`”:
<https://mathoverflow.net/questions/472877/a-subfield-r-subseteq-mathbbcx-y-with-many-generators-w-rw-math>.

The answer begins by **choosing** a quadratic extension

```text
L=R(s),
s^2=u,
```

and then constructs coordinates `x=s+v`, `y=s+2v` for which every nonconstant
monomial is primitive. It supplies a quadratic example; it does not prove that
every extension with the rare property has degree two. The subsequent comments
on the page explicitly reveal this mismatch between example and classification.

### Exact cubic countermodel to the classification

The model

```text
L=C(s,v),
R=C(s^3,v),
x=s+v,
y=s+2v
```

has degree three and the same rare property. The proof is in
`COUNTERMODEL_LADDER.md`; exact bounded and finite-field falsification controls
are in `verify_prime_degree_audit.py`.

Therefore the classification used in the preprint's first case is false, and
the claimed all-prime-degree theorem is not imported here.

### Scope of this criticism

This audit identifies a specific unsupported implication in version 1 of the
preprint. It does not adjudicate every argument in the paper, every later
revision, or the separate `xy in k(p,q)` case. None of those claims is needed
because Orevkov directly covers degree three.

## 4. Non-load-bearing context

The predecessor packet already source-binds its finite-flatness and `R1/S2`
inputs. This successor does not add a new external use of those theorems. The
binary-cubic determinant identities, boundary special-fiber classification,
affine-family formula, differential lemmas, and rare-property cubic model are
proved directly and symbolically checked.

No secondary survey, database summary, or recent broad claim is used as a
terminal theorem.

## 5. Source disposition

| Source | Disposition | Reason |
|---|---|---|
| Orevkov 1986/1987 primary article | `BOUND_AT_EXACT_STATEMENT` | exact theorem matches degree-three Keller application |
| Moskowicz arXiv:2407.13795v1 | `REJECT_AS_LOAD_BEARING` | first case misuses an example as a classification; cubic countermodel supplied |
| MathOverflow answer | `AUDITED_AS_EXAMPLE_ONLY` | correctly constructs a quadratic rare-property model; does not prove uniqueness of degree |

The rank-three conclusion depends only on the first row.
