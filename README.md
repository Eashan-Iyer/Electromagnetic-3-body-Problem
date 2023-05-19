# Electromagnetic-3-body-Problem
Summary: This is a spin-off of the three-body problem. The three body problem normally predicts the time evolution of three objects undergoing gravitational interactions. This program uses similar methods, but for simulating electromagnetic interactions between point charges.

Usage: In order to use the program, input the initial conditions of the system (the initial position and velocities), as well as the properties of the system (the value of the charge for each charges particle, and the mass). The electromagnetic force is then computed using Coulumb's law, and the particles move based on the forces they experience. This approach is repeated iteratively, based on user-inputted timesteps and simulation duration. The program then produces a list of position coordinates over time, and visualies then using mathplotlib.

Limitations: The three body problem is a simulation of a chaotic system. This means that numerical methods will only be able to predict the evolution of a system for a small amount of time. You can think of it like predicting the weather, which is doable for short timesteps, but predictions lose accuracy as they get further out in time.

This simulation does not account for gravitational interactions between the particles, nor does it account for quantum mechanical effects. Every particle is treated classically, with a definite position and momentum that evolves over time.
