programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
                         }
print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "the action of doing something over and over"
empty_dictionary ={}
print(programming_dictionary)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for key in student_scores:
    value_to_check = student_scores[key]
    if value_to_check < 70:
        student_grades[key] = "Fail"
    elif 70 < value_to_check <= 80:
        student_grades[key] = "Acceptable"
    elif 80 < value_to_check <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 90 < value_to_check <= 100:
        student_grades[key] = "Outstanding"

print(student_grades)
print(student_scores)
