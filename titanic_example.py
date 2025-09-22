import pandas as pd
import requests
import os


url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
filename = "titanic.csv"
response = requests.get(url)

# Save content to a CSV file
if not os.path.exists(filename):
    response = requests.get(url)
    with open("titanic.csv", "wb") as file:
      file.write(response.content)
    print("CSV downloaded successfully!")
else:
  print((f'{filename} already exists.'))

titanic = pd.read_csv("titanic.csv")

# print(titanic.head(8))

"""Pax over 35"""
ages = titanic["Age"]
above_35 = titanic[titanic["Age"] > 35]
#print(ages.head())
print(above_35.head())


"""Passengers w/ longest names"""

idx = titanic["Name"].str.len().idxmax()
print(titanic.loc[idx, "Name"])


"""Average age of the Pax"""
print(titanic["Age"].mean())

"""median age and ticket fare"""
titanic[["Age", "Fare"]].median()

titanic[["Age", "Fare"]].describe()