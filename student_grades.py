student_grades ={
    "Alice":[85, 90, 92],
    "Bob":[88, 89, 92, 95],
    "Charlie":[78, 80],
    "David":[95, 96, 98]
}
for student, grades in student_grades.items():
    average_grade = sum(grades)/len(grades)
    print(student, average_grade)
