#Question 1
import re
#file_object = open('./faculty.csv', 'r')
answer = {}
with open('./faculty.csv', 'r') as file_object: #file_object is variable, and
#it represents the file i want to open as an OBJECT
        lines_read = file_object.readlines()
        for lines in lines_read:
            m = re.search('.*,(.*),.*,.*', lines) #put regex as string
            #looking for something, it's
            #('what you're looking for', where you're looking)
            degrees_grouped = m.group(1)
            no_periods = degrees_grouped.replace('.', '')
            # print no_periods
            splitted = no_periods.split()
            # print splitted
            for degree in splitted:
                # answer['PhD'] = 'yes'
                if degree not in answer:
                    answer[degree] = 1
                else:
                    answer[degree] += 1
            if 'degree' in answer:
                del answer['degree']
            if '0' in answer:
                del answer['0']
        print answer

#Question 2
answer = {}
with open('./faculty.csv', 'r') as file_object: #file_object is variable, and
#it represents the file i want to open as an OBJECT
        lines_read = file_object.readlines()
        for lines in lines_read:
            m = re.search('.*,.*,(.*),.*', lines) #put regex as string
            #looking for something, it's
            #('what you're looking for', where you're looking)
            title = m.group(1)
            # print titles_grouped
            if title not in answer:
                answer[title] = 1
            else:
                answer[title] += 1
        if 'title' in answer:
            del answer['title']
        print answer

#Question 3
answer = []
with open('./faculty.csv', 'r') as file_object: #file_object is variable, and
#it represents the file i want to open as an OBJECT
        lines_read = file_object.readlines()
        for lines in lines_read:
            m = re.search('.*,.*,.*,(.*)', lines) #put regex as string
            #looking for something, it's
            #('what you're looking for', where you're looking)
            email = m.group(1)
            answer.append(email)
        answer.remove(' email')
        print answer

#Question 4
answer = set()
with open('./faculty.csv', 'r') as file_object: #file_object is variable, and
#it represents the file i want to open as an OBJECT
        lines_read = file_object.readlines()
        for lines in lines_read:
            m = re.search('.*,.*,.*,.*@(.*)', lines) #put regex as string
            #looking for something, it's
            #('what you're looking for', where you're looking)
            if m:
                emails_grouped = m.group(1)
                answer.add(emails_grouped)
                length = len(answer)
        print list(answer)
        print length
