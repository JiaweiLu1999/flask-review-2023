import pandas as pd


def count(dataframe, column_name, color):
    return dataframe[dataframe[column_name] == color][column_name].count()


df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
COLUMN_NAME = "Primary Fur Color"
colors = ["Gray", "Cinnamon", "Black"]

data_dict = {
    "Fur Color": colors,
    "Count": []
}

for c in colors:
    cnt = count(df, COLUMN_NAME, c)
    data_dict["Count"].append(cnt)

new_df = pd.DataFrame(data_dict)
new_df.to_csv("new_squirrel_data.csv")
