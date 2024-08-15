import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def generate_signal(freq, t):
    return np.sin(1 * np.pi * freq * t)


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')


def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.5, 1.5)
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(generate_signal(5, frame))  # 5 Hz sine wave
    ln.set_data(xdata, ydata)
    if frame > 1:
        ax.set_xlim(frame - 1, frame)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 1000),
                    init_func=init, blit=True)
plt.show()

# Function to generate a sine wave signal
def generate_signal(freq, t):
    return np.sin(2 * np.pi * freq * t)


# Initialize the plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')


# Initialize the plot limits
def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.5, 1.5)
    return ln,


# Update the plot with new data
def update(frame):
    xdata.append(frame)
    ydata.append(generate_signal(5, frame))  # 5 Hz sine wave
    ln.set_data(xdata, ydata)
    if frame > 1:
        ax.set_xlim(frame - 1, frame)
    return ln,


# Animate the plot
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 1000),
                    init_func=init, blit=True)
plt.show()
