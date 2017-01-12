import re
faculty_dict = {}

with open('./faculty.csv', 'r') as file_object:
    lines_read = file_object.readlines()

    for lines in lines_read[1:]:
        m = re.search('(\w+),(.*),(.*),(.*)', lines)
        surname = m.group(1)
        degree = m.group(2)
        title = m.group(3)
        email = m.group(4)
        if surname not in faculty_dict:
            faculty_dict[surname] = [[degree, title, email]]
        else:
            faculty_dict[surname].append([degree, title, email])
    count = 0
    for stuff in faculty_dict.keys():
        if count < 3:
            count += 1
            print str(stuff) + ': ' + str(faculty_dict[stuff])
        else:
            break

professor_dict = {}

with open('./faculty.csv', 'r') as file_object:
    lines_read = file_object.readlines()
    for lines in lines_read[1:]:
        m = re.search('(.*),(.*),(.*),(.*)', lines)
        full_name = m.group(1)
        degree = m.group(2)
        title = m.group(3)
        email = m.group(4)
        split_names = full_name.split()
        first_name = split_names[0]
        last_name = split_names[-1]
        professor_dict[(first_name, last_name)] = [[degree, title, email]]
        #tuple creation, must initialize by assigning something to it

    count = 0
    for stuff in professor_dict.keys():
        if count < 3:
            count += 1
            print str(stuff) + ': ' + str(professor_dict[stuff])
        else:
            break

new_dict = {}

with open('./faculty.csv', 'r') as file_object:
    lines_read = file_object.readlines()
    for lines in lines_read[1:]:
        m = re.search('(.*),(.*),(.*),(.*)', lines)
        full_name = m.group(1)
        degree = m.group(2)
        title = m.group(3)
        email = m.group(4)
        split_names = full_name.split()
        first_name = split_names[0]
        last_name = split_names[-1]
        new_dict[(last_name, first_name)] = [[degree, title, email]]
        #tuple creation, must initialize by assigning something to it
    dict_keys = sorted(new_dict, key=lambda x: x[0]) #this returns a list

    for i in dict_keys:
        print str(i) + ': ' + str(new_dict[i])
