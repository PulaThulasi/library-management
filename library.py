books = []

while True:
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available in the library")
        else:
            print("Available Books:")
            for b in books:
                print(b)

    elif choice == "3":
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found")

    elif choice == "4":
        print("Thank you for using Library System")
        break

    else:
        print("Invalid choice")