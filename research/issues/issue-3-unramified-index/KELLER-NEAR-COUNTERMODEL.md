# Smooth Rational Fixed-Sheet Countermodel

```text
authority: MUTABLE_NONAUTHORITATIVE
engineering_status: DEVELOPMENT
execution_validity: NOT_A_SCIENTIFIC_EXECUTION
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
```

## 1. The theorem

Let

```text
B = C[u,v]
```

and let `O` be the free rank-three `B`-module with basis `1,w,e` and
multiplication

```text
w^2 = w-u e,
we  = -uv,
e^2 = v(w-1).                                                (1.1)
```

Then:

1. `O` is a connected smooth normal finite-flat `B`-algebra of rank three.
2. Its fraction field is rational and the generic cubic is non-Galois.
3. `O/B` is Zariski-locally monogenic on all of `Spec(B)`.
4. Its discriminant is squarefree, and every generic branch inertia is a
   transposition with one unramified sheet.
5. `Y=Spec(O)` contains an open subset `X_0` isomorphic to `A2`.
6. Nevertheless, `O` is not globally monogenic.
7. Every integral element generating all ramified height-one
   semilocalizations has nonempty index support at unramified generic points.
8. For the explicit open plane `X_0`, the finite map to `Spec(B)` has
   Jacobian `s(3us-2)`, not a nonzero constant.

Thus the following package is still insufficient for global monogenicity:

```text
smoothness + normality + finite flatness + rational function field
+ local monogenicity everywhere + squarefree tame branching
+ a fixed unramified sheet over each branch divisor
+ an open immersion A2 -> Y.
```

The exact Keller feature absent from this model is **etaleness on the open
plane**.

## 2. Associativity and the generic field

The multiplication is associative. The only nontrivial basis checks are

```text
(w^2)e = (w-u e)e = -uv-u v(w-1) = -uv w = w(we),
(we)e  = -uv e = v(w^2-w) = w(e^2).
```

Over `K=Frac(B)`, relation (1.1) gives

```text
e=(w-w^2)/u,
w^3-w^2-u^2v=0.                                             (2.1)
```

Put

```text
p(T)=T^3-T^2-u^2v.
```

The polynomial `p` is irreducible over `K`. Indeed, a root in `K` would be
integral over the integrally closed ring `B`, hence would lie in `B`.
Specializing `v=1` would give a polynomial root in `C[u]` of

```text
T^3-T^2-u^2.
```

No such root exists: if its degree were positive, the highest degree on the
left would be divisible by three and could not equal two; a constant root is
also impossible. Since `p` is cubic, it is irreducible. Therefore

```text
O tensor_B K = K(w)
```

is a field and `O` is a domain.

Equation (2.1) also gives

```text
v=w^2(w-1)/u^2,
```

so

```text
Frac(O)=C(u,w).
```

The function field is rational.

## 3. Exact index form

For

```text
alpha=c+xw+ye,
```

translation by `c in B` does not change the generated order. Direct
multiplication gives

```text
alpha^2 = (-2uvxy-vy^2)
          +(x^2+vy^2)w
          -u x^2 e.
```

Hence the determinant of `1,alpha,alpha^2` in the basis `1,w,e` is

```text
Phi(x,y)=-(u x^3+x^2y+v y^3).                                (3.1)
```

Consequently,

```text
B[alpha]=O  <=>  u x^3+x^2y+v y^3 is in C*.                  (3.2)
```

This binary cubic is the universal index form of the algebra modulo base
translation.

## 4. Local monogenicity everywhere

The three values

```text
-Phi(1,0)=u,
-Phi(0,1)=v,
-Phi(1,1)=1+u+v
```

have no common zero. Therefore the opens

```text
D(u), D(v), D(1+u+v)
```

cover `Spec(B)`, and `O` is generated there by `w`, `e`, and `w+e`,
respectively. This is local monogenicity on the whole base, not merely away
from a codimension-two set.

The transitions are nonlinear. For example, on `D(u)` one has

```text
e=(w-w^2)/u.
```

Thus affine-linear transition arguments do not apply.

## 5. No global generator

Assume for contradiction that

```text
u x^3+x^2y+v y^3=c                                           (5.1)
```

for some `x,y in C[u,v]` and `c in C*`. Set `u=0`, and write

```text
x_0=x(0,v),  y_0=y(0,v).
```

Then in `C[v]`,

```text
y_0(x_0^2+v y_0^2)=c.                                       (5.2)
```

Both factors in (5.2) must be units. Hence `y_0=a in C*` and

```text
x_0^2=b-a^2v
```

for some `b in C*`. The right side has degree one with nonzero linear
coefficient, and therefore cannot be a square in `C[v]`. This contradiction
proves that (5.1) has no solution.

Thus `O` is locally monogenic everywhere but not globally monogenic.

## 6. Smoothness and normality

On `D(u)`, the element `w` generates and

```text
O_u = B_u[w]/(w^3-w^2-u^2v).
```

The derivative of the defining equation with respect to `v` is `-u^2`, a
unit on this chart. Hence this chart is smooth.

On `D(v)`, the element `e` generates. From `w=1+e^2/v` and `we=-uv`,
one obtains

```text
O_v = B_v[e]/(e^3+ve+uv^2).
```

The derivative with respect to `u` is `v^2`, a unit on this chart.

Only the fiber over `(u,v)=(0,0)` remains. On `D(1+u+v)`, put
`alpha=w+e`. Its monic equation is

```text
g(T)=T^3-T^2+v(3u+1)T-v(u^2-uv+2u+1).                       (6.1)
```

At the origin, `g(T)=T^2(T-1)`. At the point `T=1`, one has
`partial g/partial T=1`. At the point `T=0`, one has
`partial g/partial v=-1`. Thus both points of the fiber are smooth.

Therefore `Y=Spec(O)` is smooth. In particular, `O` is normal and is the
integral closure of `B` in its fraction field.

## 7. Discriminant and simple fixed-sheet branching

The trace Gram matrix in the basis `1,w,e` is

```text
[ 3       1          0   ]
[ 1       1        -3uv  ]
[ 0     -3uv        -2v  ].
```

Its determinant is

```text
Disc(O/B)=-v(4+27u^2v).                                     (7.1)
```

The two factors are coprime and reduced. The second factor is smooth because
on its zero set `u` is nonzero and

```text
partial(4+27u^2v)/partial v=27u^2.
```

At the generic point of `v=0`, equation (2.1) becomes

```text
p(T)=T^2(T-1).
```

There is one double ramified sheet and one simple unramified sheet. At the
generic point of `4+27u^2v=0`, one has `u^2v=-4/27` and

```text
p(T)=(T-2/3)^2(T+1/3).
```

Again there is one double ramified sheet and one simple unramified sheet.
All ramification is tame because the characteristic is zero.

The generic cubic is non-Galois: it is irreducible, while its discriminant
has the nonsquare class of `-v(4+27u^2v)`.

This model therefore retains the fixed-sheet local monodromy pattern that a
Keller normalization is expected to have in degree three.

## 8. An open affine plane inside `Y`

Set

```text
z=1-w.
```

The relations become

```text
wz=ue,
we=-uv,
e^2=-vz.                                                   (8.1)
```

Let

```text
E=V(u,z) subset Y.
```

On `E`, one has `w=1` and `e=0`, while `v` is free. Hence

```text
E is isomorphic to A1.
```

Put

```text
X_0=Y-E=D(u) union D(z).
```

On `D(u)` define `s=w/u`; on `D(z)` define `s=e/z`. Equation (8.1) shows
that these definitions agree on the overlap. They give

```text
w=us,
z=1-us,
e=s(1-us),
v=-s^2(1-us)=us^3-s^2.                                    (8.2)
```

Conversely, formulas (8.2) define a morphism from `A2_{u,s}` to `Y-E`, and
the two constructions are inverse. Thus

```text
X_0 is isomorphic to A2_{u,s}.                               (8.3)
```

The finite map `Y -> Spec(B)` restricts on this open plane to

```text
(u,s) |-> (u, us^3-s^2).
```

Its Jacobian determinant is

```text
J=s(3us-2).                                                   (8.4)
```

Therefore the open plane is not an etale source. Its two ramification curves
are visible inside `X_0`.

This is the exact point at which the model fails to be a Keller
normalization: it has the open affine plane, but not source etaleness.

## 9. Moving unramified index divisors

For `lambda in C`, put

```text
alpha_lambda=w+lambda e.
```

Equation (3.1) gives

```text
Phi(alpha_lambda)=-(u+lambda+lambda^3v).                     (9.1)
```

The polynomial in (9.1) is divisible by neither branch factor in (7.1).
Thus every `alpha_lambda` generates both ramified height-one
semilocalizations. It nevertheless has the nonempty index divisor

```text
D_lambda: u+lambda+lambda^3v=0.                              (9.2)
```

Every generic point of `D_lambda` is unramified. Distinct values of
`lambda` give distinct divisors. Hence even in the smooth, rational,
squarefree, fixed-sheet model, constant primitive-element mutation moves the
collision divisor without eliminating it.

For a polynomial coefficient `h in B`,

```text
Phi(w+h e)=-(u+h+v h^3).
```

The no-unit proof in Section 5 applies to every possible coefficient pair
`x,y`, so arbitrary polynomial expressions in any finite generating set do
not evade the obstruction.

## 10. Exact scientific inference

This model is not a Keller counterexample. It proves only the following
negative statement:

> A purely algebraic moving-index theorem cannot be rescued by adding
> smoothness, rationality, squarefree tame branch, fixed unramified sheets,
> or even the existence of an open affine plane. A successful theorem must
> use the fact that the specified open affine plane is etale over the target.

The smallest surviving Keller-specific problem is therefore to convert the
constant-Jacobian condition on `A2_source` into a unit-value theorem for the
universal index form.
