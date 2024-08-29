
#https://blog.csdn.net/YUZHOUYANGAND/article/details/118404590
#https://blog.csdn.net/null18/article/details/133079879
#https://blog.csdn.net/weixin_43569478/article/details/108079690

#https://blog.csdn.net/weixin_44225602/article/details/112912067
#https://blog.csdn.net/Cyril_KI/article/details/106969315


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error

# importing data
df = pd.read_csv("adjusted_plus_minus_new_scoredifferential.csv")

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

#x = df[['Accept','Enroll','Top10perc','Top25perc','F.Undergrad','P.Undergrad','Outstate','Room.Board','Books','Personal','PhD','Terminal','S.F.Ratio','perc.alumni','Expend','Grad.Rate']]
#y = df['Apps']


x = df[all_user_ids]
y = df[['ScoreDifferential', 'StintTime']]


# using the train test split function
X_train, X_test,y_train, y_test = train_test_split(x, y, random_state=104, test_size=0.25, shuffle=True)

# printing out train and test sets

print('X_train : ')
print(X_train.head())
print('')
print('X_test : ')
print(X_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())


# model = LinearRegression(fit_intercept=True)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)


model = linear_model.Ridge(alpha=500)
model.fit(X_train, y_train["ScoreDifferential"], sample_weight=y_train["StintTime"])
y_pred = model.predict(X_test)


print('w : ', model.coef_, ' b:', model.intercept_)
print('MSE :', mean_squared_error(y_test["ScoreDifferential"], y_pred))
ridge_coefficient = model.coef_.tolist()
ridge_coefficient.append(-1.23162381)
print(type(ridge_coefficient))
print(len(ridge_coefficient))

graph_df = pd.read_csv('graph.csv')
graph_df["Ridge_Plus_Min_2"] = ridge_coefficient
graph_df.to_csv("graph.csv", index=False)

# 65.1635877073379  0.1
# 65.12778089470923 1
# 64.90359354122225 10
# 64.43538743730221 100
# 64.17153253561004 300
# 64.14448314828768 500
# 64.15379620786273 550
# 64.20400281529821 700
# 64.25068895148738 800
# 64.30467889486495 900
# 64.36415742154612 1000
# 64.49472531300033 1200
# 64.70828783494683 1500
# 65.0842149098752  2000
# 69.70668105961717 10000





