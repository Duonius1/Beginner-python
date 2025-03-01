import pandas

#data = pandas.read_csv("weather_data.csv")
#type(data)
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(temp_list)

#print(data["temp"].mean())
#print(data["temp"].max())

#Get Data in Columns
#print(data["condition"])
#print(data.condition)

#Get Data in Rows

#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#print(monday.temp * 9/5 + 32)

#Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
