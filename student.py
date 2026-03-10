# Student Record System

students = {}

while True:
    print("\n----- Student Record Menu -----")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print("Name:", name, "| Marks:", marks)

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")