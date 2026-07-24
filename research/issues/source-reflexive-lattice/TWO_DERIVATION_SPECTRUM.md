# Two-Derivation Fractional Residue Spectrum

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-002`, `SRL-003`, `SRL-008`

## 1. Divisor and branch data

Fix an irreducible target curve

```text
h(P,Q)=0
```

and a height-one valuation `w` of `L` above `(h)`. Let `e` be the ramification index and let `S` be the corresponding DVR. At the generic point of the reduced curve, put

```text
a_P = partial_P h mod h,
a_Q = partial_Q h mod h
```

in the residue field `kappa(h)`. The pair is not zero because characteristic zero excludes simultaneous divisibility of `h_P,h_Q` by `h`.

After strict henselization and extraction of a unit root, choose a branch parameter `s` with

```text
h=s^e.
```

The canonical translations satisfy

```text
D_P(h)=h_P,
D_Q(h)=h_Q.
```

Consequently their leading normal actions are

```text
D_P(s) = h_P/(e s^(e-1)),
D_Q(s) = h_Q/(e s^(e-1)).
```

Tangential and unit-correction terms have strictly larger `s`-valuation and do not change the residue operators.

## 2. Raw and normalized residue operators

In the normalization basis

```text
1,s,...,s^(e-1),
```

let

```text
R_e = diag(0,1/e,2/e,...,(e-1)/e).
```

Modulo `h`, the logarithmic operators `hD_P` and `hD_Q` have residues

```text
Res_w(hD_P) = a_P R_e,
Res_w(hD_Q) = a_Q R_e.
```

If `a_i` is nonzero, normalizing the corresponding translation by

```text
E_i = h/D_i(h) * D_i
```

gives

```text
Res_w(E_i)=R_e.
```

The normalized fractional spectrum is therefore

```text
{0,1/e,...,(e-1)/e} mod Z,
```

with the residue-degree multiplicity described in the local theorem.

## 3. Coordinate-independent pair spectrum

The raw pair remembers the conormal direction. For each exponent `j/e`, define

```text
rho_j = (j/e)(a_P,a_Q) in kappa(h)^2.
```

Changing a common logarithmic lattice by an integral boundary shift changes `rho_j` by an integral multiple of the normal vector `(a_P,a_Q)`. The intrinsic simultaneous spectrum is therefore the multiset

```text
Spec_pair(w)
 = { rho_j mod Z*(a_P,a_Q) : 0<=j<e },
```

again with residue-degree multiplicity.

Equivalently, it is the rank-one residue map

```text
normal symbol of a target derivation
       |->
normal symbol * R_e.
```

This description is independent of the chosen equation for the divisor: replacing `h` by a unit multiple rescales both the normal symbol and the logarithmic normalization in inverse ways.

## 4. What commutativity supplies

The exact translations commute:

```text
[D_P,D_Q]=0.
```

Their leading polar endomorphisms are already scalar multiples of the same diagonal operator `R_e`, so they commute at the residue level. This is the full compatibility forced by integrability in the normal direction.

The tangential Hamiltonian combination

```text
T_h = h_Q D_P - h_P D_Q
```

satisfies

```text
T_h(h)=0.
```

Its normal residue is zero:

```text
a_Q(a_P R_e)-a_P(a_Q R_e)=0.
```

This is a genuine cancellation, but only for the derivation that is tangent to the branch. It does not cancel the connection as a two-field system. Any combination

```text
V = b_P D_P+b_Q D_Q
```

with

```text
b_P a_P+b_Q a_Q != 0 mod h
```

is transverse and has normalized residue spectrum `j/e mod Z`. Because `(a_P,a_Q)` is nonzero, such a combination always exists locally.

## 5. No simultaneous integralization for `e>1`

Suppose one full finite lattice were stable under both `D_P` and `D_Q`. It would then be stable under every `B_(h)`-linear combination of them, including a transverse combination. The local no-lattice theorem gives a contradiction when `e>1`.

At the residue level, the same conclusion reads:

- an integral boundary shift changes `j/e` to `j/e+n`;
- reduction modulo `Z` leaves `j/e mod Z` unchanged;
- for `e>1`, the class `1/e mod Z` is nonzero;
- shifting the two matrices separately is not allowed when they arise from one common lattice and one integrable connection;
- canceling the tangent combination does not alter the transverse quotient.

Thus the pair contains geometric information—the normal covector and its tangent kernel—but no stronger ramification obstruction than one transverse derivation. It does not by itself prove `e=1`; it proves `e=1` only when a common finite exact-stable lattice is assumed.

## 6. Conductor, different, and pole shifts

For a fractional ideal `s^mS`, use the basis

```text
s^m,s^(m+1),...,s^(m+e-1).
```

The normalized residue representatives are

```text
(m+j)/e,       0<=j<e.
```

As `j` ranges through a complete residue system modulo `e`, the multiset modulo `Z` remains

```text
{0,1/e,...,(e-1)/e}.
```

Important special cases are:

- normalization: `m=0`;
- inverse different in the Kummer model: `m=1-e`;
- arbitrary reflexive fractional ideals: any integer `m`;
- multiplication by `h^N=s^(eN)`: shift by the integer `N`;
- conductor order basis `1,h^Ns,...,h^Ns^(e-1)`: nontrivial representatives `N+j/e`.

No one of these operations changes the fractional spectrum.

## 7. Keller symplectic and primitive identities

The equality

```text
dP wedge dQ = dx wedge dy
```

identifies the different order `e-1` in the local form

```text
dP wedge dQ = unit * s^(e-1) ds wedge dz.
```

Solving for a lifted normal vector field divides by exactly that factor. The identity identifies the denominator; it does not make the numerator divisible by it.

Likewise, the exact primitive

```text
P dQ + y dx = dH
```

supplies the full coefficient relations recorded in the principal-part packet. Its logarithmic coefficient vanishes, but higher negative Laurent coefficients are absorbed by negative coefficients of `H`. It neither alters `R_e` nor makes the nonzero classes `j/e mod Z` integral.

Therefore `SRL-008` is an obstruction statement: the exact Keller identities are compatible with the residue calculation and provide no hidden cancellation of its transverse fractional classes.
