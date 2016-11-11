# ticket_booking
Introduction

eticket is a console application that facilitates a ticket booking service
eticket allows a user to do the following:

Create a new event with a name, start date, end date and venue
Generate tickets for events and send an email update
Invalidate a ticket
View an event's tickets
Delete an event
List out all events
Send email updates on an event's schedule
Dependencies

Backend Dependencies:

Docopt - This is a Pythonic package that allows creating the command-line interface for eticket.
SQlite - This is a light-weight relational database that eticket uses to store event data.
SQL Alchemy - This is a python SQL toolkit and Object relational mapper.
smtplib - This is a python library that handles sending of emails via python modules.
python-crontab - This is a python library that enables scheduling of various tasks.
mailgun - Mailgun offers an API for sending emails.

Installation and setup:

Navigate to a directory of choice on terminal.

Clone this repository from Github on that directory.

Using SSH;

git@github.com:andyela/ticket_booking.git
Using HTTP;

https://github.com/andyela/ticket_booking.git
Navigate to the repo's folder on your computer

cd eticket
Install the app's dependencies using a virtual environment

pip install -r requirements.txt
Run the app
python tickets.py -i for interactive mode
Tests

Tests have been written using the python unittest framework.
To run the tests, navigate to the project's root folder,
issue the following command on terminal.
python buzz_tests.py
If the tests are successful, they will not display any error or failure.
To-Do:

Cron jobs to be assigned email addresses
User profiles for user identification
Event edit for event detail change
