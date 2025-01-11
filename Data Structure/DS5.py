# Define a list of student tuples (name, age, grade)
students = [
    ("John Doe", 20, 85),
    ("Jane Smith", 22, 90),
    ("Alice Johnson", 21, 75),
    ("Bob Brown", 23, 92),
    ("Charlie Davis", 24, 88)
]

# Function to print students with grades above a certain value
def print_students_above_grade(students):
    # Ask the user to input a grade threshold
    threshold = int(input("Enter the grade threshold: "))
    
    print(f"Students with grades above {threshold}:")
    for student in students:
        name, age, grade = student  # Unpack the tuple
        if grade > threshold:
            print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Call the function to print students with grades above the user's threshold
print_students_above_grade(students)
