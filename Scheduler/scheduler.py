import math
import MySQLdb
import re


# would normal grab degree information here but instead I am faking it for testing
degree = "CS"
courses = ['CS 1000', 'CS 1121', 'CS 1122', 'CS 1142', 'CS 2311', 'CS 2321', 'CS 3000', 'CS 3141', 'CS 3311', 'CS 3331',
           'CS 3411', 'CS 3421', 'CS 3425', 'CS 4121', 'CS 4321', 'MA 1160', 'MA 2160', 'MA 3710', 'MA 2330', 'UN 1025',
           'UN 1015']
complete = ['CS 1000', 'CS 1121', 'MA 1160', 'UN 1015']


def check_prereqs(input, prereqLength, prereqChain):
    input = input.replace("(C)", "")
    # deal with parentheses
    exp = re.findall("\(([^)]+)\)", input)
    if exp:
        for group in exp:
            group_with_parentheses = "(" + group + ")"
            input = input.replace(group_with_parentheses, str(check_prereqs(group, prereqLength, prereqChain)))
            # print(str)

    # deal with 'and's
    groups = input.split(" and ")
    value = math.nan;
    for group in groups:
        # inside of ands deal with 'or's
        t = group.split(" or ")
        min = math.nan
        minPrereq = "null"
        for prereq in t:
            # or logic
            if prereq in prereqLength:
                if not math.isnan(prereqLength[prereq]) and math.isnan(min):
                    min = prereqLength[prereq]
                    minPrereq = prereq
                elif not math.isnan(prereqLength[prereq]) and prereqLength[prereq] < min:
                    min = prereqLength[prereq]
                    minPrereq = prereq
            elif prereq.isdigit():
                if math.isnan(min):
                    min = int(prereq)
                    minPrereq = "null"
                elif int(prereq) < min:
                    min = int(prereq)
                    minPrereq = "null"

        if minPrereq != "null" and minPrereq not in prereqChain:
            prereqChain.append(minPrereq)

        # and logic
        if math.isnan(min):
            value = math.nan
            break
        elif math.isnan(value):
            value = min
        elif value < min:
            value = min
    return value

prereqLength = {}
prereqChain = {}
for course in courses:
    prereqLength[course] = math.nan
    prereqChain[course] = []

db = MySQLdb.connect("141.219.214.79", "degreePlanner", "teamsoftware", "TSP")

cursor = db.cursor()

prereqs = {}
# get prereqs of every course
for course in courses:
    query = "SELECT course_num, prereq from courses WHERE course_num='" + course + "'"
    cursor.execute(query)
    data = cursor.fetchall()
    prereqs[data[0][0]] = data[0][1]
    if data[0][1] == 'null' or course in complete:
        prereqLength[course] = -1
db.close()

change = True
while change:
    change = False
    for key, value in prereqLength.items():
        if math.isnan(prereqLength[key]):
            val = check_prereqs(prereqs[key], prereqLength, prereqChain[key])
            if not math.isnan(val):
                change = True
                prereqLength[key] = int(val) + 1
        """
        if math.isnan(value):
            #if prereq met then set it to highest prereq plus 1
            #change becomes true
            #if the prereq only contains 'or's then check for any singular class
            if not re.search('and', prereqs[key]):
                t = prereqs[key].split(" or ")
                min = math.nan
                for prereq in t:
                    #if the prereq is need/taken then update min
                    if prereq in prereqLength:
                        if not math.isnan(prereqLength[prereq]) and math.isnan(min):
                            min = prereqLength[prereq]
                        elif not math.isnan(prereqLength[prereq]) and prereqLength[prereq] < min:
                            min = prereqLength[prereq]
                if not math.isnan(min):
                    change = True
                    prereqLength[key] = min + 1

            # if the prereq only contains 'and's then check for every class
            elif not re.search('or', prereqs[key]):
                t = prereqs[key].split(" and ")
                max = math.nan
                for prereq in t:
                    # if the prereq is need/taken then update min
                    if prereq in prereqLength:
                        if math.isnan(prereqLength[prereq]):
                            max = math.nan
                            break
                        if not math.isnan(prereqLength[prereq]) and math.isnan(max):
                            max = prereqLength[prereq]
                        elif not math.isnan(prereqLength[prereq]) and prereqLength[prereq] > max:
                            max = prereqLength[prereq]
                if not math.isnan(max):
                    change = True
                    prereqLength[key] = max + 1

            #singular class
            elif prereqs[key] in prereqLength and not math.isnan(prereqLength[prereqs[key]]):
                prereqLength[key] = prereqLength[prereqs[key]] + 1

            #mix of 'and's and 'or's

"""
change = True
while change:
    change = False
    for key, value in prereqChain.items():
        for course in value:
            if course in prereqChain.keys():
                for prereq in prereqChain[course]:
                    if prereq not in prereqChain[key]:
                        change = True
                        prereqChain[key].append(prereq)

maxPrereqChain = 0
for value in prereqLength.values():
    if value > maxPrereqChain:
        maxPrereqChain = value
result = "";
for i in range(maxPrereqChain + 1):
    i = maxPrereqChain - i
    for key, value in prereqLength.items():
        if value == i:
            if key not in complete:
                print(key, ": ", value)
                result = result+key+": "+str(value)+"<br>";
                for v in prereqChain[key]:
                    print("   ", v)
                    result=result+"   "+v+"<br>";

print(result)
