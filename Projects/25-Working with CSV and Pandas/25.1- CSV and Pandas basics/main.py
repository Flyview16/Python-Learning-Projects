import pandas

# Read data from csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get data from primary fur color column
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Convert extracted data to csv file
data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel colour count")


