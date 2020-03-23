# James L. Romero III
# Email: jaromero@chapman.edu
# CPSC 408
#Professor: Rene German


import sqlite3 as sq
from Student import Student
import sys
from exitstatus import ExitStatus

#Connects to database
conn = sq.connect('/Users/jlloyd/Database/StudentDB.db')
c = conn.cursor()

#Displays all students
def allStudents():
    print("------Display ALL Students------")
    c.execute("SELECT * FROM Student")
    data = (c.fetchall())
    print("|StudentID | First Name | Last Name | GPA | Major | Faculty Advisor |")
    for row in data:
        print(row)
    cmd = input("Would you like to return to the main menu(Y/N)?")
    if cmd.upper() == 'Y':
        GUI()
    elif cmd.upper() == 'N':
        print("Thank you, have a wonderful day!")
        conn.commit()
        conn.close()
        sys.exit(ExitStatus.success)

#Creates a student
def createStudent():
    print("------Create Student------")
    studentID = input("Enter StudentID: ")
    firstname = input("Enter Students First Name: ")
    lastname = input("Enter Students Last Name: ")
    gpa = input("Enter Students GPA: ")
    major = input("Enter Students Major: ")
    facultyadvisor = input("Enter Students Faculty Advisor: ")
    isdeleted = False
    stdt = Student(studentID, firstname, lastname, gpa, major, facultyadvisor, isdeleted)
    c.execute("INSERT INTO Student (StudentID, FirstName,LastName, GPA, Major, FacultyAdvisor, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ? )",
                   (stdt.get_studentID(), stdt.get_firstname(), stdt.get_lastname(), stdt.get_GPA(), stdt.get_Major(), stdt.get_facultyAdvisor(), False))
    print("Successfully Created", firstname, lastname)
    cmd = input("Would you like to return to the main menu(Y/N)?")
    if cmd.upper() == 'Y':
        GUI()
    elif cmd.upper() == 'N':
        print("Thank you, have a wonderful day!")
        conn.commit()
        conn.close()
        sys.exit(ExitStatus.success)

#Updates students records
def updateStudentRecord():
    print("-------Update Student's Record--------")
    while True:
        try:
            studentID = input("ENTER STUDENT_ID: ")
            c.execute("SELECT * FROM Student WHERE StudentId = ? ", studentID)
            stud = c.fetchall()
            print("[StudentID | FirstName | LastName | GPA |  Major | Faculty Advisor]")
            for row in stud:
                print(row)
            userChoice = int(input("Update Student By:\n1)Last Name\n2)GPA\n3)Major\n4) Faculty Advisor\nSELECT VALID OPTION(1-4)"))
            if userChoice == 1:
                userInput = input("Update Last Name: ")
                c.execute("UPDATE Student SET LastName = ? WHERE StudentID = ?", (userInput, studentID))
            elif userChoice == 2:
                userInput = float(input("Update Students GPA: "))
                c.execute("UPDATE Student SET GPA = ? WHERE StudentID = ?", (userInput, studentID))
            elif userChoice == 3:
                userInput = input("Update Students Major: ")
                c.execute("UPDATE Student SET Major = ? WHERE StudentID = ?", (userInput, studentID))
            elif userChoice == 4:
                userInput = input("Update Students Faculty Advisor: ")
                c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID = ?", (userInput, studentID))
            else:
                print("That was not a valid option.")
                updateStudentRecord()
        except ValueError:
            print("Incorrect input, try again")
        cmd = input("Would you like to return to the main menu(Y/N)?")
        if cmd.upper() == 'Y':
            GUI()
        elif cmd.upper() == 'N':
            print("Thank you, have a wonderful day!")
            conn.commit()
            conn.close()
            sys.exit(ExitStatus.success)

#Search within the database based on category, ie Major, GPA, and Faculty Advisor
def searchDirectory():
    print("-------Search Directory------\n")
    while True:
        try:
            search = int(input("Search by: \n(1)Major\n(2)GPA\n(3)Faculty Advisor\nSELECT VALID OPTION(1-3)"))
            if search == 1:
                category = input("Select all Students by Major: ")
                c.execute("SELECT * FROM Student WHERE Major = ?", (category,))
                data = c.fetchall()
                print("[StudentID | FirstName | LastName | GPA | *Major | Faculty Advisor]")
                for row in data:
                    print(row)
            elif search == 2:
                category = input("Select all Students by GPA: ")
                c.execute("SELECT * FROM Student WHERE GPA = ?", (category,))
                data = c.fetchall()
                print("[StudentID | FirstName | LastName | *GPA |  Major | Faculty Advisor]")
                for row in data:
                    print(row)
            elif search == 3:
                category = input("Select all Students by Faculty Advisor: ")
                c.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", (category,))
                data = c.fetchall()
                print("[StudentID | FirstName | LastName | *GPA |  Major | Faculty Advisor]")
                for row in data:
                    print(row)
            else:
                print("That was not a valid option.")
                searchDirectory()
        except ValueError:
            print("Incorrect input, try again")
        cmd = input("Would you like to return to the main menu(Y/N)?")
        if cmd.upper() == 'Y':
            GUI()
        elif cmd.upper() == 'N':
            print("Thank you, have a wonderful day!")
            conn.commit()
            conn.close()
            sys.exit(ExitStatus.success)

#Intiates a soft delete to a student in the database
def deleteStudent():
    studentID = input("What is the student's ID number? ")
    c.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1, studentID,))
    conn.commit()  # commit changes
    print("Student Deleted")


#Main Menu
def GUI():
    print("\n")
    print("|Chapman University's Student Database|\n")
    print("Enter the option number you wish to execute: ")
    print("0) Display all students and their attributes")
    print("1) Create New Student")
    print("2) Update Student Record")
    print("3) Search for a specific student")
    print("4) Remove a Students from Database")
    print("99) Exit")
    while True:
        try:
            selection = int(input("Enter a valid selection from the menu above: "))
            if selection == 0:
                allStudents()
            elif selection == 1:
                createStudent()
            elif selection == 2:
                updateStudentRecord()
            elif selection == 3:
                searchDirectory()
            elif selection == 4:
                deleteStudent()
            elif selection == 99:
                print("Thank you, have a wonderful day!")
                conn.commit()
                conn.close()
                sys.exit(ExitStatus.success)
            else:
                print("That was not a valid option.")
                break;
        except ValueError:
            print("Incorrect input, try again")

#main function to give code ability to run
if __name__ == "__main__":
    GUI()
