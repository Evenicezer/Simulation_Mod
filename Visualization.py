import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dummy data
np.random.seed(0)
n = 30 # Number of data points

data = pd.DataFrame({
    'x_column': np.random.rand(n),
    'y_column': np.random.rand(n),
    'size_column': np.random.randint(1, 1300, n),
    'label_column': [f'Label {i+1}' for i in range(n)]
})

# Scatter plot with bubble sizes
plt.scatter(data['x_column'], data['y_column'], s=data['size_column'], alpha=0.5)

# Add labels to bubbles
for i, label in enumerate(data['label_column']):
    plt.annotate(label, (data['x_column'][i], data['y_column'][i]), ha='center')

# Customize the plot as needed (e.g., axes labels, title, etc.)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Bubble Visualization')

# Show the plot
plt.show()