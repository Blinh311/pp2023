# Initialize empty lists and dictionaries
students = []
courses = []
marks = {}

# Function to input student information
def input_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    students.append((id, name, dob))

# Function to input course information
def input_course():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((id, name))

# Function to input marks for a given course and student
def input_marks():
    course_id = input("Enter course ID: ")
    student_id = input("Enter student ID: ")
    mark = float(input("Enter marks for {}: ".format(courses[courses.index((course_id,))][1])))
    marks.setdefault(course_id, {})[student_id] = mark

# Function to list courses
def list_courses():
    print("Courses:")
    for course in courses:
        print("- {}: {}".format(course[0], course[1]))

# Function to list students
def list_students():
    print("Students:")
    for student in students:
        print("- {}: {}".format(student[0], student[1]))

# Function to show student marks for a given course
def show_marks():
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("No marks found for course")
        return
    print("Marks for {}:".format(courses[courses.index((course_id,))][1]))
    for student_id, mark in marks[course_id].items():
        student_name = students[students.index((student_id,))][1]
        print("- {}: {}".format(student_name, mark))

# Main program
while True:
    print("""
    1. Input student information
    2. Input course information
    3. Input marks for a student in a course
    4. List courses
    5. List students
    6. Show student marks for a course
    7. Exit
    """)
    choice = input("Enter choice: ")
    if choice == "1":
        input_student()
    elif choice == "2":
        input_course()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        show_marks()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
