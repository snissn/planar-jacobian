# Collision Divisors, Galois Closure, and Primitive-Element Mutation

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
```

## 1. Galois-closure formula

Let `N/K` be a Galois closure of `L/K`, let `S` be the normalization of `B` in `N`, and let

```text
sigma_1,...,sigma_n: L -> N
```

be the `K`-embeddings. For an integral primitive `theta`, define

```text
V(theta) = product_{i<j} (sigma_j(theta)-sigma_i(theta)).
```

Then

```text
Disc(f_theta) = V(theta)^2
              = (-1)^(n(n-1)/2) Norm_{L/K}(f_theta'(theta)).       (1.1)
```

Choose a local `B`-basis `e_1,...,e_n` of `O`. Let

```text
E = (sigma_i(e_j))_{i,j},
W(theta) = (sigma_i(theta^(j-1)))_{i,j}.
```

If `A_theta` is the inclusion matrix of the power basis in the `e`-basis, then

```text
W(theta) = E A_theta,

det A_theta
  = det W(theta) / det E
  = V(theta) / det(sigma_i(e_j)).                                  (1.2)
```

Squaring (1.2) is exactly the discriminant/index identity

```text
Disc(f_theta) = ind(theta)^2 Disc(O/B).                              (1.3)
```

Thus the Vandermonde records both intrinsic ramification and accidental collision; dividing by the determinant of an integral normal basis removes the intrinsic contribution and leaves the index.

## 2. Which collisions are intrinsic?

Fix a height-one base prime `p` and a height-one prime `r` of `S` above it.

- **Unramified `p`.** Inertia at `r` is trivial. A zero of `sigma_i(theta)-sigma_j(theta)` along `r` means two distinct geometric étale sheets have equal residual `theta`-value. Every such zero is accidental. Formula (1.3) gives

  ```text
  v_p(Disc(f_theta)) = 2 length_{B_p}(O_p/B_p[theta]).
  ```

- **Ramified `p`.** Embeddings in one inertia orbit necessarily acquire equal residual values. Their minimal contact is measured by the different of `O/B`. A ramification-adapted element has

  ```text
  length_{B_p}(O_p/B_p[theta])=0,
  ```

  so the valuation of its Vandermonde is exactly the intrinsic normal discriminant valuation. Extra contact inside an inertia orbit, or equality between distinct residue components, contributes index support.

The correct separation is therefore not "Vandermonde zero versus nonzero." It is

```text
excess Vandermonde valuation
  = (power-basis discriminant valuation - normal discriminant valuation)/2.
```

## 3. Translation by the base does nothing

For every `h in B`,

```text
sigma_i(theta+h)-sigma_j(theta+h)
  = sigma_i(theta)-sigma_j(theta).
```

Equivalently, the binomial change from

```text
1,theta,...,theta^(n-1)
```

to

```text
1,theta+h,...,(theta+h)^(n-1)
```

is upper triangular with diagonal one. Hence

```text
B[theta+h]=B[theta],
I_{theta+h}=I_theta,
Ind(theta+h)=Ind(theta).
```

Adding `h(P,Q)` is not a moving-index mutation at all.

Scaling by a base unit also preserves generation. Scaling by a nonunit generally creates index along the scale divisor.

## 4. Linear mutation moves divisors; it does not generically remove them

For `eta in O` and a constant parameter `lambda`,

```text
sigma_i(theta+lambda eta)-sigma_j(theta+lambda eta)
 = delta_ij(theta)+lambda delta_ij(eta).                             (4.1)
```

On the Galois normalization over the finite étale locus, the incidence

```text
Z_ij = { (s,lambda) : delta_ij(theta)(s)+lambda delta_ij(eta)(s)=0 }
```

is usually a divisor in a surface times the parameter line. Its projection to the parameter line is typically dominant, so a generic parameter has a one-dimensional collision fiber. Genericity can make the divisor reduced or move it away from a prescribed finite set; it does not make the divisor empty.

At one fixed base point, pairwise distinct values are an open condition on `lambda`. That condition controls only one fiber. It imposes none of the coefficient identities required to make all pair differences units on the entire étale locus.

## 5. The universal index form

Let `V(O)` be the vector bundle of the finite locally free `B`-module `O`. It carries a universal element `Theta`. The determinant of

```text
1,Theta,...,Theta^(n-1)
```

defines an index section `Phi` of a line bundle on `V(O)`. Since `Pic(B)=0`, it may be represented after a determinant trivialization by a polynomial index form.

The generator scheme is

```text
Gen(O/B) = D(Phi) subset V(O).                                      (5.1)
```

For a base scheme `T`, a section `theta_T` generates `O_T` exactly when its index section is a unit. Fiberwise monogenicity says that

```text
Gen(O/B) -> Spec(B)
```

is surjective. Global monogenicity says that this surjective open morphism has a section. The latter does not follow from the former.

Over a split étale geometric fiber `O_b = C^n`, `Phi` is the Vandermonde

```text
product_{i<j}(z_i-z_j),
```

and the non-generator locus is the union of the diagonal hyperplanes.

## 6. Exact criterion for a finite-dimensional parameter family

Let `T` be a finite-type affine parameter scheme over `C`, and let `theta_T` be a polynomial family of integral elements. After trivializing the determinant line, write

```text
Phi(theta_T) in C[u,v] tensor C[T].
```

For a closed parameter `tau`, the following are equivalent:

1. `theta_tau` generates every height-one semilocalization.
2. `Phi(theta_tau)` has no height-one zero.
3. `Phi(theta_tau)` is a unit of `C[u,v]`.
4. `Phi(theta_tau)` is a nonzero constant.

If the family has bounded base degree, expand

```text
Phi(theta_T)=sum_{a,b} c_ab(T) u^a v^b.
```

The exact good-parameter locus is

```text
c_ab=0 for every (a,b)!=(0,0),
c_00 != 0.                                                          (6.1)
```

This is a coefficient-cancellation problem, not a generic-open condition. A dimension count does not prove that (6.1) is consistent, and generic separation on one fiber tests only a single evaluation of `Phi`.

For a one-parameter family `theta+lambda eta`, the index is a polynomial in `lambda` with coefficients in `B`; all nonconstant base coefficients must vanish at the same `lambda`. For a bounded-degree polynomial mutation `theta+h(u,v)eta`, the same criterion applies after treating the coefficients of `h` as parameters.

## 7. Arbitrary polynomial expressions do not evade the index form

Choose any finite `B`-module generating set, or a basis when available. Every polynomial expression in several integral generators reduces to one element of `O`, hence to one coefficient tuple in `V(O)`. Its generation property is still exactly the unit equation

```text
Phi(c_1,...,c_{n-1}) in C*.                                        (7.1)
```

Translation in the coefficient of `1` disappears. Enlarging the syntactic class of expressions does not change the mathematical problem.

## 8. Monodromy interpretation

Over the finite étale locus `U`, the cover `Y_U -> U` is an `n`-sheeted local system. A regular element `theta` gives a regular function on the cover. It generates the finite algebra over `U` exactly when

```text
Y_U -> A1_U,   y |-> theta(y)
```

is a closed immersion, equivalently when it separates every geometric fiber. The diagonal arrangement of collisions is permuted by monodromy; its union descends even when individual sheets cannot be labeled globally.

A generic function separates the generic fiber. The moving collision divisor is the locus where this relative embedding fails. Monodromy explains why "choose distinct values once" is not a global construction.

## 9. Divisor-class control is insufficient by itself

The index divisor on `Spec(B)` is principal because `B` is factorial. This does not force it to vanish: nonzero principal effective divisors are abundant. The rank-three countermodel has `Cl(B)=0` and a nonempty principal moving index divisor for every ramification-adapted generator.

On the Galois normalization, every individual difference has a principal divisor. Again, principal class zero controls linear equivalence, not support. A class-group route would need an additional effective-support theorem forcing every zero of every sheet difference into the ramification/boundary divisor. No such theorem follows from class-group triviality.

## 10. What the Keller open immersion actually adds

For a Keller normalization, the special package is:

1. `L=C(x,y)` is rational.
2. `X=A2_source` is openly immersed in `Y`.
3. The finite map is étale on `X`, so every ramification divisor lies in `Y-X`.
4. Every `theta in O` restricts to a polynomial in `C[x,y]`.
5. If `theta` globally generates, then `f_theta'(theta)` restricts to a unit of `C[x,y]`, forcing degree one.

The locally-monogenic rank-three countermodel lacks rationality and the open affine-plane source. The rational corank-two countermodel has rational function field but lacks the Keller étale-source package. Therefore the counterexamples block only the **purely algebraic** bridge. A rescue must use the simultaneous package above to prove the unit equation (7.1), an affine-transition reduction, or an equivalent support theorem.
