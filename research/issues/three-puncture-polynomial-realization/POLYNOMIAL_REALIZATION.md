# Global polynomial-realization theorem

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `TPPR-02`, `TPPR-03`, `TPPR-04`, `TPPR-05`

## Theorem `TPPR-05`

Let

```text
F=(P,Q):C^2->C^2
```

be a dominant quasi-finite polynomial map. In the finite-normalization
factorization of `F`, no omitted source-boundary divisor can map onto

```text
C: P Q^2(Q-1)^2+(Q-1)^2+Q^2=0.                        (0.1)
```

Consequently no polynomial Keller map has the displayed normalized boundary
branch.

## Proof

### Step 1: make the branch a nonproperness component

Let `X->Y->C^2` be the finite-normalization factorization and `D=Y-X`.
`SOURCE_COMPACTIFICATION.md` proves

```text
S_F=pi(D).                                              (1.1)
```

If a divisor `E subset D` maps onto `C`, finite dimension preservation and
(1.1) make `C` an irreducible component of `S_F`.

### Step 2: invoke the exact primary-source theorem

Jelonek--Lasoń, *Quantitative properties of the non-properness set of a
polynomial map*, manuscripta mathematica 156 (2018), Theorem 3.2, states:

```text
if f:C^n->C^m is a generically finite polynomial map of degree d,
then S_f has degree of C-uniruledness at most d-1.       (2.1)
```

Definitions 2.1 and 2.3 make this componentwise and polynomial: through every
point of each irreducible component passes the image of a nonconstant
polynomial map `C->component`.

All hypotheses hold for `F`: the source and target are affine spaces over
`C`, the coordinate functions are polynomials, and quasi-finiteness implies
generic finiteness. For a Keller pair, constant nonzero Jacobian makes the map
étale, hence quasi-finite; its nonempty open image in the irreducible target
also supplies dominance.

### Step 3: isolate the displayed component

Choose a point `c in C` outside the finite union of intersections with all
other components of `S_F`. By (2.1), a nonconstant polynomially parametric
curve in `S_F` passes through `c`. Its irreducible closure lies in one
irreducible component of `S_F`; the choice of `c` forces that component to be
`C`. Thus there is a nonconstant morphism

```text
A1->C.                                                  (3.1)
```

### Step 4: contradict the exact unit calculation

`BRANCH_GEOMETRY.md` proves every morphism `A1->C` is constant because `Q` and
`Q-1` are units on `C`. This contradicts (3.1). `square`

## Exact low-complexity realization search

The polynomial-curve search is exhaustive rather than merely bounded. If

```text
p(t),q(t) in C[t],
g(p(t),q(t))=0,
```

then the two Bézout identities pull back to polynomial inverses of both `q`
and `q-1`. Hence `q in C*`, `q!=1`, and the branch equation fixes `p`.
No polynomial ansatz of any degree survives.

The checker also runs explicit degree campaigns and denominator-allowed
controls. The controls show the hypotheses are sharp:

- rational `P` and `H` can realize the Jacobian and primitive identities;
- a non-generically-finite polynomial map falls outside Theorem 3.2;
- filling two punctures changes the curve to `A1`, which has polynomial
  parametrizations.

## Scope

The theorem excludes exactly (0.1) for the quasi-finite class, even with
multiple source-boundary components and arbitrary finite cover data. It does
not cover a merely generically finite polynomial map with a
positive-dimensional exceptional fiber, does not say that every
Liouville-exact branch lacks polynomial parametrizations, and proves no
general one-boundary theorem.
