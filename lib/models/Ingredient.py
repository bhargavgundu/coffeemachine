class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display(self):
        print "Name: ", self.name, " Quantity", self.quantity

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity