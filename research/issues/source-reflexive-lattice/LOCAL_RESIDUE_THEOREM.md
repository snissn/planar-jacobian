# Local Residue Theorem and the Codimension-One Equivalence

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-002`, `SRL-003`, `SRL-004`

## 1. Lattices and hypotheses

Let `k` be a characteristic-zero field.  Let `B` be an excellent normal
Noetherian domain, let `K=Frac(B)`, let `L/K` be finite separable, and let `O`
be the integral closure of `B` in `L`, assumed finite over `B`.

A **full finite `B`-lattice in `L`** is a finite torsion-free `B`-submodule
`M subset L` such that

\[
M\otimes_B K=L.
\]

It need not be an `O`-module, reflexive, locally free, or multiplicatively
closed.  If `B` is a regular surface, the reflexive hull `M^{**}` is locally
free, but stability of `M^{**}` must be checked rather than assumed.

For `delta in Der_k(B)`, separability gives a unique extension `D` to `L`.
A reduced ramified base divisor `H` is **delta-logarithmic** when, at its
generic point with prime `p`,

\[
\delta(p)\subset p.
\]

Equivalently, for a local equation `t`, `delta(t) in tB_p`.  If this fails,
`delta(t)` is a unit of the DVR `B_p`; the derivation is transverse.

## 2. Sharp fixed-derivation theorem

### Theorem 2.1

Assume `B` is regular in codimension one and all height-one residue
characteristics are zero.  For a fixed `delta` and its lift `D`, the following
are equivalent:

1. there is a full finite `B`-lattice `M subset L` with `D(M) subset M`;
2. every reduced height-one branch divisor of `O/B` is `delta`-logarithmic;
3. `D(O) subset O`.

When these conditions hold, `O` itself is a finite full stable lattice.
Neither reflexivity nor local freeness is needed in condition 1.

### Proof: `1 => 2`

Let `p` be a ramified height-one base prime and `q` a valuation of `L` above
it.  Put `R=B_p`, choose a uniformizer `t`, and localize `M`.  If `delta` is
not logarithmic, then `delta(t)` is a unit.

Pass to a strict henselization.  It is an ind-etale faithfully flat base
change, the derivation extends uniquely, the finite separable algebra splits
into valuation factors, and a stable full lattice projects to a stable full
lattice in each factor.  In residue characteristic zero every ramified
factor is tame.  After an unramified extension and a change of uniformizer,
its totally ramified part has

\[
t=s^e,\qquad e>1.
\]

Writing `a=delta(t)`, the lifted derivation satisfies

\[
D(s)=\frac{a}{e s^{e-1}}=\frac{a}{e}t^{-1}s.
\]

Every full finite `R`-lattice is valuation bounded.  If
`t^N s` lies in it, then

\[
D^n(t^Ns)=
\left(\prod_{r=0}^{n-1}(N+1/e-r)\right)
 a^n t^{N-n}s+\text{terms of larger valuation}.
\]

No displayed factor vanishes in characteristic zero when `e>1`, so the
valuation tends to minus infinity.  This contradicts stability.  Hence a
stable full lattice forces `delta(t) in (t)` at every ramified divisor.

### Proof: `2 => 3`

At an unramified height-one point, formal etaleness uniquely extends the base
derivation and preserves the local normalization.

At a ramified point, strict-henselian tame coordinates have
`t=u s^e`, with `u` a unit.  Logarithmic tangency writes
`delta(t)=t b`.  Differentiating gives

\[
e\frac{D(s)}s=b-\frac{D(u)}u.
\]

The right side is regular, so `D(s) in sS`.  The unramified residue extension
is also preserved.  Thus `D(O_q) subset O_q` at every height-one point `q` of
`O`.

Normality gives the Krull intersection

\[
O=\bigcap_{\operatorname{ht}q=1}O_q\subset L.
\]

Therefore `D(O) subset O`.

### Proof: `3 => 1`

Take `M=O`.  Finiteness of the normalization makes it a full finite
`B`-lattice.  This completes the proof.

## 3. Canonical two-derivation theorem

Now specialize to

\[
B=\mathbf C[P,Q],\qquad L=\mathbf C(x,y),
\]

with the canonical lifts `D_P,D_Q`.

### Theorem 3.1

The following are equivalent:

1. some full finite `B`-lattice in `L` is stable under both `D_P,D_Q`;
2. some full coherent reflexive `B`-lattice is stable under both;
3. `O` is stable under both;
4. every height-one extension of DVRs in `O/B` is unramified (not merely
   numerically `e=1`).

If these conditions hold, `O` is finite locally free over `B`.  Purity of the
branch locus makes `Spec(O)->A^2_C` finite etale, and connectedness then
forces `[L:K]=1`.

### Proof

The implications `3=>2=>1` are immediate.  For `1=>4`, let `h(P,Q)` define a
reduced irreducible ramified base divisor.  In characteristic zero,
`h` cannot divide both `h_P` and `h_Q`: each nonzero partial has smaller
degree, and both cannot vanish unless `h` is constant.  Thus at least one of
`D_P,D_Q` is transverse to `(h)`.  Theorem 2.1 excludes a lattice stable under
that derivation.

For `4=>3`, every height-one localization of `O/B` is unramified, including
separability of its residue extension, so both base translations preserve every
height-one local normalization.  Intersecting the height-one local rings
proves global stability.

A finite normal surface over the regular surface `B` is Cohen--Macaulay; the
finite dominant equidimensional map is therefore flat, hence finite locally
free.  With no codimension-one branch, purity removes any codimension-two
branch locus.  The resulting connected finite etale cover of complex affine
two-space has one sheet.

## 4. Why one canonical derivation is insufficient

A single member of the frame can be tangent to a ramified divisor.  In the
model

\[
h=Q,\qquad h=s^e,
\]

`D_P(h)=0`, so `D_P` preserves the normalization, while
`D_Q(h)=1` and `D_Q` has the fractional-residue obstruction.  Therefore the
one-derivation statement must name either:

- a derivation known to be transverse to every ramified divisor; or
- the exact logarithmic-tangency condition of Theorem 2.1.

Requiring both canonical translations is the coordinate-free global way to
ensure that every base divisor has a transverse member.

## 5. Intrinsic fractional-residue spectrum

Let `R` be a characteristic-zero DVR with valuation `v`, uniformizer `t`, and
transverse derivation `delta`.  Let `w` be an extension valuation on `L` with
ramification index `e` and residue degree `f`.  Normalize the lift by

\[
\Theta=\frac{t}{\delta(t)}D.
\]

The operator `Theta` preserves the valuation filtration of the local
normalization.  On the associated graded piece of valuation `n`, after
strict henselization, it acts with scalar

\[
\frac ne.
\]

This yields the coordinate-independent multiset

\[
\operatorname{FRS}_w(L/K)
 =\left\{0,\frac1e,\ldots,\frac{e-1}{e}\right\}\pmod{\mathbf Z},
\]

with every class repeated `f` times before strict-henselian splitting.
Equivalently, it is the regular multiset of the value-group quotient

\[
\Gamma_w/\Gamma_v\cong (1/e)\mathbf Z/\mathbf Z.
\]

This definition is intrinsic: replacing `t`, the tame parameter, or a
logarithmic lattice changes residue representatives by integers but not their
classes.  Completion preserves `e`, `f`, and the spectrum.  Strict
henselization separates the residue-field factors and exposes `f` copies of
the same tame spectrum.

## 6. Exact role of characteristic zero

Characteristic zero is used for:

1. separability and uniqueness of derivation extension to `L`;
2. tameness of all height-one ramification;
3. invertibility of `e` in the Kummer calculation;
4. nonvanishing of every factor `N+j/e-r` under repeated differentiation;
5. separability of residue-field extensions.

In characteristic `p`, repeated-derivative coefficients can vanish and wild
or inseparable extensions are not governed by this theorem.  The
characteristic-zero result must not be inferred from a nonuniform mod-`p`
calculation.
