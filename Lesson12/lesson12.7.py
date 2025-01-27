# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

def min_of_ages(student_info):
    youngest_student = None
    youngest_age = float('inf')

    for student, info in student_info.items():
        age = info['age']
        if age < youngest_age:
            youngest_age = age
            youngest_student = info

    return youngest_student

students_info = {
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6],
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10],
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9],
    },
}

print(min_of_ages(students_info))
