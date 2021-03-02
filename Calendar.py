""" CLI 
      INTERACTIVE
          Calendar
"""
from time import sleep, strftime
NAME = "Steve"
calendar = {}

def welcome():
  print "Welcome to Calendar, %s!" % (NAME)
  print "The program is starting..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d %Y")
  print "Time: " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar is empty!"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("What update? ")
      calendar[date] = update
      print "Update successful!"
      print calendar
start_calendar()


