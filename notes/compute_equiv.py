import numpy as np
import numpy.linalg as linalg
from numpy import array, kron

# 1/sqrt(2)
c = 1.0 / np.sqrt(2.0)

# Pauli gates.
X = array([[0, 1], [1, 0]])
Y = array([[0, -1j], [1j, 0]])
Z = array([[1, 0], [0, -1]])
I2 = np.eye(2)
swap = array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
cz = array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])

# CZ with the control and target qubits flipped
cz_flip = array([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]])

op1 = cz_flip @ kron(X, I2)
op2 = kron(X, Z) @ cz_flip

print(op2.tolist())

# Let's see if we can infer this.
# First, solve the system of equations:
#

import cirq

circuit = cirq.Circuit()
q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)
circuit.append([cirq.H.on(q0), cirq.H.on(q1)])
circuit.append([cirq.Y.on(q0) ** 0.25, cirq.Y.on(q1) ** -0.25])
circuit.append(cirq.X.on(q1) ** 0.25)
psi = cirq.Simulator().simulate(circuit).final_state_vector

