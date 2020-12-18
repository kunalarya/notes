---
tags: [quantum-computing]
title: Global Phase
created: '2020-12-18T20:41:09.225Z'
modified: '2020-12-18T21:45:44.871Z'
---

# Global Phase

Global phase does not matter in circuits, only relative phase between states.

The identity:

$$
\big| {\psi} \rangle = e^{-i\gamma} \cdot \big| {\psi} \rangle 
$$

For any given state, for example, a negative sign does not matter.

Proof:

$$
\begin{aligned}
    \big| {\psi} \rangle = e^{-i\gamma} \cdot \big| {\psi} \rangle \\
    \text{where } e^{-i\gamma}=1
\end{aligned}
$$

If we can show that there is a $\gamma$ that satisfies this equation, we can show the effect of a negative sign on global state.


$$
\begin{aligned}
    e^{-i\gamma} = 1 \\
    \ln{(e^{-i\gamma})} = \ln{1} \\
    \text{Since } \ln{1}=i\pi, \\
    -i\gamma = i\pi \\
    gamma = -\pi
\end{aligned}
$$

So a negative sign effects a $\pi$ global phase, which is not measurable.
