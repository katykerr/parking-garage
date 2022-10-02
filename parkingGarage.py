
# take a ticket
# dictionary for tickets -1 each time
# list for space -1 each time
# one function for both actions

<<<<<<< main
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
=======

# take a ticket
# dictionary for tickets -1 each time
# list for space -1 each time
# one function for both actions




class parking_Garage():

    ticket_available[9]
    space_available[9]

    def TakeTickets():
        input("Welcome to the parking garage. Type PARK to take a ticket")
        if input == "PARK":
            ticket_list.remove(-1)
            parking_list.remove(-1)
        else:
            print("If you're not parking, please get out.")


    def payForParking():
        input("Ready to leave? Enter your payment total now:")
        if input:
            input == dict[value == True]
            print("Thanks for paying! You have 15 minutes to leave before you self destruct.")
        else:
            print("Please pay.")

    def leaveGarage():
        if dict[value] == True:
            print("Thank you, have a nice day!")

        else:
            input("Ready to leave? Enter your payment total now:")

        elif input:
            input == dict[value == True]
            ticket_list.append(+1)
            parking_list.append(+1)
            print("Thank you, have a nice day!")


class Parking_Garage:

 def __init__(self):
        self.tickets = []
        self.parkingSpaces = 10
        self.currentTicket = 0



    def TakeTickets():
        if garage_prompts.lower == "park":
            ticket_list.remove(-1)
            parking_list.remove(-1)
        else:
            print("If you're not parking, please get out.")


    def PayForParking():
        input("Ready to leave? Enter your payment total now:")
        if input:
            input == dict[value == True]
            print("Thanks for paying! You have 15 minutes to leave before you self destruct.")
        else:
            print("Please pay.")

    def LeaveGarage():
        if dict[value] == True:
            print("Thank you, have a nice day!")

        else:
            input("Ready to leave? Enter your payment total now:")

        elif input:
            input == dict[value == True]
            ticket_list.append(+1)
            parking_list.append(+1)
            print("Thank you, have a nice day!")


while True:

        garage_prompts = input("Welcome to the parking garage. What would you like to do: [Park], [Pay], or [Leave]?")

print(Parking_Garage())
