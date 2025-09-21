# Exercise 6: Celebrate Students
#
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings.
# For example: ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

def create_awesome_students():
    # your code here
    students = ['Berthany', 'Jankle', 'Carble']
    is_awesome = [f"{student} is awesome!" for student in students]
    return is_awesome

# Call the function and print the result
print('Exercise 6:', create_awesome_students())
