# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.

students_scores = (("Alice", 88), ("Anna", 92), ("Ani", 85))

highest_score = max(students_scores, key=lambda student: student[1])

print(f"The highest scoring student is {highest_score[0]} with a score of {highest_score[1]}.")