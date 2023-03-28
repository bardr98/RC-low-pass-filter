import numpy as np
import matplotlib.pyplot as plt

# Define the circuit parameters
R1 = 1e3
R2 = 2e3
C = 1e-6
Vin = 5

# Calculate the time constant of the circuit
tau = R1 * C

# Define the time range and time step for simulation
t_start = 0
t_stop = 5 * tau
t_step = tau / 100

# Generate the input voltage waveform
t = np.arange(t_start, t_stop, t_step)
Vin_waveform = Vin * np.sin(2 * np.pi * t * 50)

# Simulate the circuit response to the input voltage
Vout = []
Vout_prev = 0
for Vin_sample in Vin_waveform:
    Vout_sample = (Vin_sample - Vout_prev * (1 / (R1 * C))) * (R2 / (R1 + R2))
    Vout.append(Vout_sample)
    Vout_prev = Vout_sample

# Plot the input and output waveforms
plt.plot(t, Vin_waveform, label='Input')
plt.plot(t, Vout, label='Output')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('RC Low-Pass Filter Response')
plt.legend()
plt.show()
