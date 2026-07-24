# Track: Global Monogenicity and the Moving Index Divisor

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Issue:** [#3](https://github.com/snissn/planar-jacobian/issues/3)  
> **Leaf:** [`../leaf-packets/unramified-index-elimination.md`](../leaf-packets/unramified-index-elimination.md)

Let

```text
B=C[P,Q],        K=Frac(B),
L=C(x,y),        Cbar=the integral closure of B in L,
Y=Spec(Cbar).
```

The Keller source `Spec(C[x,y])` is openly immersed in `Y` and is etale over
`Spec(B)`. A global power basis `Cbar=B[theta]` would force degree one, but a
primitive field element need not generate the integral closure.

## Correct height-one object

For a height-one prime `p` of `B`, generation is tested in the entire semilocal
DVR algebra

```text
Cbar_p=Cbar tensor_B B_p,
```

not separately in the local DVRs at primes of `Cbar` above `p`. Separate factor
generation can miss a residual collision between sheets.

For integral primitive `theta`, put

```text
M_theta=Cbar/B[theta],
I_theta=Fitt^B_0(M_theta).
```

At height one,

```text
ord_p(I_theta)=length_{B_p}(Cbar_p/B_p[theta]),
Disc(B[theta]/B)=I_theta^2 Disc(Cbar/B).
```

In a Galois closure the power-basis determinant is the Vandermonde product of
sheet differences divided by the determinant of an integral basis. At an
unramified prime every excess zero is an accidental sheet collision.

## Issue #3 disposition

### Candidate positive results

1. For every prescribed finite set of height-one primes of `B`, one integral
   primitive element can be patched to generate all corresponding semilocal
   algebras. This includes all ramified height-one primes.
2. If one element generates every height-one semilocalization, then
   `B[theta]=Cbar`: the hypersurface order is `S2`, height-one equality gives
   `R1`, and normality follows.
3. Once global monogenicity is established, the degree-one conclusion is
   noncircular. The Keller source makes `f_theta'(theta)` a unit of
   `C[x,y]`, hence a nonzero constant; minimality of `f_theta` forces degree
   one.

### Scoped algebraic obstruction

Purely algebraic elimination of the remaining unramified index divisor is
false. The issue packet constructs a connected smooth normal finite-flat
rational rank-three algebra that is locally monogenic everywhere, has
squarefree tame branch with a fixed unramified sheet, and contains an open
`A2`, but is not globally monogenic. Its universal index form is

```text
Phi(X,Y)=-(uX^3+X^2Y+vY^3),
```

which never represents a nonzero constant. The family `w+lambda e` moves the
unramified collision divisor

```text
u+lambda+lambda^3 v=0
```

without eliminating it. The open affine plane in this model is not etale over
the base, isolating the precise missing Keller property.

## Surviving bridge

The only surviving load-bearing statement is:

> Use etaleness of the specified open Keller source, together with its open
> immersion in `Y`, to construct an integral primitive element whose index
> ideal is a unit.

Equivalently, the universal index form on the trace-zero bundle must represent
an element of `C*`. The first exact successor is rank three, where this is a
binary cubic unit-representation problem.

## Forbidden shortcuts

- generic field primitivity;
- distinct values on one chosen fiber;
- finite-dimensional parameter counts;
- adding a base element, which leaves all sheet differences unchanged;
- class-group triviality, which makes the index divisor principal but not
  empty;
- rationality, smoothness, local monogenicity, squarefree branch, or an open
  affine plane without source etaleness;
- Hartogs extension of functions as a substitute for extension and
  trivialization of an affine primitive-element torsor.

## Detailed artifacts

The complete theorem packet, collision formulas, countermodels, source audit,
adversarial review, and handoff are in
[`../issues/issue-3-unramified-index/`](../issues/issue-3-unramified-index/README.md).

## Exit condition

This track closes only when the Keller-specific unit-index statement is proved
at exact scope, or when a still stronger Keller-near countermodel identifies an
even smaller missing hypothesis. The algebraic genericity bridge is already
disposed as false.