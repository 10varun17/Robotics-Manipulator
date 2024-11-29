import numpy as np
from scipy.integrate import odeint

class RoboticManipulator:
    def __init__(self, lengths, masses):
        self.lengths = np.array(lengths)   # Convert lengths to a NumPy array
        self.masses = np.array(masses)     # Convert masses to a NumPy array
        self.g = 9.81                      # Gravitational acceleration

    def hamiltonian(self, q, p):
        """ 
        Calculate the Hamiltonian of the system. 
        """
        # Kinetic energy
        T = 0.5 * np.sum(p**2 / (self.masses * self.lengths**2))
        
        # Potential energy
        V = 0
        for i in range(len(self.masses)):
            V += self.masses[i] * self.g * (self.lengths[i] * np.cos(q[i]))
        
        return T + V

    def equations_of_motion(self, state, t):
        """ 
        Calculate the equations of motion using Hamilton's equations. 
        """
        q = state[:len(self.lengths)]
        p = state[len(self.lengths):]
        
        q_dot = p / (self.masses * self.lengths**2)
        
        # Calculate forces (negative gradient of potential energy)
        p_dot = -np.array([self.masses[i] * self.g * np.sin(q[i]) for i in range(len(self.masses))])
        
        return np.concatenate([q_dot, p_dot])

    def simulate(self, initial_state, t):
        """ 
        Simulate the dynamics of the robotic manipulator. 
        """
        return odeint(self.equations_of_motion, initial_state, t)