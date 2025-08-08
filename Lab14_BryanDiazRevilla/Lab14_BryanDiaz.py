"""
Lab14_bdiazrevilla_1.py
Author: Bryan Diaz Revilla
Purpose: This program plots three mathematical graphs—a circle, sine wave, and spiral—using matplotlib and math. It demonstrates how math functions can be visualized.
Date: August 7, 2025
"""

import matplotlib.pyplot as plt
import math

# Plot 1: Circle
x_circle = [math.cos(math.radians(a)) for a in range(360)]
y_circle = [math.sin(math.radians(a)) for a in range(360)]

plt.figure()
plt.plot(x_circle, y_circle, linewidth=2)
plt.title("Circumference of Circle")
plt.grid(True)

# Plot 2: Sine Wave
x_sin = [x for x in range(360)]
y_sin = [math.sin(math.radians(x)) * 3 for x in x_sin]

plt.figure()
plt.plot(x_sin, y_sin, linewidth=2)
plt.title("Sine Wave")
plt.grid(True)

# Plot 3: Spiral
x_spiral = []
y_spiral = []
for angle in range(720):
    radius = angle * 0.01
    x_spiral.append(radius * math.cos(math.radians(angle)))
    y_spiral.append(radius * math.sin(math.radians(angle)))

plt.figure()
plt.plot(x_spiral, y_spiral, linewidth=2)
plt.title("Spiral")
plt.grid(True)

plt.show()
