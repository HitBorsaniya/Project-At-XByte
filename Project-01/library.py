from crud import *
from services import *

def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Search Book")
        print("8. Exit")

        ch = input("Enter choice: ")

        if ch == "1": add_book()
        elif ch == "2": view_books()
        elif ch == "3": update_book()
        elif ch == "4": delete_book()
        elif ch == "5": issue_book()
        elif ch == "6": return_book()
        elif ch == "7": search_book()
        elif ch == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
