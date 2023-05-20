import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

epsilon_0 = 8.854*(10**-12)  # Vacuum permittivity (F/m)
mu_0 = 4*np.pi*(10**-7)  # Vacuum permeability (T·m/A)
c = 299792458  # Speed of light (m/s)

# Defining the relevant properties of the bodies.
charges = [-3e-3, -4e-3, -5e-3]  #Units of Coulumbs
masses = [1, 1, 1]  #Units of Kg

# Setting the initial conditions of the simulation
positions = [[3, 0], [0, 4], [0, 0]]  #Units of meters
velocities = [[0, 0], [0, 0], [0, 0]]  #Units of meters per second

# Computing the electromagnetic force vector
def electromagnetic_force(q1, q2, r):
    force_magnitude = 1 / (4 * np.pi * epsilon_0) * q1 * q2 / (np.linalg.norm(r)**2)
    force_direction = r / np.linalg.norm(r)
    return force_magnitude * force_direction

# Computing the equations of motion of each object
def equations_of_motion(t, y):
    positions = np.array(y[:6]).reshape(3, 2)
    velocities = np.array(y[6:]).reshape(3, 2)
    forces = np.zeros((3, 2))

    for i in range(3):
        for j in range(3):
            if i != j:
                forces[i] += electromagnetic_force(charges[i], charges[j], positions[j] - positions[i])

    accelerations = forces / np.array(masses).reshape(3, 1)
    return np.concatenate((velocities.flatten(), accelerations.flatten()))

y0 = np.concatenate((np.array(positions).flatten(), np.array(velocities).flatten()))

# Integrating the equations of motion numerically to produce a solution. The timescale and numeric step number can be adjusted here
solution = solve_ivp(equations_of_motion, (0, 1), y0, t_eval=np.linspace(0, 0.15, 10000))

# Acquiring a list of position values to put into the graph.
positions_sol = solution.y[:6].reshape(3, 2, -1)

# Plotting the graph on pyplot
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.plot(positions_sol[i, 0], positions_sol[i, 1], label=f"Body {i + 1}")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.title("Motion of Three Bodies Undergoing Electromagnetic Interactions")
plt.show()
