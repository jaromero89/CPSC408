#Citation: https://www.codesdope.com/python-your-class/
class Student():
    def __init__(self, Studentid, FirstName, LastName,
                 GPA, Major, FacultyAdvisor, isDeleted):
        self.studentid = Studentid
        self.firstname = FirstName
        self.lastname = LastName
        self.gpa = GPA
        self.major = Major
        self.facultyadvisor = FacultyAdvisor
        self.isdeleted = isDeleted

    def get_studentID(self):
     return self.studentid

    def get_firstname(self):
     return self.firstname

    def get_lastname(self):
     return self.lastname

    def get_GPA(self):
     return self.gpa

    def get_Major(self):
     return self.major

    def get_facultyAdvisor(self):
     return self.facultyadvisor

    def isDeleted(self):
     return self.isdeleted