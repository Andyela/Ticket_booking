import sqlite3
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data import Event

conn = sqlite3.connect('ticketing.db')
c = conn.cursor()


class Tickets(object):

    engine = create_engine('sqlite:///eTicket.sqlite', echo = False)

    # create new session object for queries
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    def __init__(self):
        pass


    def create_event(self, arg):
        '''
        creates a new event instance
        '''
        # creating a new event from Event class
        event_name = arg['<name>']
        start_date = datetime.strptime(arg['<start_date>'], "%d-%m-%Y" )
        end_date = datetime.strptime(arg['<end_date>'], "%d-%m-%Y" )
        venue = arg['<venue>']
        event = Event(name=event_name, start_date=start_date, end_date=end_date, venue=venue)

        try:
            # add event object to session for db commit

            Tickets.session.add(event)
            Tickets.session.commit()
            return "Event created"
        except Exception as e:
            print (e)
            raise e

    @staticmethod
    def delete_event(event_id):
        # query item by id given
        deleted_item = Tickets.session.query(Event).filter_by(id=event_id).delete()
        # EventsCrud.session.delete(deleted_item)
        Tickets.session.commit()
        return 'Entry has been deleted'

    def list_events(self):

        events = Tickets.session.query(Event).all()
        event_data = []
        for item in events:
            event_data.append([item.name, item.start_date, item.end_date, item.venue])

        for event in events:
            print("{} {} {} {} {}".format('id'.ljust(15), 'name'.ljust(10), 'start_date'.ljust(20),
                                          'end_date'.ljust(20), 'venue'.ljust(30)))

        for event_item in event_data:
            print("{} {} {} {}".format(str(event_item[1]).ljust(15), event_item[0].ljust(10),
                                       str(event_item[1]).ljust(20), str(event_item[2]).ljust(20),
                                       event_item[3].ljust(30)))
        print(
            '--------------------------------------------------------------------------------------------')

    def edit_event(self, event_id, **kwargs):
        event_item = Tickets.session.query(Event).filter_by(id == event_id)
        event_item['event'] = kwargs['events']
        event_item.EventsCrud.session.commit()

        return event_item


conn.commit()
conn.close()