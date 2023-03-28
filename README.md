# RC-low-pass-filter
The code is a Python script that simulates the response of an RC low-pass filter circuit to a sinusoidal input voltage waveform. This is an example of a common application of electrical engineering concepts in semiconductor design.

Let's start by looking at the parameters that define the circuit. We have two resistors, R1 and R2, and a capacitor, C, that are used to create the low-pass filter circuit. The input voltage to the circuit is defined by Vin, which we set to 5 volts.

The first step in simulating the circuit response is to calculate the time constant of the circuit, which is given by the product of R1 and C. This is stored in the variable tau.

Next, we define the time range and time step for the simulation. The time range is set from t_start, which we set to 0, to t_stop, which we set to 5 times the time constant tau. The time step t_step is set to tau divided by 100. These values are used to create the input voltage waveform that we will use to simulate the circuit response.

We generate the input voltage waveform using a sinusoidal waveform with a frequency of 50 Hz. This waveform is stored in the variable Vin_waveform.

Now we are ready to simulate the circuit response. We create an empty list Vout to store the output voltage values, and we set Vout_prev to 0, which represents the output voltage at the previous time step. We then loop through each sample in the input voltage waveform and calculate the corresponding output voltage for that sample. We use the voltage divider equation to calculate the output voltage, which depends on the input voltage, the previous output voltage, and the circuit parameters R1 and R2. We append each output voltage sample to the Vout list and update Vout_prev to the current output voltage.

Finally, we plot the input and output waveforms using the Matplotlib library. We use plt.plot() to create line plots of the input and output waveforms, with time on the x-axis and voltage on the y-axis. We also add labels to the x-axis and y-axis and a title to the plot, and we use plt.legend() to add a legend to the plot that identifies the input and output waveforms.

Overall, this code demonstrates proficiency in basic electrical engineering concepts, such as RC circuits and voltage dividers, and it showcases an application of these concepts in semiconductor design. The code also uses common Python libraries like NumPy and Matplotlib, which are widely used in scientific computing and data visualization.
