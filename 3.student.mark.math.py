import math
import numpy as np


class student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob

    def getStudentName(self):
        return self.name

    def getNameAndId(self):
        print("\t", (self.id).ljust(15, " "),
              (self.name).ljust(20, " "), end="")

    @property
    def printList(self):
        print((self.id).ljust(15, " "), (self.name).ljust(20, " "), self.dob)


class course(student):
    def __init__(self, _id, _name, _studentList, _markList):
        self.id = _id
        self.name = _name
        self.studentList = _studentList
        self.markList = _markList

    @property
    def printCoursesList(self):
        print((self.id).ljust(15, " "), self.name)

    def getCourseName(self):
        return self.name

    def printList(self, i):
        print(self.markList[i])


students = []
courses = []
marks = []

# Input number of students in a class
numOfStudents = int(input("Number of students: \n"))

# Input student information: id, name, DoB
for i in range(0, numOfStudents):
    print(f"Student {i+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    dob = input("Dob (format: dd/mm/yy): ")
    students.append(student(id, name, dob))

    i += 1

# Input number of courses
numOfCourses = int(input("Number of courses: \n"))

# Input course information: id, name
for j in range(0, numOfCourses):
    print(f"Course {j+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    studentsList = students

    courses.append(course(id, name, studentsList, 0))

    j += 1

courseSelection = 1
while courseSelection in range(1, numOfCourses + 1):
    courseSelection = int(
        input(
            f"To enter marks for student, select a course (from 1 to {numOfCourses}, type 0 to quit): "
        )
    )

    if courseSelection == 0:
        break

    for k in range(0, numOfStudents):
        print(f"Mark for student {students[k].getStudentName()}: ")
        _mark = round(float(input()), 1)
        marks.append(_mark)

        k += 1

    courses[courseSelection - 1].markList = marks[
        (courseSelection - 1) * numOfStudents: courseSelection * numOfStudents
    ]


def listCourses():
    print("Id".ljust(15, " "), "Name")
    for j in range(0, numOfCourses):
        courses[j].printCoursesList


def listStudents():
    print("Id".ljust(15, " "), "Name".ljust(20, " "), "Dob")
    for i in range(0, numOfStudents):
        students[i].printList


def showMarks():
    for j in range(0, numOfCourses):
        print(courses[j].getCourseName())
        print("\tId".ljust(15, " "), "Name".ljust(20, " "), "Mark")
        for i in range(0, numOfStudents):
            students[i].getNameAndId()
            courses[j].printList(i)


def showAverageMarks():
    print("Average mark: ")
    marksLength = len(marks)
    averageMarks = []
    for i in range(0, numOfStudents):
        averageMark = np.average(marks[i:marksLength:numOfStudents])
        averageMarks.append(averageMark)
    print(sorted(averageMarks, reverse=True))


choices = 1

# Listing functions
while choices:
    choices = int(
        input("1. Courses list\n2. Student list\n3. Student' marks\n4. Student average marks\nElse. Exit\n"))

    # List courses
    if choices == 1:
        listCourses()

    # List students
    elif choices == 2:
        listStudents()

    # Show student marks for a given course
    elif choices == 3:
        showMarks()

    # Show student average marks
    elif choices == 4:
        showAverageMarks()

    else:
        break