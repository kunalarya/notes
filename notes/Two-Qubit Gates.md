---
title: Two-Qubit Gates
created: '2021-06-27T23:57:07.910Z'
modified: '2021-06-28T02:23:15.686Z'
---

# Two-Qubit Gates

A `CNOT` gate with *control* qubit $q_0$ and *target* qubit $q_1$ applies an `X` gate on $q_1$ if $q_0$ evaluates to the $\big| 1 \rangle$ state, and otherwise leaves $q_1$ alone.

The operation entangles the qubits,  as you can no longer treat them as separate states (i.e. this state is no longer "seperable").

One use case for a `CNOT` gate is that it can be used to "detect" whether an `X` gate has been applied to the control qubit $q_0$. Say you initialize the second qubit in state $\big| 0 \rangle$, apply a `CNOT` with the control on $q_0$ and the target on $q_1$, measuring $q_1$ will tell you whether an `X` was detected on $q_0$.

This also changes *changes* the state of $q_0$ so that any

A `CZ` gate is similar, but applies a `Z` gate instead. Note that this is subtly different from *detecting* a `Z`


## WIP: Measuring a Single Qubit

**Warning: This hasn't been validated!**

If you have a two-qubit state with $q_0$ and $q_1$, and it's state is:

$$
\alpha \big| {00} \rangle + \beta \big| {01} \rangle + \gamma \big| {10} \rangle + \delta \big| {11} \rangle
$$

tl;dr: say we measure $q_1$, the resulting system's state vector is:

$$

\sqrt{  }

$$

### Longer explanation
Say you wanted to measure $q_1$ but *not* $q_0$. We're ultimately looking for something in the form:

$$

\zeta \big| {0} \rangle + \eta \big| {1} \rangle

$$

which describes the state of just $q_0$ (since this will be *after* measuring $q_1$, so $q_1$ has been resolved to either $\big| {0} \rangle$ or $\big| {1} \rangle$)

_Case 1_: $q_1$ measures $\big| {0} \rangle$:

- We eliminate the cases where $q_1 = \big| {1} \rangle$, and are left with:
$$
\psi_{unnormalized}=\alpha \big| {00} \rangle + \cancel{\beta \big| {01} \rangle} + \gamma \big| {10} \rangle + \cancel{\delta \big| {11} \rangle} \\
=\alpha \big| {00} \rangle + \gamma \big| {10} \rangle
$$

* However, simply dropping those terms leaves us in an incorrect state because the probabilities will not sum to $1$. So we need to *normalize* the expression. To make the coefficients $\alpha$ and $\gamma$ sum to $1$, we divide the state vector by:

$$

\sqrt{\big|\alpha\big|^2 + \big|\gamma\big|^2 }

$$

Resulting in:

$$

\psi_{(q_1=0)} = \frac{ \alpha \big| {00} \rangle + \gamma \big| {10} \rangle }{\sqrt{\big|\alpha\big|^2 + \big|\gamma\big|^2 }}

$$

_Case 2_: $q_1$ measures $\big| {1} \rangle$:

- We eliminate the cases where $q_1 = \big| {0} \rangle$, and are left with:
$$
\psi_{unnormalized}=\cancel{\alpha \big| {00} \rangle} + \beta \big| {01} \rangle + \cancel{\gamma \big| {10} \rangle} + \delta \big| {11} \rangle\\
=\beta \big| {01} \rangle + \delta \big| {11} \rangle
$$

* Likewise we normalize by dividing by:

$$

\sqrt{\big|\beta\big|^2 + \big|\delta\big|^2 }

$$

Resulting in:

$$

\psi_{(q_1=1)} = \frac{ \beta \big| {01} \rangle + \delta \big| {11} \rangle }{\sqrt{\big|\beta\big|^2 + \big|\delta\big|^2 }}

$$



