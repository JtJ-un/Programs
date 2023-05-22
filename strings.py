students = "John 1, Jane 2, Bob 3, Alice 4"
students_list = students.split(", ")

for student in students_list:
    name, roll_number = student.split()
    print(f"Name: {name}, Roll Number: {roll_number}")
