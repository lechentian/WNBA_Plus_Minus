import pandas as pd
from sklearn.linear_model import LinearRegression


#https://aiplanet.com/blog/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn/
data = pd.read_csv("bradleyterry_model_in_wnba.csv")

#print(data.shape)


x = data[['Dallas','Indiana','LosAngeles','Minnesota','NewYork','Phoenix','Seattle','Washington','LasVegas','Connecticut','Chicago','Atlanta']].values
y = data['ScoreDifferential'].values

#print(x)
#print(y)

model = LinearRegression()
model.fit(x, y)
r2_score = model.score(x, y)
print(model.coef_)
print(model.intercept_)
print(f"R-squared value: {r2_score}")