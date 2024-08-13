import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#https://aiplanet.com/blog/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn/
data = pd.read_csv("adjusted_plus_minus_2.csv")

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
y_wight_sting_time = data['StintTime'].values
#print(x)
print(y_wight_sting_time)
print(type(y_wight_sting_time))
y_list = np.ndarray.tolist(y_wight_sting_time)
# print(y_list)
# for i in y_list:
#     if i <0:
#         print(i)


model = LinearRegression()
model.fit(x, y, sample_weight=y_wight_sting_time)
r2_score = model.score(x, y)
#print(model.coef_)
#print(model.intercept_)
#print(f"R-squared value: {r2_score}")
List_result = np.ndarray.tolist(model.coef_)
List_result.append(-1.223758894)
print(List_result)
print(len(List_result))
all_user_ids.append(5209660)


data = pd.read_csv("plusminusdataset.csv")
cc = data['AveragePlusMinus '].values
print(len(cc))


print(len(all_user_ids))

with open('graph.csv', 'w') as f:
    f.writelines("UserId,UserName,Plus_min,Adjust_plus_min" +"\n")
    for i in range(len(all_user_ids)):
        f.writelines(str(all_user_ids[i])+","+all_user_name[i].strip()+","+str(cc[i])+","+str(List_result[i])+"\n")