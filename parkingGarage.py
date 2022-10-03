
class parking_Garage():

    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

    def takeTicket(self):
        #{key(string), bool\ is paid status}
        self.currentTicket.update({"Paid": False})
        # remove tickets and spaces from available in lists
        self.tickets.pop(0)
        self.parkingSpaces.pop(0)
        print("Welcome to The Parking Garage")
        print(input("To purchase a ticket for parking press any key."))
        print("Happy Parking!")
        print(input("Press any key when you're ready to leave."))
        

    def payForParking(self):
        userInput = int(input("Ready to leave? Enter your payment total now:"))
        if userInput == (""):
            print("Please pay.")

        if userInput < 20000 and not None:
            print('')
            print("Thanks for parking with us!")
            print(' ')
            # call leave method after payment
            self.leaveGarage()

    def leaveGarage(self):
        # make tiket value as paid
        self.currentTicket.update({"Paid": True})
        # add tickets and space back to lists
        self.tickets.insert(0, self.tickets[0]-1)
        self.parkingSpaces.insert(0, self.parkingSpaces[0]-1)
        print("You have 15 minutes to leave before you self destruct.")
        

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pg = parking_Garage(tickets,parkingSpaces)
run = True

while run:
    pg.takeTicket()
    pg.payForParking()
    # end loop
    break



