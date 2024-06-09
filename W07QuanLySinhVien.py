class Student:
    def __init__(self, student_id, name, dob, hometown, major, class_name):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.hometown = hometown
        self.major = major
        self.class_name = class_name

class Student_List:
    def __init__(self):
        self.students = []

    def view_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}, Hometown: {student.hometown}, Major: {student.major}, Class: {student.class_name}")

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, student_id, new_student):
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                self.students[index] = new_student
                print("Student information updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[index]
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def search_student(self, keyword):
        found = False
        for student in self.students:
            if (keyword.lower() in student.name.lower()) or (keyword.lower() in student.student_id.lower()):
                print(f"Student ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}, Hometown: {student.hometown}, Major: {student.major}, Class: {student.class_name}")
                found = True
        if not found:
            print("No student found with the given keyword.")

    def sort_students(self):
        self.students.sort(key=lambda x: x.name)

# Example usage:
# Create some students
student1 = Student("001", "Alice", "1999-01-01", "New York", "Computer Science", "CS101")
student2 = Student("002", "Bob", "2000-02-02", "Los Angeles", "Mathematics", "MATH201")
student3 = Student("003", "Bobble", "2000-02-02", "Los Angeles", "Mathematics", "MATH201")

# Create a student list
student_list = Student_List()

# Add students to the list
student_list.add_student(student1)
student_list.add_student(student2)
student_list.add_student(student3)

# View all students
print("All students:")
student_list.view_students()

# Update a student's information
new_student_info = Student("002", "Bobby", "2000-02-02", "Los Angeles", "Mathematics", "MATH201")
student_list.update_student("002", new_student_info)
print("Updated students list:")
student_list.view_students()

# Delete a student
student_list.delete_student("001")
print("Students list after deletion:")
student_list.view_students()

# Search for a student
print("Searching for students with keyword 'bob':")
student_list.search_student("bob")

# Sort students by name
print("Students list after sorting by name:")
student_list.sort_students()
student_list.view_students()
