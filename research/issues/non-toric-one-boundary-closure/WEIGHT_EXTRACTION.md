# Weight extraction and the exact support obstruction

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary label: `NTLC-07`

## 1. The valuation candidate

Assume both source coordinates have poles

```text
v_E(x)=-m,  v_E(y)=-n,
```

and put `d=gcd(m,n)`. The natural primitive positive candidate is

```text
w_E=(p,q)=(m/d,n/d).                               (1.1)
```

For a polynomial `G=sum c_ij x^i y^j`, its displayed weighted degree is

```text
d_G=max{p i+q j: c_ij!=0}.                         (1.2)
```

If this weight were known to satisfy

```text
kappa_w=d_P+d_Q-p-q<=4,
```

the independently reviewed fixed-weight theorem would make the Keller pair an
automorphism. No such inequality follows from the local data proved here.

If one pole order is zero, the valuation vector is not a positive weight. A
positive perturbation can be chosen, but neither its direction nor its defect
is canonical from the one-boundary data.

## 2. Why regular target functions do not bound support

The valuation of a polynomial is not the negative of its largest displayed
weight when leading monomials cancel. The common-power relation makes this
failure explicit. With

```text
m=d m0,  n=d n0,
a=alpha h^m0,  b=beta h^n0,
```

choose `lambda in C*` so that the leading terms cancel in

```text
T=y^m0-lambda x^n0.                                (2.1)
```

The two monomials of `T` have the same `w_E`-degree, while `v_E(T)` is strictly
larger than their common monomial valuation. Consequently `T^N` has arbitrarily
large displayed `w_E`-degree but is invisible to the first leading valuation
equation.

This is not presented as a Keller-preserving mutation. It proves the narrower
logical point required here: the equation

```text
n a' b-m a b'=0
```

and the finite amount of pole/conductor data preceding it do not control all
monomials of `P` and `Q`. A bounded-defect theorem needs the full global Keller
staircase or another support theorem.

## 3. Other proposed weights

The same defect appears for the other natural constructions.

| Proposed source | Candidate | Uncontrolled input |
|---|---|---|
| pole vector | primitive `(m,n)` | cancellations among all top pole layers |
| value semigroup | primitive extremal generator | no bound on which semigroup values occur in `P,Q` |
| Newton edge | inward primitive normal | no proof one boundary supplies a unique global Newton edge |
| branch multiplicity | multiplicity/degree pair | target branch multiplicity does not bound source support |
| conductor | gap or conductor exponents | conductor controls finite jets, not polynomial degrees |
| ramification | `(e,1)` or variants | `e` controls the normal parameter, not monomial support |

None yields a proved formula for both `d_P` and `d_Q`.

## 4. No defect bound from the recursive system

The normalized recursion constrains coefficient differentials in the completed
boundary field. It does not identify the Rees layers of the global polynomials.
The formal models in `FORMAL_MODELS.md` exist for arbitrary ramification index
`e` and pole order `m`; they show that the local symplectic and exactness
equations alone contain no numerical mechanism bounding those integers.

Those models are not polynomial Keller pairs. Therefore the packet does not
claim that actual Keller boundary types are unbounded. It identifies the exact
missing global input:

```text
formal Laurent/conductor solution
 + polynomial realization of P,Q,H
 + control of every Newton support layer
 => bounded kappa_w or contradiction.              (4.1)
```

## 5. Defect-four and defect-five interfaces

The only licensed fixed-weight terminal implication is

```text
primitive positive w and kappa_w<=4 => automorphism.
```

The defect-five packet on the pinned base is mutable `candidate_proved`; issue
#38 remains the independent-review successor. Accordingly:

- a future proof of `kappa_w<=4` may consume the reviewed theorem directly;
- a future proof of `kappa_w=5` is conditional on independent acceptance of
  issue #38 or an independent rederivation of every consumed step;
- this packet neither invokes defect five nor claims a strict filtration
  descent.

## 6. Exact disposition

`NTLC-07` is a negative extraction result, not a counterexample to a possible
qualifying-weight theorem:

```text
one boundary + the present Laurent/conductor equations
not=> any computed bound on kappa_w.                (6.1)
```

The obstruction is global Newton-support control. Producing that control is the
smallest filtered-equivariance handoff left by this packet.
