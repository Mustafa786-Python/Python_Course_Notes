"""
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
"""

from random import randint


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(
            f"The ticket is booked from {fro} to {to} in Train Number {self.trainNo}")

    def get_status(self):
        print(f"The {self.trainNo} is running")

    def fare(self, fro, to):
        print(
            f"The Fare from {fro} to {to} in Train Number {self.trainNo} is Rs {randint(3000, 5000)}")

train = Train(12399)
train.book("Karachi", "Lahore")
train.get_status()
train.fare("Karachi", "Lahore")