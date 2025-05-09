import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Define the function you want to plot in 3D
def z_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


# Generate coordinate matrices from coordinate vectors
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = z_function(x, y)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap="viridis", edgecolor="none")

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

# Set labels
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

# Set title
ax.set_title("3D Surface Plot")

plt.show()
