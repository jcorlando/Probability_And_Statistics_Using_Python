import numpy
import matplotlib.pyplot as plt

# Create vector
Position = numpy.array([ [2],
                         [3],
                         [4] ])


# Print vector contents
# ----------------------
print("\nThis is 3D Column Vector of Integers")
print("--------------------------------------")
print("\nPosition vector  ==  \n")
print(Position)
print("\nPosition[0]  ==  ", Position[0])
print("Position[1]  ==  ", Position[1])
print("Position[2]  ==  ", Position[2])
print("Magnitude of Vector is  ==  ", numpy.linalg.norm(Position), "\n")


# Plot vector using MatPlotlib
# -----------------------------
origin = numpy.array([ [0],
                       [0],
                       [0] ])

# Configure plot to show a 3-D
# plot instead of a 2-D plot
fig = plt.figure()
ax = plt.axes(projection='3d')

# Set the axis limits so the plot 
# properly shows the vector
ax.set_xlim([-1, 10])
ax.set_ylim([-1, 10])
ax.set_zlim([-1, 10])



# Show the 3-D vector in the graph as an arrow starting at the origin with a "RED" color
ax.quiver(origin[0], origin[0], origin[0], Position[0], Position[1], Position[2], color='red')

# Show the plot
plt.show()



