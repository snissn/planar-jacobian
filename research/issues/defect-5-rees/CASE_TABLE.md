# Exhaustive Defect-Five Resonance and Weight Table

Assume a selected nonzero interior resonance has been oriented and normalized to

```text
P_a=x,  Q_(5-a)=c y,  c!=0,  p<=q.
```

An exponent-one top common power is an exact strict descent and is omitted from
the no-descent rows. Equal weights mean only `(p,q)=(1,1)`. For unequal weights,
the support sieve proves that the maximal common root is a pure `x`-power and
that the following list is exhaustive.

## 1. Universal rows

| Situation | Exact disposition |
|---|---|
| `(0,5)` or `(5,0)` nonzero | The complete top component is a polynomial coordinate; the full Keller map is triangular in coordinate-complement variables. |
| Top exponent `m=1` or `n=1` | Determinant-one target shear cancels the complete top layer and strictly lowers the actual defect to a nonnegative integer at most four. |
| Arithmetic `rho=gcd(p+a,q+5-a)` has no weighted-homogeneous support | No nonzero common root `H` exists; the no-descent branch is impossible before coefficient stairs. |
| Original `p>q` | Signed source swap and weight relabeling reduce to the table and preserve `kappa`. |
| Reversed target-component degree orientation | Signed target swap changes `(a,b)` to `(b,a)`, preserves `J=1`, and retains the scalar `c`. |

## 2. Exact no-descent weight families

| Position | Unequal-weight families left after the root sieve | Finite support exceptions | Generic decisive stairs |
|---|---|---|---|
| `(1,4)` | `p=1`, odd `q>=3` | extra `y^2` in `Q_1` at `q=3` | `2Af_1=0`, `2Af_2+f_1=0`, `2Af_3+f_2=0`, `2Ac+f_3=0` |
| `(2,3)` | `p=1`, `q>=2`, `3` not dividing `q`; or `p=2`, `q≡3 mod 4` | `(1,2)`, `(2,3)` | for `p=1`: three-step chain ending `3Ac`; for `p=2,q>=7`: `2Af=0`, `2Ac+f=0` |
| `(3,2)` | `p=1`, `q>=3`, `q not congruent to 2 mod 4`; or `p=3`, `q≡1 mod 6`, `q>=7` | `(1,3)` | for `p=1,q>3`: `4Af=0`, `4Ac+3uf=0`; for `p=3`: `2Ac=0` |
| `(4,1)` | `p=1`, `q>=2`, `q not congruent to 4 mod 5`; or `p=2`, odd `q` with `q not congruent to 2 mod 3`; or `p=4`, `q≡3 mod 8`, `q>=11` | `(1,2)`, `(1,3)`, `(2,3)` | coefficient of `S_1` is respectively `5Ac`, `3Ac`, or `2Ac` outside the exceptions |
| every interior position | `(1,1)` | `(1,4)` and `(2,3)` are new; signed target swaps give `(4,1)` and `(3,2)` | complete equal-weight ideals are inconsistent |

## 3. Simultaneous resonances in the exceptional systems

The selected scalar is never silently replaced by one. The only unequal-weight
systems in the table whose complete support permits another nonzero resonant
bracket have the following exact `S_5` equations.

| Position / weight | Other possible resonant bracket | Complete `S_5` scalar equation |
|---|---|---|
| `(2,3)`, `(1,2)` | `J(vy,kx)=-vk` | `c-vk=1` |
| `(2,3)`, `(2,3)` | `J(vy,kx)=-vk` | `c-vk=1` |
| `(3,2)`, `(1,3)` | `J(vy,kx)=-vk` | `c-vk=1` |
| `(4,1)`, `(1,2)` | `J(ty,kx)=-tk` | `c-tk=1` |
| `(4,1)`, `(1,3)` | `J(ty,ell x)=-t ell` | `c-t ell=1` |
| `(4,1)`, `(2,3)` | `J(ty,kx)=-tk` | `c-tk=1` |

All six systems contradict an earlier stair while `c!=0`; simultaneous
resonance therefore cannot repair them.

## 4. Complete exceptional equations

The exact equations, with complete supports and signs, are recorded in
`DERIVATION.md` Sections 7.2, 7.4, 8.2, and 9.2–9.4. Each saturated coefficient
ideal has unit Gröbner basis in `validate_defect5.py`.

## 5. Equal-weight completeness

For `(1,1)`, the common root is linear. In coordinates `X=H,Y` with
`J(X,Y)=1`:

- `(1,4)` forces the transverse coefficient of the resonant linear form to
  vanish through a cubic coefficient chain; the other resonant form then also
  loses its transverse coefficient, contradicting its nonzero determinant.
- `(2,3)` first forces `H|P_1` through the `Y^3` coefficient of
  `J(P_1,Q_1)`, then forces both transverse resonant coefficients to vanish.
- `(4,1)` and `(3,2)` are their exact signed target swaps.

This exhausts all four interior positions, both component orientations, both
source-weight orientations, zero layers, and multiple resonant terms.
