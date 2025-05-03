# Define the Student Class
class Student:
    def __init__(self, name, subject_marks):
    # Intialize name and a dictinary of subject marks
        self.name = name
        self.subject_marks = subject_marks

    def calculate_average(self):
        # Calculate the average marks
        total = sum(self.subject_marks.values())
        count = len(self.subject_marks)
        return total / count if count > 0 else 0
    
    def calculate_grade(self):
        # Assign grade based on average marks
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def display(self):
        # Display the student's details
        print(f"\nName: {self.name}")
        print("Marks:")
        for subject, mark in self.subject_marks.items():
            print(f" {subject}: {mark}")
        avg = self.calculate_average()
        grade = self.calculate_grade()
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")


# Function to get one student's data from user input
def get_student_from_input():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects:"))
    subject_marks = {}

    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        mark = float(input(f"Enter mark for {subject}: "))
        subject_marks[subject] = mark
    
    return Student(name, subject_marks)


# Main program
def main():
    students = [] # List to store multiple Student objects
    num_students = int(input("Enter number of students: "))

    for _ in range(num_students):
        print("\nEnter details for student:")
        student = get_student_from_input()
        students.appendS(student)
    
    # Display details for all students
    print("\n--- Student Details ---")
    for student in students:
        student.display()


# Run the main program
if __name__ == "__main__":
    main()