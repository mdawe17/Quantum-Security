import numpy as np
import math
import time
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()

N = 21

backend = Aer.get_backend('qasm_simulator') 
quantum_instance = QuantumInstance(backend, shots=1024)
shor = Shor(quantum_instance)

print("Starting Shor's Algorithm")

start = time.time()
result = shor.factor(N)
end = time.time() - start

print(f"Completed in: {end} seconds")

print(f"The list of unique prime factors of {N} as computed by the Shor's algorithm is {result.factors}")

print(f'Computed number of qubits for circuit: {4 * math.ceil(math.log(N, 2)) + 2}')
print(f'Actual number of qubits of circuit: {shor.construct_circuit(N).num_qubits}')
