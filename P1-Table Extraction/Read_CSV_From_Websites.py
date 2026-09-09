#Import libraries needed
import pandas as pd

#Reading 1 csv file form the website
df = pd.read_csv("https://www.timestored.com/data/sample/titanic.csv")

#Rename columns
df.rename(columns={
    "PassengerId": "ID",
    "Name":"Full Name"}, inplace=True)

print(df.head(10))