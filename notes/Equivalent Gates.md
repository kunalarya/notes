---
title: Equivalent Gates
created: '2020-12-18T21:45:11.152Z'
modified: '2020-12-18T23:56:10.038Z'
---

# Equivalent Gates

## Trivial Pauli Flips

These are sort of obvious, when pictured as rotations about a sphere:
$$
XX = I
$$

$$
YY = I
$$

$$
ZZ = I
$$

That is, if you rotate about an axis $\pi$ (or $180\degree$) twice, you will end up where you started.

## Hadamard

A Hadamard gate is defined by:

$$
\frac{1}{\sqrt2}
\begin{bmatrix}
   1 & 1 \\
   1 & -1
\end{bmatrix}
$$

It is equivalent to a $Y^{\frac{1}{2}}$ rotation (i.e. a $\frac{\pi}{2}$, or $90\degree$, rotation about the Y axis) followed by a full $\pi$, or $180\degree$, rotation about the X axis.

We'll show equivalence here.

Given the gates:
$$
X = 
\begin{bmatrix}
   0 & 1 \\
   1 & 0
\end{bmatrix}
$$

and

$$
Y^{\frac{1}{2}}=
\frac{1}{\sqrt2}
\begin{bmatrix}
   1 & -1 \\
   1 & 1
\end{bmatrix}
$$

First we'll show: $XY^{\frac{1}{2}}$. **Important**: This is the same as applying a $Y^{-\frac{1}{2}}$ gate first, *then* an $X$ gate.
Then we'll show equivalence with $Y^{-\frac{1}{2}}X$.

Given:
$$
\begin{aligned}
XY^{\frac{1}{2}}

=\frac{1}{\sqrt2}
\begin{bmatrix}
   0 & 1 \\
   1 & 0
\end{bmatrix}
\begin{bmatrix}
   1 & -1 \\
   1 & 1
\end{bmatrix} 

= \frac{1}{\sqrt2}
\begin{bmatrix}
   1 & 1 \\
   1 & -1
\end{bmatrix}

\end{aligned}
$$
Which we can see is exactly the Hadamard gate.

Note that the same is *not* true if we switch the order of the gates.

For the other order, first we'll define $Y^{-\frac{1}{2}}$. This computed by evaluating $R_Y(\frac{3\pi}{2})$. Recall that $R_Y$ uses $\sin(\frac{\theta}{2})$ & $\cos(\frac{\theta}{2})$, and that $\sin(\frac{3\pi}{4})=\frac{1}{\sqrt2}$ and $\cos(\frac{3\pi}{4})=-\frac{1}{\sqrt2}$

$$
Y^{-\frac{1}{2}}
= \frac{1}{\sqrt2}
\begin{bmatrix}
   -1 & -1 \\
   1 & -1
\end{bmatrix}
$$
And so:
$$
\begin{aligned}
Y^{-\frac{1}{2}}X 

=\frac{1}{\sqrt2} 
\begin{bmatrix}
   -1 & -1 \\
   1 & -1
\end{bmatrix} 
\begin{bmatrix}
   0 & 1 \\
   1 & 0
\end{bmatrix}

= \frac{1}{\sqrt2}
\begin{bmatrix}
   -1 & -1 \\
   -1 & 1
\end{bmatrix}

= -\frac{1}{\sqrt2}
\begin{bmatrix}
   1 & 1 \\
   1 & -1
\end{bmatrix}

\end{aligned}
$$

But, we know that global phase is not measurable, so we can assume that the negative sign is the same as a $2\pi$ global phase:


$$
= \frac{1}{\sqrt2}
\begin{bmatrix}
   1 & 1 \\
   1 & -1
\end{bmatrix}
$$

Which is exactly a Hadamard gate.
