from db import get_connection
from utils import captcha_check, validate_name
from datetime import datetime

FINE_PER_DAY = 10

# ------------------ ISSUE BOOK ------------------
def issue_book():
    if not captcha_check():
        print("CAPTCHA failed!")
        return

    con = get_connection()
    cur = con.cursor()

    book_id = input("Enter Book ID to issue (DB ID): ")
    student = input("Enter student name: ")

    if not validate_name(student):
        print("Invalid student name!")
        return

    # Check availability
    cur.execute("SELECT status FROM books WHERE id=%s", (book_id,))
    result = cur.fetchone()
    if not result:
        print("Book not found!")
        return

    status = result[0]

    if status != "Available":
        print("Book is already issued. Adding to reservation queue...")
        reserve_book(book_id, student)
        return

    cur.execute("UPDATE books SET status=%s WHERE id=%s", (f"Issued to {student}", book_id))
    cur.execute("INSERT INTO issued_books (book_id, student_name) VALUES (%s, %s)", (book_id, student))

    con.commit()
    print("Book issued successfully!")
    con.close()


# ------------------ RETURN BOOK + FINE ------------------
def return_book():
    con = get_connection()
    cur = con.cursor()

    book_id = input("Enter Book ID to return: ")

    # Fetch issue record
    cur.execute("SELECT issue_date FROM issued_books WHERE book_id=%s ORDER BY issue_id DESC LIMIT 1", (book_id,))
    record = cur.fetchone()

    if not record:
        print("This book was not issued.")
        return

    issue_date = record[0]
    now = datetime.now()
    days = (now - issue_date).days

    fine = 0
    if days > 7:
        fine = (days - 7) * FINE_PER_DAY

    print(f"Book is late by {days} days. Fine = ₹{fine}")

    # Update status
    cur.execute("UPDATE books SET status='Available' WHERE id=%s", (book_id,))
    con.commit()

    print("Book Returned Successfully!")
    con.close()


# ------------------ RESERVE BOOK ------------------
def reserve_book(book_id, student):
    con = get_connection()
    cur = con.cursor()

    cur.execute("INSERT INTO reserved_books (book_id, student_name) VALUES (%s, %s)", (book_id, student))
    con.commit()

    print("Book reserved successfully!")
    con.close()
