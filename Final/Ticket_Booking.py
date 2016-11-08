import sqlite3

from datetime import date, time

conn = sqlite3.connect('ticket.db')
c = conn.cursor()

print("\t\t\tWelcome\t\t\t")
print("If this is your first time contacting us, \nplease use the form below to open a new ticket.\n")


def generate_ticket(event, login = 'NULL', event_ID = None, email_address = None):
    c.execute("SELECT * FROM events WHERE event = ?", (event,))
    data = c.fetchall()
    if len(data) == 0:
        print("Invalid Entry!")

    else:
        if login == 'NULL':
            print("Unregistered User")
            response = input("Create Account? Y/N: ")
            if response == 'Y':
                login = input("\n1Enter email address: \n1, \n2Enter Password\n2")
            else:
                print("Invalid Entry")

    c.execute(
            "INSERT INTO tickets (event_ID, email_address, ticket_status, ticket_time_stamp) VALUES (?, ?, ?, ?)",
            (event_ID, email_address, 1, round (time.time ())))
    conn.commit()
    print("Ticket created successfully")