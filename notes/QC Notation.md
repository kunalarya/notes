---
title: QC Notation
created: '2021-06-19T20:49:42.290Z'
modified: '2021-06-19T22:36:36.421Z'
---

# QC Notation

## Tensor Products

Tensor symbol is often omitted:
$$
\big| {\psi} \rangle \otimes \big| {\phi} \rangle \\

= \big| {\psi} \rangle  \big| {\phi} \rangle

$$

We often encounter:
$$

\langle \phi \big| A \big| \psi \rangle

$$

Which is equivalent to
$$

\big| \phi \rangle \cdot A \big| \psi \rangle

$$
i.e. the inner product.

## Error Correction

Often you will see e.g. $ZZ=I$. In this case, $ZZ$ is two $Z$ operators applied to the *same* qubit, and the result is equivalent to the matrix product, i.e. $Z*Z$.

In QEC, we often encounter $ZZZZ$ -- this is more likely a notational shortcut that refers to 4 separate $Z$ operators applied to separate qubits.
