# Write a function that takes a dictionary with information about students. Return info
# about the student with_highest average score
def calculate_average(scores):
    return sum(scores) / len(scores)

def student_with_highest_average(students):
    highest_avg = 0
    top_student = None

    for student_id, info in students.items():
        average = calculate_average(info['scores'])

        if average > highest_avg:
            highest_avg = average
            top_student = info

    return top_student

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

top_student = student_with_highest_average(students_info)

print(top_student)
