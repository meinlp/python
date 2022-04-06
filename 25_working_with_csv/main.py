import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# print(data[data["Primary Fur Color"] == "Black"]["Unique Squirrel ID"])
gray     = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black    = len(data[data["Primary Fur Color"] == "Black"])
# print(gray, cinnamon, black)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_colors.csv")

