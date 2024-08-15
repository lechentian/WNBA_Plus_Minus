import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("graph2.csv")

x = data['UserName'].values
y1 = data['Plus_min'].values
y2 = data['Weighted_adjust_plus_min'].values

y1 =[float(i) for i in y1]
y2 =[float(i) for i in y2]

#print(min(y1))
#print(min(y2))
fig, ax = plt.subplots()
ax.scatter(y1, y2)

for i, txt in enumerate(x):
    ax.annotate(x[i], (y1[i], y2[i]))
plt.show()
