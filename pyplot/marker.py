# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
plt.plot(xpoints, ypoints, 'o')
plt.show()