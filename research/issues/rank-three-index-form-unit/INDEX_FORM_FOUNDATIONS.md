# Index-Form Foundations in Rank Three

```text
claims: IDX3U-01, IDX3U-02
status: CANDIDATE_PROVED_AT_STATED_FINITE_LOCALLY_FREE_SCOPE
```

## 1. Finite-locally-free scope

Let `B=C[P,Q]`, let `K=Frac(B)`, let `L=C(x,y)`, and let `O` be the integral
closure of `B` in `L`. This file works under

```text
O is finite locally free of rank 3 over B.                         (1.1)
```

The hypothesis has two inputs, which must not be conflated.

1. Finiteness of normalization follows in the repository baseline from the
   finite-normalization factorization. Independently, polynomial rings over a
   field are excellent/Nagata, so normalization in a finite field extension is
   finite.
2. Flatness is not automatic from finiteness. At a maximal ideal `m` of the
   regular surface `Spec(B)`, each normal two-dimensional local ring `O_q` over
   `m` is `S2`, hence Cohen-Macaulay. A regular parameter pair of `B_m` is a
   system of parameters in `O_q` and therefore an `O_q`-regular sequence.
   Auslander-Buchsbaum over the two-dimensional regular local ring `B_m` gives
   projective dimension zero. Thus `O_m` is free. At height one, finite
   torsion-free modules over a DVR are free. This is the argument already
   banked in issue #3.

A primary-source formulation of the flatness criterion is Grothendieck and
Dieudonne, *EGA IV*, Publ. Math. IHES **24** (1965), Proposition 6.1.5, with the
regular-target, Cohen-Macaulay-source, finite/equidimensional hypotheses stated
in the issue #3 source audit.

Nothing below infers finite local freeness merely from the symbol
“normalization.”

## 2. Trace splitting

The trace map of the finite locally free algebra is a `B`-linear map

```text
Tr = Tr_{O/B}: O -> B,
Tr(1)=3.
```

Because `3` is invertible in `B`,

```text
rho = (1/3) Tr: O -> B
```

is a retraction of `B*1 -> O`. Therefore

```text
O = B*1 direct_sum E,
E = ker(Tr),
rank_B(E)=2.                                                       (2.1)
```

Since `O` is finite projective, `E` is a direct summand of a projective module
and is projective. This is the exact hypothesis under which projectivity is
available.

Quillen-Suslin now applies to the polynomial ring `B=C[P,Q]`: every finitely
generated projective `B`-module is free. Hence

```text
E is free of rank 2.                                               (2.2)
```

Primary sources:

- D. Quillen, “Projective modules over polynomial rings,” *Inventiones
  Mathematicae* **36** (1976), 167-171, DOI 10.1007/BF01390008.
- A. A. Suslin, “Projective modules over a polynomial ring are free,”
  *Doklady Akademii Nauk SSSR* **229** (1976), 1063-1066; English translation,
  *Soviet Mathematics Doklady* **17** (1976), 1160-1164.

The binary-cubic coordinates below use a chosen free frame, but the determinant
section itself does not.

## 3. Intrinsic determinant line and index section

For `s in E`, define

```text
Phi(s) = 1 wedge s wedge s^2 in det_B(O).                          (3.1)
```

The splitting (2.1) identifies `det(O)` with `det(E)` by

```text
1 wedge e_1 wedge e_2  <->  e_1 wedge e_2.
```

Thus `Phi` is intrinsically a cubic law

```text
Phi: E -> det(E).
```

It has the exact covariance properties

```text
Phi(s+b)=Phi(s)              for b in B,
Phi(a s)=a^3 Phi(s)          for a in B.                           (3.2)
```

The first equality follows by elementary column operations on
`(1,s+b,(s+b)^2)`; the second is homogeneous scaling.

Choose a frame `e_1,e_2` of `E`, write `s=Xe_1+Ye_2`, and project products to
`E`:

```text
e_1^2 = (...) + a_1 e_1 + a_2 e_2,
e_1e_2 = (...) + b_1 e_1 + b_2 e_2,
e_2^2 = (...) + c_1 e_1 + c_2 e_2.
```

Relative to `e_1 wedge e_2`, direct expansion gives

```text
Phi(X,Y)
 = a_2 X^3
 + (2b_2-a_1) X^2Y
 + (c_2-2b_1) XY^2
 - c_1 Y^3.                                                       (3.3)
```

A change of frame changes the coordinate polynomial and the determinant-line
trivialization compatibly. No coefficient statement below is allowed to depend
on one chosen frame without this covariance.

Because `6` is invertible, polarization identifies the cubic law with a
`B`-linear map

```text
c_Phi: Sym^3(E) -> det(E).                                        (3.4)
```

## 4. Fixed-section index and exact local criterion

For any `s in O`, Cayley-Hamilton expresses every power of `s` in the span of
`1,s,s^2`. Hence the image of

```text
beta_s: B^3 -> O,
(a,b,c) |-> a+bs+cs^2
```

is `B[s]`. Its determinant is precisely `Phi(s^0)`, where
`s^0=s-Tr(s)/3`; translation invariance makes this equal to the determinant of
`1,s,s^2`.

Let

```text
M_s = O/B[s].
```

The square presentation gives

```text
Fitt^B_0(M_s) = (Phi(s^0))                                        (4.1)
```

in any determinant-line trivialization. Intrinsically, `Phi(s^0)` is a
generator of `det(O)` exactly when `beta_s` is an isomorphism.

For every prime `p` of `B`, and in particular every height-one prime,

```text
B_p[s]=O_p
<=> Phi(s^0) is a unit in B_p
<=> kappa(p)[bar s]=O_p/pO_p.                                     (4.2)
```

The last equivalence is Nakayama applied to the finite module `M_s`. The object
at a height-one base prime is the whole semilocal algebra `O_p`, not the
separate DVR factors `O_q`.

## 5. Discriminant and power-basis index

For a finite locally free `B`-module `M` with trace pairing, its discriminant is
the determinant of that pairing, intrinsically a section of
`(det M^vee)^{tensor 2}`. If `A_s` is the inclusion matrix of the power basis
in a local basis of `O`, then

```text
Gram(B[s]) = A_s^T Gram(O) A_s.
```

Therefore

```text
disc(B[s]/B) = Phi(s^0)^2 disc(O/B)                               (5.1)
```

as determinant sections/ideals. At a height-one prime `p`,

```text
v_p(disc(B[s]))
 = v_p(disc(O)) + 2 length_{B_p}(O_p/B_p[s]).                     (5.2)
```

If `Phi(s^0)` is nonzero, then `s` is generically primitive. Its degree-three
minimal polynomial is monic in `B[T]` when `s` is integral, and its polynomial
discriminant is the power-basis discriminant in (5.1).

These formulas are direct determinant identities. For the broader arbitrary-
base relation between binary forms, cubic algebras, and associated ideals, see
M. M. Wood, “Rings and ideals parameterized by binary n-ic forms,” *Journal of
the London Mathematical Society* **83** (2011), 208-231, DOI
10.1112/jlms/jdq074. Wood's correspondence is used only as a source-bound
context; equations (3.1)-(5.2) are proved directly here.

## 6. Imported issue #3 consequences

This packet consumes, without broadening, the following issue #3 candidate
statements.

1. **Finite-prime adaptation.** For any finite set of height-one base primes,
   one integral primitive section generates the whole semilocal normalization
   at all of them.
2. **Codimension-one globalization.** If one section generates `O_p` for every
   height-one base prime, then `B[s]=O`. The proof is the issue #3 hypersurface
   `S2` plus height-one `R1` argument (or the equal-rank determinant argument).
3. **Degree one from global monogenicity.** If `O=B[s]` with minimal polynomial
   `f`, then on the Keller open source
   `Omega_{A/B}=0`, so `f'(s)` restricts to a unit of `A=C[x,y]`, hence to a
   nonzero constant. If `deg f>1`, `f'(T)-c` is a lower-degree polynomial
   vanishing at `s`, contradicting minimality.

The direction of restriction is always induced by `O -> A`.

## 7. Foundational conclusion

The rank-three problem is exactly the existence of one `s in E` for which
`Phi(s)` generates `det(E)`, equivalently, after a frame is chosen,

```text
Phi(s) in B^* = C*.                                                (7.1)
```

Local monogenicity of fibers or localizations does not by itself produce such a
global section.
