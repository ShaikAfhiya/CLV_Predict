# Generated from: train.ipynb
# Converted at: 2026-04-04T12:10:49.902Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd

df=pd.read_csv('ecommerce_customer_behavior_dataset.csv')
df

df.info()

df.drop(columns=['Order_ID','Customer_ID','Date'],inplace=True)
df.columns

x=df.drop('Total_Amount',axis=1)
y=df['Total_Amount']
x

num_col=x.select_dtypes(exclude='object').columns
num_col

cat_col=x.select_dtypes(include='object').columns
cat_col

df.isnull().sum()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder

preprocessing=ColumnTransformer([
    ('num_col',StandardScaler(),num_col),
    ('cat_col',OneHotEncoder(),cat_col)
])
preprocessing

from xgboost import XGBRegressor


pipeline=Pipeline([
    ('preprocessing',preprocessing),
    ('model',XGBRegressor(n_estimators=3,
    learning_rate=0.1,
    max_depth=3))
])
pipeline

pipeline.fit(x_train,y_train)

from sklearn.metrics import r2_score,mean_squared_error
pred = pipeline.predict(x_test)
print('R2_score value:',r2_score(y_test, pred))
print('MSE value:',mean_squared_error(y_test, pred))

import joblib
model=joblib.dump(pipeline,'clv.pkl')
print('pkl file is create successfully!')