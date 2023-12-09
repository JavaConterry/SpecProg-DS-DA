import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import ipywidgets as widgets


time = np.linspace(0, 360)

def harmonic_with_noise(amplitude, frequency, phase, noise_mean, noise_covariance, show_noise):
    harmonic = amplitude * np.sin(frequency * time + phase)
    return harmonic

# Create initial values for a and b
initial_a = 1.0
initial_b = 10.0

# Create x values
x_values = np.linspace(0, 360, 100)

# Create the initial y values based on the initial values of a and b
y_values = harmonic_with_noise(initial_a, initial_b, 0, 0, 0, 0)

# Create the figure with sliders
fig = make_subplots(rows=1, cols=1, subplot_titles=["Harmonic function"])

# Add the harmonic function trace
harmonic_trace = go.Scatter(x=x_values, y=y_values, mode='lines', name='Harmonic Function')
fig.add_trace(harmonic_trace)

# Define sliders for a and b
slider_a = widgets.FloatSlider(value=initial_a, min=0, max=5, step=0.1, description='a:')
slider_b = widgets.FloatSlider(value=initial_b, min=0, max=100, step=1, description='b:')


# Define the function to update the plot
def update_plot(change):
    a = slider_a.value
    b = slider_b.value
    y_values = harmonic_with_noise(a, b, 0, 0, 0, 0)
    fig.update_traces(selector=dict(name='Harmonic Function'), y=[y_values])

# Observe changes in sliders and update the plot
slider_a.observe(update_plot, names='value')
slider_b.observe(update_plot, names='value')

# Show the plot
fig.show()
