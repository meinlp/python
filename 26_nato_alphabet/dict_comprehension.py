# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)


students_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# for (key, value) in students_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)

# loop through the dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.score >= 60:
        print("sup")