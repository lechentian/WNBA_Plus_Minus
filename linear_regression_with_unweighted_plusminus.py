import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#https://aiplanet.com/blog/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn/
data = pd.read_csv("adjusted_plus_minus.csv")

#print(data.shape)



data = pd.read_csv("adjusted_plus_minus_3.csv")

#print(data.shape)

allPlayers = open('PlayersNames.csv', 'r')
Lines = allPlayers.readlines()
all_user_ids = []
all_user_name = []
for line in Lines:
    player_id_and_name = line.split(",")
    #all_ids = all_ids + player_id_and_name[0] + ","
    #if player_id_and_name[0] != "585":
    all_user_ids.append(player_id_and_name[0])
    all_user_name.append(player_id_and_name[1])

all_user_ids.pop()
coefficient = ","
#print(all_ids)


x = data[all_user_ids].values
y = data['ScoreDifferential'].values

#print(x)
#print(y)

model = LinearRegression()
model.fit(x, y)
r2_score = model.score(x, y)
print(model.coef_)
print(model.intercept_)
print(f"R-squared value: {r2_score}")
List_result = np.ndarray.tolist(model.coef_)
print(List_result)
#lista = (list)model.coef_
#print(lista)
print(len(List_result))
List_result.append(-1.223758894)

graph_df = pd.read_csv('All_Coefficients.csv')
graph_df["Unweighted_PlusMinus"] = List_result
graph_df.to_csv("All_Coefficients.csv", index=False)