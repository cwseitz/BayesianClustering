import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Read the data from data.txt
data = pd.read_csv('data.txt')

# Read the labels from labels.txt
labels = pd.read_csv('labels/clusterscale20 thresh20labels.txt', header=None)
labels = labels.transpose()
# Merge the data and labels based on index
merged_data = pd.concat([data, labels], axis=1)
# Scatter plot with color-coded clusters
cmap = cm.get_cmap('viridis')  # Choose the desired colormap (e.g., 'viridis')
plt.scatter(merged_data['x'], merged_data['y'], c=merged_data[0], s=1, marker='x', cmap=cmap)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Cluster Colors')
plt.colorbar(label='Cluster Number')
plt.show()

