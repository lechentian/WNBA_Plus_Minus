import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("all_player_bpm_stats.csv")

x = data[["AveragePoints"]].values
y = data["AveragePlusMinus"].values
total_minutes = data["TotalMinutes"].values
#print(total_minutes)

model = LinearRegression()
model.fit(x, y, sample_weight=total_minutes)
r2_score = model.score(x, y)
print(model.coef_)
print(model.intercept_)
print(f"R-squared value: {r2_score}")
List_result = np.ndarray.tolist(model.coef_)
print(List_result)