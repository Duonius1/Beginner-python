#with open("file1.txt") as file1:
#    numbers_1 = file1.readlines()
#with open("file2.txt") as file2:
#    numbers_2 = file2.readlines()
#
#
#result = [int(num) for num in numbers_1 if num in numbers_2]
#
#print(result)

#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#split_sentence = sentence.split()
#result = {word: len(word) for word in split_sentence}
#print (result)

#weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
#weather_f = {day: (temp * 9 / 5 + 32) for (day, temp) in weather_c.items()}
#
#print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
#   print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# Loop through a data frame
#for (key, value) in student_data_frame.items():
#    print(value)

# Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#        if row.student == "Angela":
#            print(row.score)
