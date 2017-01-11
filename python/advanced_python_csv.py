import re
answer = []
with open('./faculty.csv', 'r') as file_object:
    lines_read = file_object.readlines()
    for lines in lines_read:
        m = re.search('.*,.*,.*,(.*)', lines)
        email = m.group(1)
        answer.append(email)
    answer.remove(' email')

    solution = open('emails.csv', 'w')
    for each in answer:
        solution.write(each + '\n')
