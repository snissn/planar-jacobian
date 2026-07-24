# Collision Divisors, Galois Closure, and Primitive-Element Mutation

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
```

## 1. Setup and the correct height-one object

Let

```text
B=C[P,Q],
K=Frac(B),
L=C(x,y),
O=Cbar.
```

For a height-one prime `p` of `B`, all local generation statements concern

```text
O_p=O tensor_B B_p,
```

the entire finite semilocal algebra over the DVR `B_p`. Checking the factors
`O_q` separately does not detect residual collisions between distinct
components.

Let `theta in O` be integral and generically primitive. Put

```text
R_theta=B[theta],
M_theta=O/R_theta,
I_theta=Fitt^B_0(M_theta).
```

Because `O` and `R_theta` are finite locally free of the same rank, the
inclusion determinant generates `I_theta` locally. For every height-one
`p`,

```text
ord_p(I_theta)=length_{B_p}(O_p/B_p[theta]),                 (1.1)
```

and therefore

```text
B_p[theta]=O_p  <=>  (I_theta)_p=B_p.                        (1.2)
```

Equivalently, by Nakayama,

```text
B_p[theta]=O_p
  <=> kappa(p)[bar(theta)]=O_p/pO_p.                          (1.3)
```

## 2. Galois-closure Vandermonde formula

Let `N/K` be a Galois closure of `L/K`, let `S` be the normalization of `B`
in `N`, and write

```text
sigma_1,...,sigma_n:L -> N
```

for the `K`-embeddings. Define

```text
V(theta)=product_{i<j}(sigma_j(theta)-sigma_i(theta)).        (2.1)
```

If `f_theta` is the monic minimal polynomial of `theta`, then

```text
Disc(f_theta)=V(theta)^2
             =(-1)^(n(n-1)/2) Norm_{L/K}(f_theta'(theta)).    (2.2)
```

Choose a local integral `B`-basis `e_1,...,e_n` of `O`. Let

```text
E=(sigma_i(e_j))_{i,j},
W(theta)=(sigma_i(theta^(j-1)))_{i,j}.
```

If `A_theta` is the inclusion matrix of the power basis in the `e`-basis,
then

```text
W(theta)=E A_theta,

det(A_theta)=V(theta)/det(E).                                (2.3)
```

Squaring gives the exact index-discriminant identity

```text
Disc(B[theta]/B)=I_theta^2 Disc(O/B)                          (2.4)
```

as an equality of determinant ideals. Formula (2.3) uses an integral basis;
no Galois normal-basis assertion is made.

## 3. Intrinsic ramification versus accidental collision

Fix a height-one base prime `p` and a height-one prime `r` of `S` above it.

### Unramified `p`

The normal discriminant is a unit at `p`. Hence

```text
ord_p Disc(f_theta)
  =2 length_{B_p}(O_p/B_p[theta]).                            (3.1)
```

A zero of `sigma_i(theta)-sigma_j(theta)` along `r` means that two distinct
geometric etale sheets acquire the same residual value. Every such
height-one zero is accidental index support.

### Ramified `p`

Embeddings in the same inertia orbit necessarily have equal residual values.
The minimal forced contact is measured by the normal discriminant, or
locally by the different. A ramification-adapted element satisfies

```text
B_p[theta]=O_p,
```

so its Vandermonde valuation is exactly the intrinsic normal-discriminant
valuation. Extra contact inside an inertia orbit, or equality between
separate residue components of the semilocal fiber, contributes index.

Thus the correct invariant is not whether `V(theta)` vanishes. It is the
excess

```text
ord_p(I_theta)
  =(ord_p Disc(f_theta)-ord_p Disc(O/B))/2.                   (3.2)
```

The conductor of `B[theta]` in `O` need not equal `I_theta`, but their
height-one supports agree because either localizes to the unit ideal exactly
when the two orders are equal.

## 4. Base translation does not move anything

For every `h in B`,

```text
sigma_i(theta+h)-sigma_j(theta+h)
  =sigma_i(theta)-sigma_j(theta).                             (4.1)
```

The change from the power basis of `theta` to that of `theta+h` is upper
triangular with diagonal one. Therefore

```text
B[theta+h]=B[theta],
I_{theta+h}=I_theta.                                          (4.2)
```

Adding `h(P,Q)` is not a moving-index mutation. Scaling by a base unit also
preserves generation; scaling by a nonunit generally creates index along the
scale divisor.

## 5. Linear mutation and collision incidence

For `eta in O` and a scalar parameter `lambda`,

```text
sigma_i(theta+lambda eta)-sigma_j(theta+lambda eta)
 =delta_ij(theta)+lambda delta_ij(eta).                       (5.1)
```

On the Galois normalization over the finite etale locus, consider

```text
Z_ij={(s,lambda):
      delta_ij(theta)(s)+lambda delta_ij(eta)(s)=0}.           (5.2)
```

Unless the pair-difference in (5.1) is a unit for a special parameter,
`Z_ij` is a divisor in the product of a surface and the parameter line. Its
projection to parameter space is commonly dominant, so a generic parameter
still has a one-dimensional collision fiber. Genericity may make the divisor
reduced or move it away from a prescribed finite set; it does not make it
empty.

At a single base point, distinct sheet values form an open condition on
`lambda`. That condition tests one fiber only and imposes none of the global
coefficient identities needed to make every pair difference a unit.

## 6. Universal index form and generator scheme

Let `V(O)` be the vector bundle associated with the finite locally free
module `O`. It carries a universal element `Theta`. The determinant of

```text
1,Theta,...,Theta^(n-1)
```

defines an index section `Phi` of the determinant line. Since
`Pic(C[P,Q])=0`, a determinant trivialization represents it by a polynomial
index form.

The generator scheme is

```text
Gen(O/B)=D(Phi) subset V(O).                                  (6.1)
```

For a base scheme `T`, a section `theta_T` generates `O_T` exactly when
`Phi(theta_T)` is a unit. Fiberwise monogenicity says that

```text
Gen(O/B) -> Spec(B)
```

is surjective. Global monogenicity says that this surjective open morphism
has a global section. The second statement does not follow from the first.

Over a split geometric etale fiber `C^n`, the index form is the Vandermonde

```text
product_{i<j}(z_i-z_j),
```

and the nongenerator locus is the union of diagonal hyperplanes.

## 7. Exact criterion for a finite-dimensional family

Let `T` be a finite-type affine parameter scheme and let `theta_T` be a
polynomial family of integral elements. After trivializing the determinant
line, write

```text
Phi(theta_T) in C[P,Q] tensor C[T].                           (7.1)
```

For a closed parameter `tau`, the following are equivalent:

1. `theta_tau` generates `O_p` for every height-one base prime `p`;
2. `Phi(theta_tau)` has no height-one zero;
3. `Phi(theta_tau)` is a unit of `C[P,Q]`;
4. `Phi(theta_tau)` is a nonzero constant.

Expand the finite polynomial (7.1) as

```text
Phi(theta_T)=sum_{a,b} c_ab(T) P^a Q^b.
```

The exact good-parameter locus is

```text
c_ab=0 for every (a,b)!=(0,0),
c_00!=0.                                                       (7.2)
```

This is a simultaneous coefficient-cancellation problem. It is generally a
locally closed locus, not a generic open subset. A dimension count does not
show that (7.2) is consistent.

For `theta+lambda eta`, every nonconstant base coefficient of the index must
vanish at the same scalar `lambda`. For `theta+h(P,Q)eta` with bounded-degree
`h`, the coefficients of `h` are merely more parameters in the same system.
Allowing arbitrary polynomial expressions in several generators does not
change the problem: every expression reduces to one coefficient tuple in
`V(O)` and must still solve the unit equation.

## 8. Explicit moving divisors

The fixed-sheet cubic countermodel has

```text
Phi(X,Y)=-(uX^3+X^2Y+vY^3).
```

For `theta_lambda=w+lambda e`,

```text
Phi(theta_lambda)=-(u+lambda+lambda^3v).                      (8.1)
```

Every `theta_lambda` generates at both ramified height-one primes, but the
line in (8.1) is a nonempty unramified index divisor. Distinct parameters
give distinct lines. No coefficient pair `(x,y)` makes `Phi(x,y)` constant.

In the diagonal cubic model,

```text
Phi(X,Y)=-(tX^3+(t^2+1)Y^3),
```

and the divisor for `w+lambda e` depends on `lambda^3`. Parameters differing
by a cube root of unity give the same divisor; distinct cubes give distinct
divisors.

In the biquadratic Galois model,

```text
V(a+cb)=64c^2uv(u-c^2v),
ind(a+cb)=-4c^2(u-c^2v).
```

These examples explicitly separate the fixed intrinsic ramification factors
from moving accidental collision factors.

## 9. Monodromy interpretation

Over the finite etale locus `U`, the cover `Y_U -> U` is an `n`-sheeted
local system. A regular element `theta` gives a function on the cover. It
generates the finite algebra over `U` exactly when

```text
Y_U -> A1_U,
y |-> theta(y)
```

is a closed immersion, equivalently when it separates every geometric fiber.
The diagonal collision arrangement is permuted by monodromy and descends as
a union even when individual sheets cannot be labeled globally.

A generic function separates the generic fiber. The collision divisor is the
locus where that relative embedding fails. Monodromy therefore explains why
choosing distinct values once is not a global construction.

## 10. Divisor classes and Hartogs do not remove support

The index divisor on `Spec(B)` is principal because `B` is factorial. That
controls its divisor class, not its support; nonzero principal effective
divisors are abundant. Likewise, every sheet difference on the Galois
normalization has a principal divisor, but principal class zero does not make
that divisor empty.

A class-group route requires an additional effective-support theorem forcing
all zeros into a prescribed ramification or boundary divisor.

If local primitive elements have affine-linear transitions on a cover of all
`Spec(B)`, `Pic(B)=0` and `H^1(Spec(B),O_B)=0` globalize them. On a punctured
surface, extension of individual functions does not by itself trivialize the
affine torsor; Hartogs is not a substitute for the missing cocycle extension.

## 11. What remains Keller-specific

The strongest countermodel is smooth, rational, locally monogenic everywhere,
has squarefree tame branch with a fixed sheet over each branch component, and
contains an open `A2`. It still has no unit index value. On its open plane the
map has Jacobian `s(3us-2)`, so source etaleness fails.

For a Keller normalization, the missing simultaneous package is:

```text
L=C(x,y),
A2_source openly immersed in Y,
the finite map etale on A2_source,
and every theta in O restricting to a polynomial on that source.
```

A successful successor must use the constant-Jacobian/etale-source condition
to prove the unit equation (7.2), an equivalent support theorem, or a global
affine-transition reduction. No purely algebraic genericity assertion remains
available.
