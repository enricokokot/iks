import matplotlib.pyplot as plt
import numpy as np

def mm1_queue(ρ):
    L_q = (ρ**2) / (1 - ρ)
    W_q = ρ / (1 - ρ)
    return L_q, W_q

ρ_values = np.linspace(0, 0.99, 100)
L_q_values = []
W_q_values = []

for ρ in ρ_values:
    L_q, W_q = mm1_queue(ρ)
    L_q_values.append(L_q)
    W_q_values.append(W_q)

plt.plot(ρ_values, L_q_values, label='Average Queue Length (L_q)')
plt.plot(ρ_values, W_q_values, label='Average Waiting Time (W_q)')
plt.xlabel('Traffic Intensity (ρ)')
plt.ylabel('Value')
plt.legend()
plt.title('M/M/1 Queue')
plt.grid(True)
plt.show()