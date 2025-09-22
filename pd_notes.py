import pandas as pd
df = pd.DataFrame

df = pd.DataFrame(
       {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
   

# print(df)

print(df["Age"].max()) #max age of passengers

pets = pd.Series(['dog', 'cat', 'frog', 'owl', 'rat', 'cobra'], name = "Pets")

df["Colors"] = ["blue", "green", "yellow"]

print(df)
