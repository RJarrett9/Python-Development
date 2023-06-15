"""
Ryan Jarrett
Dean and Honor Test
This app checks to see if a student qualifies to be on either the Dean's List or the Honor Roll
firstName is mostly there for coherence in printing student names
lastName is to check when the program needs to terminate
studentGPA is to find out which list the student made, if any
"""

firstName = input("Enter student's first name: ")
lastName = input("Enter student's last name or ZZZ to quit: ")
studentGPA = float(input("Enter student's GPA: "))

while lastName != "ZZZ":
    if studentGPA >= 3.5:
        print(firstName, lastName, "has made the Dean's List!")
    elif studentGPA >= 3.25:
        print(firstName, lastName, "has made the Honor Roll!")
    else:
        print(firstName, lastName, "did not make either list.")

    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name or ZZZ to quit: ")
    if lastName != "ZZZ":
        studentGPA = float(input("Enter student's GPA: "))