# Transformation-Orbit Analysis

## 1. Exact family

For an integer `N>=2`, set

```text
sigma_N(x,y)=(x+y^N,y),
tau_N(u,v)=(u,v+u^N),
A_N=tau_N o sigma_N
   =(x+y^N, y+(x+y^N)^N).
```

Both factors are determinant-one triangular automorphisms, so `A_N` is an
actual polynomial automorphism with `J(A_N)=1`. The family tests whether an
orbit complexity has declared enough transformations to recognize a known
automorphism.

## 2. Affine-orbit theorem

### Theorem `QWD-AFFINE`

Let `C_aff` contain arbitrary compensated affine source and target
transformations, and let `C_SL` contain determinant-one linear source and target
transformations. Then

```text
mu_aff(A_N)=mu_SL(A_N)=N^2-1.                            (2.1)
```

### Proof

Translations do not affect a positive weighted top degree. After an arbitrary
affine source change, write the independent linear parts of the new source
coordinates as `M,L`. The transformed components have the exact top pattern

```text
P=M+L^N+(lower weighted terms),
Q=L+P^N+(lower weighted terms).                         (2.2)
```

Fix `w=(p,q)` and put

```text
epsilon=deg_w(M),
delta=deg_w(L),
D=max(epsilon,N delta).                                 (2.3)
```

Then `deg_w(P)=D`. If `epsilon=N delta`, the linear form `M` cannot cancel the
ordinary-degree-`N` form `L^N`. Also `D>=N delta>delta`, so the top term of `Q`
is `P^N` and

```text
deg_w(Q)=N D.                                           (2.4)
```

Apply an arbitrary invertible affine target matrix. A target component with a
nonzero `Q` coefficient has degree `ND`; its top term cannot cancel against a
multiple of `P`, whose degree is only `D`. If one row has zero `Q` coefficient,
the two component degrees are `D,ND`. If both rows have nonzero `Q`
coefficients, both degrees are `ND`. Hence every affine target change satisfies

```text
d_1+d_2 >=(N+1)D.                                      (2.5)
```

Order the coordinate weights as `r<=s`. If `L` contains the weight-`s`
variable, then `delta=s` and `D>=Ns`. Otherwise `L` is a multiple of the
weight-`r` variable, and independence forces `M` to contain the weight-`s`
variable, so

```text
D>=max(s,Nr).                                           (2.6)
```

The second alternative is the smaller possible bound. Combining (2.5)--(2.6),

```text
kappa_w >=(N+1)max(s,Nr)-r-s.                           (2.7)
```

If `s>=Nr`, then the right side is

```text
N s-r >=N(Nr)-r=(N^2-1)r>=N^2-1.
```

If `s<=Nr`, then it is at least

```text
(N+1)Nr-r-s >=(N+1)Nr-r-Nr=(N^2-1)r>=N^2-1.
```

Thus every affine representative and every primitive positive weight has defect
at least `N^2-1`.

The original pair with weight `(N,1)` has

```text
d_P=N,
d_Q=N^2,
kappa=N+N^2-N-1=N^2-1.
```

The identity source and target lie in both declared classes, proving (2.1).
`square`

### Corollary

For every `N>=3`, the affine and determinant-one-linear orbit minima are at
least eight. Therefore no universal bound of five can hold for either class,
even after restricting to actual polynomial Keller automorphisms.

## 3. One nonlinear target shear collapses the family

Apply

```text
beta_N(u,v)=(u,v-u^N).
```

Then

```text
beta_N o A_N=(x+y^N,y).
```

At `w=(N,1)`, the component degrees are `(N,1)`, so

```text
kappa_(N,1)(beta_N o A_N)=0.
```

The gap from `N^2-1` to zero is produced by one explicit determinant-one
polynomial target automorphism. It is neither asymptotic nor support-only.

## 4. Transformation-class comparison

| Class | Exact behavior on `A_N` | Consequence |
|---|---:|---|
| determinant-one linear | `N^2-1` | no universal bound five |
| compensated affine | `N^2-1` | translations and affine mixing do not help |
| triangular target | `0` | complete-top cancellation is essential |
| fixed-weight graded source only | does not remove `Q-P^N` | normalization is not target descent |
| tame source/target | `0` | contains the displayed target shear |
| full polynomial source/target | `0` | inverse target trivializes every automorphism |

This is why every occurrence of `mu` in the packet has a transformation-class
subscript.

## 5. Tame versus full

Jung's theorem over `C`, with van der Kulk's standard field-general structure,
states that every plane polynomial automorphism is a finite product of affine
and elementary triangular automorphisms. Thus

```text
C_tame=C_full
```

for the source and target groups used here. The theorem is consumed only for
this equality. It does not give a decreasing factorization for an unknown
Keller pair, a bound on the number or degree of elementary steps, or a
qualifying weight.

If `F` is an automorphism, the full target orbit contains `F^-1 o F=id`. Thus
`mu_full(F)=0`; this makes the full-orbit scalar a restatement of invertibility,
not a usable well-founded search parameter.

## 6. Exact binomial-chain theorem

Consider the class `B_N`:

```text
P=a x+b y^N,
Q=c y+sum_(k=0)^N q_k x^k y^(N(N-k)),
a b c q_N !=0.
```

### Theorem `QWD-BINOMIAL`

The equation `J(P,Q)=1` is equivalent to

```text
a c=1,                                                   (6.1)
a(N-k)q_k=b(k+1)q_(k+1),  0<=k<N.                       (6.2)
```

Consequently

```text
q_k=lambda binom(N,k) a^k b^(N-k),
lambda=q_N/a^N,
Q=c y+lambda P^N.                                        (6.3)
```

The determinant-one target shear

```text
(P,Q)->(P,Q-lambda P^N)=(a x+b y^N,c y)                 (6.4)
```

has defect zero at `w=(N,1)`.

### Proof

For the chain monomial indexed by `k`, the `P_x Q_y` contribution to the
coefficient of

```text
x^k y^(N(N-k)-1)
```

is

```text
N a(N-k)q_k.
```

The only matching term from `P_y Q_x` is produced by the next chain monomial
and equals

```text
N b(k+1)q_(k+1).
```

No other declared support has that exponent. The constant coefficient of the
Jacobian is `ac`. Hence the complete coefficient system is exactly
(6.1)--(6.2). Solving the recurrence from `q_N` gives (6.3), and the binomial
theorem gives the displayed form of `Q`. The shear (6.4) has determinant one.
Since `ac=1`, the sheared pair remains normalized Keller; its component degrees
at `(N,1)` are `N,1`. `square`

### Explicit inverse

After (6.4),

```text
y=Q/c,
x=(P-b(Q/c)^N)/a.
```

Composing with the inverse target shear gives a polynomial inverse for every
pair in `B_N`.

### Missing-monomial consequence

On the chart `a b q_N!=0`, recurrence (6.2) propagates nonzero coefficients
through the whole chain, including `q_0`. Omitting any interior chain monomial
is incompatible with the full Jacobian system. This is an exact treatment of
missing support, not a generic-coefficient convention.

## 7. Complete-top versus partial cancellation

The shear in (6.4) cancels the entire top polynomial `lambda P^N`. Cancelling
only `q_N x^N`, or any proper subset of the binomial chain, leaves another
monomial of the same `(N,1)`-weight `N^2`. The weighted degree and defect do not
decrease. Every certified descent must rebuild the support and verify strict
decrease of the actual integer defect.

## 8. Scope

`A_N` is an actual counterexample to an **affine-only** bounded-orbit principle,
not to the tame/full qualifying-weight question. `B_N` is a substantial exact
class, not a proof that every common-power edge extends to a complete binomial
chain. The remaining task is to force a certified complete-top shear or a
bounded terminal core for arbitrary Keller supports.
