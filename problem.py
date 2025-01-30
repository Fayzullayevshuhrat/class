class Car:
    def __init__(self, company, model, year):
        self.make = company
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

class Baloon:
    def __init__(self,company, color, size):
        self.company = company
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.color} {self.size}"


class Basket:
    def __init__(self):
        self.baloons = []

    def add_baloon(self, baloon):
        self.baloons.append(baloon)

    def __str__(self):





