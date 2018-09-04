grades = ['A', 'F', 'B', 'C', 'F', 'B', 'D', 'A']

def removeFails(grade):
    return grade != 'F'

print(list(filter(removeFails, grades)))

new_grades = []
for grade in grades:
    if removeFails(grade):
        new_grades.append(grade)

print(new_grades)


print([grade for grade in grades if removeFails(grade)])