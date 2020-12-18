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
\frac{\sqrt{2}}{2} = \frac{\sqrt{2}\times\sqrt{2}}{\sqrt{2}\times2} = \frac{1}{\sqrt{2}}
$$

## Gates

### Y Rotation

$$
R_Y(\theta)
=\begin{bmatrix}
    \cos\frac{\theta}2 & -\sin\frac{\theta}2 \\
    \sin\frac{\theta}2 & \cos\frac{\theta}2 \\
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

Since $90\degree = \frac{\pi}{4}$ and $\cos\frac{\pi}{4} = \sin\frac{\pi}{4} = \frac{1}{\sqrt{2}}$:
$$
Y^{1/2}
=\begin{bmatrix}
    \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\
    \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} 
\end{bmatrix}
=\frac{1}{\sqrt{2}} \begin{bmatrix}
    1 & -1 \\
    1 & 1 
\end{bmatrix}
$$
