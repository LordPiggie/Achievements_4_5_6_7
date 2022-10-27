#This program creates a course list and records information for a potential student

courseInfo = { #This dictionary contains the course list

    'MATH1001   ' : 'Math',

    'ENGL1001   ' : 'English',

    'SCNC1001   ' : 'Science',

    'HIST1001   ' : 'History'

}

def printCourse(): #This function prints the course list

    for option in courseInfo:

        print(option, courseInfo[option])

print('Hello welcome to Course Registration,\nto register for courses please accuratly answer the below questions.\n\n') #Greeting message

#Below the user inputs information which is stored in a dictionary below

firstName = input('What is your first name? ') 

lastName = input('What is your last name? ')

studentID = input('What is your student number?: ')

identification = { #This is the dictonary that stores a students information

    'First name:    ' : firstName,

    'Last Name:     ' : lastName,

    'Student Number:' : studentID

}

def printIdentification(): #This function can print the students details.

    for course in identification:

        print(course, identification[course])

print('\nWhich courses would you like to select?\n')

printCourse()

courseSelection = input('\n[Please input your desired course codes seperated by commas]:\n ') #This records the students desired classes

courseList = courseSelection.split(',') #This splits the information so that the while loops can interperet the info

print('\n\nYour registration details are below:\n')

printIdentification()

print('\nYour course list is:\n')

#The below while loops decifer the users input and print the courses the student has registered for.

while "MATH1001" in courseList:

    mathOutput = courseInfo['MATH1001   ']

    print('MATH1001', mathOutput)

    break

while "ENGL1001" in courseList:

    englishOutput = courseInfo['ENGL1001   ']

    print('ENGL1001', englishOutput)

    break

while "SCNC1001" in courseList:

    scienceOutput = courseInfo['SCNC1001   ']

    print('SCNC1001', scienceOutput)

    break

while "HIST1001" in courseList:

    historyOutput = courseInfo['HIST1001   ']

    print('HIST1001', historyOutput)

    break

print('\nThank you and enjoy your time at school') #thank you message