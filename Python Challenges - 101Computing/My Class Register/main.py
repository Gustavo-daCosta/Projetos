presentCounter = counter = absentCounter = 0
pupils = ['Joe', 'Sonny', 'Yassine', 'Emma', 'Ines', 'Satveer', 'Lily', 'Reuben', 'Lucy', 'Tom']

for name in pupils:
    present = str(input(f'The student {name} is present? [y or n]: '))
    counter += 1
    if present == 'y':
        presentCounter += 1
    else:
        absentCounter += 1

print(f'''Total number of students: {counter} students
Present students: {presentCounter} students
Absent students: {absentCounter} students''')