import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons, Button
import math
import numpy as np

def harmonic_with_noise(amplitude, frequency, phase, noise_mean, noise_covariance, show_noise):
    time = np.arange(0, 360)
    harmonic = amplitude * np.sin(frequency * time + phase)
    if show_noise is True:
        noise = np.random.normal(noise_mean, noise_covariance, size=len(time))
        harmonic += noise
    return time, harmonic

init_amplitude = 1.0
init_frequency = 0.1
init_phase = 0
noise_mean = 0
noise_covariance = 0.1
show_noise = False

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.50)

time, harmonic = harmonic_with_noise(init_amplitude, init_frequency, init_phase, noise_mean, noise_covariance, show_noise)
line, = ax.plot(time, harmonic, label='Harmonic Signal')

# Create sliders with distinct axes
ax_amplitude = plt.axes([0.2, 0.25, 0.65, 0.03])
amplitude_slider = Slider(ax_amplitude, 'Amplitude', 0.1, 5.0)

ax_frequency = plt.axes([0.2, 0.20, 0.65, 0.03])
frequency_slider = Slider(ax_frequency, 'Frequency', 0.1, 5.0)

ax_phase = plt.axes([0.2, 0.15, 0.65, 0.03])
phase_slider = Slider(ax_phase, 'Phase', 1, 100)

# Create a checkbox for Show noise
ax_show_noise = plt.axes([0.2, 0.09, 0.3, 0.04])
show_noise_checkbox = CheckButtons(ax_show_noise, ['Show noise'])

reset_button = Button(plt.axes([0.53, 0.09, 0.3, 0.04]), "Reset")

def update_graph(val):
    amplitude = amplitude_slider.val
    frequency = frequency_slider.val
    phase = phase_slider.val
    show_noise = show_noise_checkbox.get_status()[0]

    time, harmonic = harmonic_with_noise(amplitude, frequency, phase, noise_mean, noise_covariance, show_noise)
    line.set_ydata(harmonic)
    fig.canvas.draw_idle()

def reset_init_vals(val):
    amplitude_slider.reset()
    frequency_slider.reset()
    phase_slider.reset()
    show_noise_checkbox.set_active(False)

amplitude_slider.on_changed(update_graph)
frequency_slider.on_changed(update_graph)
phase_slider.on_changed(update_graph)
show_noise_checkbox.on_clicked(update_graph)
reset_button.on_clicked(reset_init_vals)

# Display the plot
plt.legend()
plt.show()
