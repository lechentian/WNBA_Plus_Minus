import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("all_player_bpm_stats.csv")

x = data[["AveragePlusMinus"]].values
y = data["Ridge_Plus_Min"].values
total_minutes = data["TotalMinutes"].values
#print(total_minutes)
#print(y)

model = LinearRegression()
model.fit(x, y)
r2_score = model.score(x, y)
print(model.coef_)
print(model.intercept_)
print(f"R-squared value: {r2_score}")
List_result = np.ndarray.tolist(model.coef_)
print(List_result)