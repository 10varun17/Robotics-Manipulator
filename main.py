import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from robotic_manipulator import RoboticManipulator

def animate(i):
    ax.clear()
    
    # Extract joint angles and positions
    q = states[i][:len(lengths)]
    
    x0, y0 = 0, 0  # Base position
    x1 = lengths[0] * np.cos(q[0])
    y1 = lengths[0] * np.sin(q[0])
    x2 = x1 + lengths[1] * np.cos(q[1])
    y2 = y1 + lengths[1] * np.sin(q[1])
    
    # Draw links
    ax.plot([x0, x1], [y0, y1], 'b-', lw=5)  # Link 1
    ax.plot([x1, x2], [y1, y2], 'g-', lw=5)  # Link 2
    
    ax.set_xlim(-sum(lengths), sum(lengths))
    ax.set_ylim(-sum(lengths), sum(lengths))
    ax.set_title('Robotic Manipulator Simulation')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.grid()

# Simulation parameters
lengths = [1.0, 3.0]   # Lengths of the two links
masses = [2.0, 1.0]    # Masses of the two links

# Create an instance of the robotic manipulator
manipulator = RoboticManipulator(lengths, masses)

t = np.linspace(0, 10, 500)                         # Time parameters for simulation
initial_state = [np.pi / 4, np.pi / 4, 0.0, 0.0]    # Initial conditions: [theta1, theta2, p1, p2]
states = manipulator.simulate(initial_state, t)

fig, ax = plt.subplots(figsize=(8, 8))
ani = FuncAnimation(fig, animate, frames=len(t), interval=100)

plt.show()
