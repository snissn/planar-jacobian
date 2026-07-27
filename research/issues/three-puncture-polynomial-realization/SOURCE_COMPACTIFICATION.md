# Source compactification and the nonproperness component

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Label: `TPPR-02`

## 1. Finite-normalization factorization

Let

```text
X=Spec C[x,y]=A2,
T=Spec C[P,Q]=A2,
F=(P,Q):X->T
```

be a dominant, generically finite polynomial map. Put

```text
K=C(P,Q),
L=C(x,y),
O=integral closure of C[P,Q] in L,
Y=Spec O.
```

When `F` is Keller, its constant nonzero Jacobian makes it étale, hence
quasi-finite; equality of source and target dimensions also makes it dominant
and generically finite. Since `X` is normal, Zariski Main gives the canonical
factorization

```text
X --j--> Y --pi--> T,                                  (1.1)
```

where `j` is an open immersion and `pi` is finite. Set

```text
D=Y-j(X).
```

A normal projective completion `Ybar` may be obtained by taking a projective
completion of `Y` and normalizing. The closure of every divisorial component
`E` of `D` is a source divisor at infinity for the original `A2`. The finite
map `pi` already identifies its affine target image; no choice of projective
completion changes that image.

Equivalently, one may close the graph of `F` in `P2_source x P2_target`,
normalize it, and resolve indeterminacy. The divisors over the source line at
infinity that map into the affine target are precisely the divisorial pieces
recorded by `D`.

## 2. Equality with the nonproperness set

Use the primary-source definition

```text
S_F={a in T : no open neighborhood V of a makes
                 F^(-1)(V)->V finite}.                 (2.1)
```

### Lemma `TPPR-02`

```text
S_F=pi(D).                                              (2.2)
```

### Proof

The image `pi(D)` is closed because `pi` is finite.

If `a` is outside `pi(D)`, choose an open neighborhood `V` disjoint from
`pi(D)`. Then `pi^(-1)(V)` lies in `j(X)`, so

```text
F^(-1)(V)=pi^(-1)(V)->V
```

is finite. Hence `a` is outside `S_F`.

Conversely suppose `a` lies in `pi(D)` and that `F` is finite over some
nonempty open neighborhood `V` of `a`. The normal irreducible variety
`F^(-1)(V)` is finite over `V` and has function field `L`. Its coordinate ring
is therefore the integral closure of the coordinate ring of `V` in `L`.
Uniqueness of normalization identifies it with `pi^(-1)(V)`. This is impossible
because `D` meets `pi^(-1)(V)`. Thus `a` lies in `S_F`. `square`

The same proof can be phrased with “proper”: an affine proper morphism is
finite, and a proper quasi-finite morphism is finite.

## 3. The displayed branch is a component

Assume a divisor `E subset D` maps onto the displayed curve `C`. A finite
morphism preserves dimension and has closed image, so `pi(E)=C` is an
irreducible curve. By (2.2), `C subset S_F`.

Because `F` is generically finite, there is a nonempty open target set over
which it is finite; hence `S_F` is proper. Every irreducible component
containing the one-dimensional closed irreducible set `C` has dimension one
and therefore equals `C`. Thus `C` is an irreducible component of `S_F`.

Additional source-boundary divisors do not change this conclusion. Choose a
point of `C` outside its finite intersections with all other irreducible
components of `S_F`; a polynomial curve through that point supplied by the
source theorem must lie in `C`.

## 4. Exact scope

This argument identifies the requested actual source-boundary divisor and uses
only finite normalization, global polynomiality, and generic finiteness. It
does not assume:

- that `D` has one component;
- that `E` is smooth;
- a Puiseux pair or value-semigroup presentation;
- trivial source conductor;
- a monomial source valuation;
- a ramification index;
- or a positive Newton weight.
