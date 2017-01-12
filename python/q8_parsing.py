import sys
import re

def main():
    if len(sys.argv) < 2:
        print 'This program requires the football.csv file'
        exit(1)
    football_csv = sys.argv[1] #returns the file 'football.csv'

    club_dict = {}
    difference_list = []

    with open(football_csv, 'r') as file_object:
        lines_read = file_object.readlines() #returns a list of strings
        for lines in lines_read[1:]:
            m = re.search('(.*),.*,.*,.*,.*,(.*),(.*),.*', lines)
            club_name = (m.group(1)) #returns a string
            difference = int(m.group(2)) - int(m.group(3)) #returns integer

            if difference not in club_dict:
                club_dict[difference] = [club_name] #key=int diff. ; value=club
                difference_list.append(difference) #put diff. values into list
                #to call the min function that takes in a list with lambda.
            else:
                club_dict[difference].append(club_name)

        print club_dict[min(difference_list, key=lambda x:abs(x-0))][0]
        # print 'corresponding value of the key that\'s the closest int from 0.'

if __name__ == '__main__':
    main()
