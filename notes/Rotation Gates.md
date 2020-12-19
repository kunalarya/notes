---
tags: [quantum-computing]
title: Rotation Gates
created: '2020-12-18T18:58:01.800Z'
modified: '2020-12-18T21:45:44.896Z'
---

# Rotation Gates

## Identities:

### Euler's Formula
$$
e^{i\theta}=\cos(\theta)+\sin(\theta)
$$

Simple substitutions:
$$
\frac{\sqrt2}{2} = \frac{\sqrt2\times\sqrt2}{\sqrt2\times2} = \frac{1}{\sqrt2}
$$

## Gates

### Y Rotation

$$
R_Y(\theta)
=\begin{bmatrix}
    \cos\frac{\theta}2 & -\sin\frac{\theta}2 \\
    \sin\frac{\theta}2 & \cos\frac{\theta}2
\end{bmatrix}
$$

### Y^0.5 Gate
So if we sub $\frac{\pi}{2}$ for $\theta$:
$$
Y^{1/2}
=\begin{bmatrix}
    \cos\frac{\pi}4 & -\sin\frac{\pi}4 \\
    \sin\frac{\pi}4 & \cos\frac{\pi}4
\end{bmatrix}
$$

Since $90\degree = \frac{\pi}{4}$ and $\cos\frac{\pi}{4} = \sin\frac{\pi}{4} = \frac{1}{\sqrt2}$:
$$
Y^{1/2}
=\begin{bmatrix}
    \frac{1}{\sqrt2} & -\frac{1}{\sqrt2} \\
    \frac{1}{\sqrt2} & \frac{1}{\sqrt2}
\end{bmatrix}
=\frac{1}{\sqrt2} \begin{bmatrix}
    1 & -1 \\
    1 & 1
\end{bmatrix}
$$

### X Rotation
$$
R_X(\theta)
=\begin{bmatrix}
    \cos\frac{\theta}2 & -i\sin\frac{\theta}2 \\
    -i\sin\frac{\theta}2 & \cos\frac{\theta}2
\end{bmatrix}
$$

### Z Rotation
$$
R_Z(\theta)
=\begin{bmatrix}
    e^{-i\frac{\theta}2} & 0 \\
    0 & e^{i\frac{\theta}2}
\end{bmatrix}
$$


#### Z^0.5

Plug $\frac{\pi}{2}$ into $R_Z$:

$$
R_Z(\frac{\pi}{2})
=\begin{bmatrix}
    e^{-i\frac{\pi}4} & 0 \\
    0 & e^{i\frac{\pi}4}
\end{bmatrix}
$$


By Euler's formula:
$$
e^{-i\frac{\pi}4} =
e^{i\frac{-\pi}4}  \\
= \cos(\frac{-\pi}{4}) + i\sin(\frac{-\pi}{4})
$$

But since $\frac{-\pi}{4} = \frac{3\pi}{4}$:

$$
= \cos(\frac{3\pi}{4}) + i\sin(\frac{3\pi}{4})  \\
= -\frac{1}{\sqrt2} + i\frac{1}{\sqrt2} \\
= \frac{i - 1}{\sqrt2}
$$
And

$$
e^{i\frac{\pi}4}  \\
= \cos(\frac{\pi}{4}) + i\sin(\frac{\pi}{4})  \\
= \frac{1}{\sqrt2} + i\frac{1}{\sqrt2} \\
= \frac{i + 1}{\sqrt2}
$$


Plugging those into the matrix:
$$
R_Z(\frac{\pi}{2})
=\begin{bmatrix}
    \frac{i - 1}{\sqrt2} & 0 \\
    0 & \frac{i + 1}{\sqrt2}
\end{bmatrix}
$$

Simplified to:
$$

R_Z(\frac{\pi}{2})
=\frac{1}{\sqrt2}
\begin{bmatrix}
    i - 1 & 0 \\
    0 & i + 1
\end{bmatrix}
$$

#### Z^-0.5

We can do basically the same math for the other rotation.
$$
R_Z(-\frac{\pi}{2})
= R_Z(\frac{3\pi}{2})
=\begin{bmatrix}
    e^{-i\frac{3\pi}4} & 0 \\
    0 & e^{i\frac{3\pi}4}
\end{bmatrix}
$$

To get:
R_Z(\frac{-\pi}{2})
=\frac{1}{\sqrt2}
\begin{bmatrix}
    i + 1 & 0 \\
    0 & i - 1
\end{bmatrix}
$$
