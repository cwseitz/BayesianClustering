import numpy as np
import matplotlib.pyplot as plt

# Read the matrix data from the file
matrix_data = np.loadtxt('r_vs_thresh.txt')

# Plot the matrix as an image
print(matrix_data.shape)
plt.imshow(np.flipud(matrix_data[1:,1:]), cmap='jet')
plt.colorbar()
plt.title('Matrix Image')
plt.show()
