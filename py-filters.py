grades = ['A', 'F', 'B', 'C', 'F', 'B', 'D', 'A']

def removeFails(grade):
    return grade == 'F'

print(list(filter(removeFails, grades)))
