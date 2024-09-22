
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
df = pd.read_csv("adjusted_plus_minus_3.csv")

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


model = linear_model.Ridge(alpha=50000)
# #model.fit(X_train, y_train["ScoreDifferential"], sample_weight=y_train["StintTime"])
model.fit(X_train, y_train["ScoreDifferential"] / (y_train["StintTime"] / 60), sample_weight=y_train["StintTime"])
y_pred = model.predict(X_test)


print('w : ', model.coef_, ' b:', model.intercept_)
print('MSE :', mean_squared_error(y_test["ScoreDifferential"], y_pred))
ridge_coefficient = model.coef_.tolist()
ridge_coefficient.append(-1.23162381)
print(type(ridge_coefficient))
print(len(ridge_coefficient))

graph_df = pd.read_csv('All_Coefficients.csv')
graph_df["Ridge_Plus_Min"] = ridge_coefficient
graph_df.to_csv("All_Coefficients.csv", index=False)

# 1   9.34
# 10  9.33
# 100 9.32
# 1000 9.22
# 10000 9.02
# 30000 8.97852
# 40000 8.9754
# 50000 8.97503
# 55000 8.97533
# 60000 8.97584
# 70000 8.977
# 80000 8.978
# 90000 8.980
# 100000 8.982
# 110000 8.984
# 150000 8.99
# 1000000 9.03
# 10000000 9.05









