import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("graph.csv")

x = data['UserName'].values[20:30]
y1 = data['Plus_min'].values[20:30]
y2 = data['Adjust_plus_min'].values[20:30]

# Create a figure and a set of subplots
plt.plot(x, y1, color='r', label='Plus min')
plt.plot(x, y2, color='g', label='Adjust plus min')

plt.xlabel("PlayerName")
plt.ylabel("Plus min")
plt.title("Plus min and Adjust plus min")

# Show the plot
plt.tight_layout()
plt.show()