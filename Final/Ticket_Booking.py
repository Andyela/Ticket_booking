import sqlite3

from datetime import date, time

conn = sqlite3.connect('ticket.db')
c = conn.cursor()

print("\t\t\t\tWelcome\t\t\t")
print("If this is your first time contacting us, \nplease use the form below to open a new ticket.\n")

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tickets(event TICKET BOOKING, login NOT NULL , event_ID NOT NULL, email TEXT)")

def generate_ticket(event, login = 'NULL', event_ID = None, email_address = None):
    c.execute("SELECT * FROM tickets WHERE event = ?", (event,))
    data = c.fetchall()
    conn.commit()

    if len(data) == 0:
        print("Invalid Entry!")

    else:
        if login == 'NULL':
            print("Unregistered User")
            response = input("Create Account? Y/N: ")
            if response == 'Y':
                login = input("\n1Enter email address: \n1, \n2Enter Password\n2")
            else:
                print("Invalid Entry!")

    c.execute(
        "INSERT INTO tickets (event_ID, email_address, ticket_status, ticket_time_stamp)VALUES (?, ?, ?, ?)",
        (event_ID, email_address, 1, date))
    print("Ticket created successfully")
    conn.commit()

    c.execute("SELECT * FROM tickets WHERE ticket_ID = (SELECT MAX(ticket_ID) FROM tickets)")
    ticket_data = c.fetchone()
    ticket_ID = ticket_data[0]
    print("Ticket ID:\t\t" + str(ticket_data[0]))
    print("Event ID:\t\t" + str(ticket_data[1]))
    print("Email Address:\t\t" + ticket_data[2])
    if ticket_data[3] == 1:
        print("Ticket Status:\t\tValid")
    elif ticket_data[3] == 0:
        print("Ticket Status:\t\tInvalid")
    else:
        print("Ticket Status:\t\t" + ticket_data[3])
        print("Time of creation:\t" + datetime.datetime.fromtimestamp.strftime('%d-%m-%Y %H:%M'))
    conn.commit()


def invalidate_ticket(ticket_ID):
    c.execute("SELECT * FROM tickets WHERE ticket_ID = ?", (int(ticket_ID),))
    data = c.fetchall()
    status = True

    if data == 0:
        print("Invalid ticket ID")

    else:
        for row in data:
            print("Ticket ID:\t\t" + str(row[0]))
            print("Event ID:\t\t" + str(row[1]))
            print("Email Address:\t\t" + row[2])
            if row[3] == 1:
                print("Ticket Status:\t\tValid")
            elif row[3] == 0:
                print("Ticket Status:\t\tInvalid")
            else:
                print("Ticket Status:\t\t" + row[3])
            print("Time of creation:\t" + datetime.datetime.fromtimestamp.strftime('%d-%m-%Y %H:%M'))
            print(50 * '*')
            if row[3] == 0:
                status = False

            if status == True:
                user_response = input("Do you want to invalidate ticket? \t\t\t[YES] \t\t\t\t[NO]: ")
                if user_response == YES:
                    c.execute("UPDATE tickets SET ticket_status = 0 WHERE ticket_ID = ?", (int(ticket_ID),))

                conn.commit()

                print("Ticket ID no.%d is now invalid"%(ticket_ID))
            else:
                print("No changes made to the ticket")


    conn.commit()

conn.close()
