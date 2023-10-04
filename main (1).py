def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x['cgpa'], reverse=True)
    return sorted_students

# Define some sample student data
students = [
    {'name': 'Alice', 'roll_number': 'A001', 'cgpa': 3.9},
    {'name': 'Bob', 'roll_number': 'B002', 'cgpa': 3.7},
    {'name': 'Charlie', 'roll_number': 'C003', 'cgpa': 3.5},
    {'name': 'David', 'roll_number': 'D004', 'cgpa': 3.8},
]

# Test the function with the sample data
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")
