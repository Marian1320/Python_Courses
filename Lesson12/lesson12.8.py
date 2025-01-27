# Write a function that takes a dictionary with information about students. Return info
# about the student with_highest average score

def max_of_average_score(student_info):
    student_with_highest_average_score = None
    highest_average_score = float('inf')

    for student, info in student_info.items():
        average_score = sum(info['scores']) / len(info['scores'])
        if average_score < highest_average_score:
            highest_average_score = sum(info['scores']) / len(info['scores'])
            student_with_highest_average_score = info

    return student_with_highest_average_score

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

print(max_of_average_score(students_info))