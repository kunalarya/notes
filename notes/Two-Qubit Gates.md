---
title: Two-Qubit Gates
created: '2021-06-27T23:57:07.910Z'
modified: '2021-06-28T01:48:26.087Z'
---

# Two-Qubit Gates

A `CNOT` gate with *control* qubit $q_0$ and *target* qubit $q_1$ applies an `X` gate on $q_1$ if $q_0$ evaluates to the $\big| 1 \rangle$ state, and otherwise leaves $q_1$ alone.

The operation entangles the qubits,  as you can no longer treat them as separate states (i.e. this state is no longer "seperable").

One use case for a `CNOT` gate is that it can be used to "detect" whether an `X` gate has been applied to the control qubit $q_0$. Say you initialize the second qubit in state $\big| 0 \rangle$, apply a `CNOT` with the control on $q_0$ and the target on $q_1$, measuring $q_1$ will tell you whether an `X` was detected on $q_0$.

This also changes *changes* the state of $q_0$ so that any

A `CZ` gate is similar, but applies a `Z` gate instead. Note that this is subtly different from *detecting* a `Z`


## Measuring a Single Qubit

If you have a two-qubit state with $q_0$ and $q_1$, and it's state is:

$$
\alpha \big| {00} \rangle + \beta \big| {01} \rangle + \gamma \big| {10} \rangle + \delta \big| {11} \rangle
$$

Say you wanted to measure $q_1$ but *not* $q_0$. We're ultimately looking for something in the form:

$$

\zeta \big| {0} \rangle + \eta \big| {0} \rangle

$$

which describes the state of just $q_0$ (since this will be *after* measuring $q_1$, so $q_1$ has been resolved to either $\big| {0} \rangle$ or $\big| {1} \rangle$)

you can compute it by reasoning this way: you want the conditional probability that the unmeasured $q_0$ (the unmeasured qubit) is in the state $\big| {0} \rangle$ or the state $\big| {1} \rangle$ *given* that the measured qubit $q_1$ is either 
