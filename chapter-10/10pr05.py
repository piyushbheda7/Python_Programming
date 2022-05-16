# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

import random


class train:
    def __init__(self , r):
        self.r = r 

    def TicketBook(self):
        print(f"\nYour Ticket Booking is successfull.....\nyour seat No is {r}")
    
    def GetStatus(self):
        print(f"\nNo of seats available is {100-r}")

    def GetFareInfo(self):
        print("\nThis trains are running under Indian Railways.....")

r = random.randint(0,100)
irctc = train(r)
irctc.TicketBook()
irctc.GetStatus()
irctc.GetFareInfo()