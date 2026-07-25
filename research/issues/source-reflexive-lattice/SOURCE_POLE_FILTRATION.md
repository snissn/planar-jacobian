# Source Pole Filtration

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-001`, `SRL-006`, `SRL-007`

## 1. Boundary audit

Let `j:U->Y` be the open immersion with ring map `O->A`.  Write

\[
Z=Y\setminus U.
\]

No purity assumption on `Z` is consumed.  Let

\[
D_{\mathrm{red}}=E_1+\cdots+E_r
\]

be the sum of its codimension-one irreducible components.  A possible
codimension-two remainder does not affect rational functions: on a normal
surface, regularity is detected at height one.

If `Z` has no divisorial component, Hartogs extension gives
`Gamma(U,O_U)=Gamma(Y,O_Y)=O`.  Since both schemes are affine and the ring map
then identifies their coordinate rings, the open immersion is an isomorphism.
Thus every proper affine source open has a nonempty divisorial part, although
this packet does not assert that the whole complement is pure.

## 2. Coherent multi-index stages

For `m=(m_1,...,m_r) in N^r`, define

\[
M_{\mathbf m}
 =\Gamma\left(Y,
   O_Y\left(\sum_i m_iE_i\right)\right)
 \subset L.
\]

The sheaf is the rank-one reflexive divisorial sheaf determined by the
valuation inequalities

\[
w_{E_i}(f)\ge-m_i,
\]

and nonnegative valuation at every other height-one point of `Y`.

Because `Y` is Noetherian and normal, every such sheaf is coherent.  Since
`Y` is affine and finite over `Spec(B)`, `M_m` is a finite `O`-module and a
finite `B`-module.  Under the finite-normalization surface hypotheses, `O` is finite flat over
the regular surface `B`.  A rank-one reflexive module on the normal surface
`Y` has depth two at closed points; a parameter sequence from `B` remains a
parameter sequence upstairs and is regular on the module.  It is therefore
maximal Cohen--Macaulay over `B`, hence `B`-reflexive and locally free.

It is full:

\[
M_{\mathbf m}\otimes_BK=L.
\]

It is generally not an algebra when any `m_i>0`, because products double the
allowed pole orders.

## 3. Exact union

Normality gives

\[
\boxed{
A=\Gamma(U,O_U)
 =\bigcup_{\mathbf m\in\mathbf N^r}M_{\mathbf m}.}
\]

Indeed, a rational function regular on `U` has no negative valuation at any
height-one point of `U`; its finitely many negative valuations can occur only
along the `E_i`, and one multi-index bounds them.  Conversely every section
of a divisorial pole sheaf is regular on `U`.

Since the number of components is finite, the diagonal filtration also works:

\[
A=\bigcup_{m\ge0}
\Gamma(Y,O_Y(mD_{\mathrm{red}})).
\]

This is a directed union of finite modules.  It is not itself finite unless
some stage already equals `A`.

## 4. Uniform pole-shift vector

For a rational derivation `D` regular on `U` and a boundary component `E`,
define the pole increment

\[
\sigma_E(D)=
\max\left(0,
-\inf_{0\ne f\in L}
   \bigl(w_E(Df)-w_E(f)\bigr)
\right).
\]

At the generic DVR this is finite.  With
`boldsymbol sigma(D)=(sigma_{E_i}(D))`, valuation arithmetic gives

\[
D(M_{\mathbf m})
 \subseteq M_{\mathbf m+\boldsymbol\sigma(D)}.
\]

The relevant local values are:

| Local geometry | Normal form | Pole increment |
|---|---|---:|
| ramified, transverse | `h=s^e`, `D(h)` a unit | `sigma_E(D)=e` |
| ramified, logarithmic | `D(h) in (h)` | `sigma_E(D)=0` |
| unramified, transverse to omitted `E` | `D(s)` a unit | `sigma_E(D)=1` |
| unramified, tangent | `D(s) in (s)` | `sigma_E(D)=0` |

For example, in `h=s^e`,

\[
D(s^{-m})=-\frac m e D(h)\,s^{-m-e},
\]

which increases the pole order by exactly `e` when `m>0`.

## 5. Repeated growth and commutativity

For nonnegative `a,b`, commutativity yields the order-independent bound

\[
D_P^aD_Q^b(M_{\mathbf m})
 \subseteq
M_{\mathbf m+a\boldsymbol\sigma(D_P)
                 +b\boldsymbol\sigma(D_Q)}.
\]

This is linear growth, not boundedness.  Commutativity says that mixed
iterations have the same result in either order; it does not place them in a
single finite stage.

Noetherian stabilization is unavailable: the modules containing successive
iterates themselves increase, so the iterates do not form an ascending chain
inside one fixed finite Noetherian module.

## 6. Failure theorem for finite source-pole stages

### Theorem 6.1

Let `E` be a ramified boundary component.  No full finite `B`-module obtained
from a fixed divisorial pole bound, its reflexive hull, a finite intersection
of such bounds, or a fixed finite conductor/different shift is stable under
both canonical derivations.

**Reason.**  At the image divisor `h=0`, one canonical derivation is
transverse.  The local no-lattice theorem excludes every valuation-bounded
full finite module, independently of its presentation.

### Theorem 6.2

Let `E` be unramified but omitted from `U`.  The normalization stage `M_0=O`
is locally stable at `E`, but every stage that admits a genuine pole along
`E` fails stability under at least one canonical derivation.

**Reason.**  At an unramified point the lifted Keller frame spans the tangent
space, so one member is transverse to `E`.  Differentiating a negative power
of a uniformizer raises its pole order by one.

Thus the source algebra is stable only after taking the unbounded union.  No
uniform `m` follows from the Keller identity.

## 7. The source conductor is zero in the proper-boundary case

Consider

\[
(O:A)=\{z\in L:zA\subset O\}.
\]

If a divisorial boundary component `E` is omitted, then the corresponding
prime `q_E` satisfies `q_EA=A`.  A valuation argument produces an element of
`A` with negative `E`-valuation, and its powers have arbitrarily negative
valuation.  No nonzero `z` can move all of them into `O`.  Hence

\[
(O:A)=0
\]

whenever `U` has a divisorial boundary.  If `U=Y`, the conductor is `O`.
This prevents source-conductor powers from furnishing nonzero finite stages
that capture all of `A`.

## 8. Exact obstruction isolated

The open immersion canonically supplies a **filtered ind-object** of finite
reflexive modules, not a finite stable module.  At ramification, every finite
stage is excluded by fractional residues.  Without ramification, any stage
that contains actual boundary poles still escapes.  Converting `j_*O_U`
into a finite pair-stable lattice therefore requires a new boundedness
principle that is absent from the pole filtration itself.
