class Ticket():
    tickets = []

    def __init__(self, paid, price, hours=""):
        self.paid = paid
        self.price = price
        self.hours = hours

    def paidTicket(self):
        print("Thank you, have a nice day!")

    def priceOfTicket(self):
        print("Based on the hours you're staying, the price of your ticket costs " + self.price)

    def hoursInGarage(self):
        print("You have selected to stay " + self.hours + " in the parking garage.")


class Parkingspace():
    parking_spots = []

    def __init__(self, remaining):
        self.remaining = remaining

    def remainingSpaces(self):
        print("Thank you for entering the parking garage. There are " + self.remaining + " spots left.")
        for remain in self.remaining:
            print(remain)



class Currentticket():
    current_tickets = {
        'name': 'confirmation of payment'
    }

    def __init__(self, name, confirmation_of_payment):
        self.name = name
        self.confirmation_of_payment = confirmation_of_payment
        print(self.name + " this is your " + self.confirmation_of_payment + ".")