class Bevarage:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def display(self):
        print "Bevarage Name:", self.name, " Ingredients are"
        for ingredient in self.ingredients:
            print "Ingredient name:", ingredient.name , " Quantity: ", ingredient.quantity

    def getName(self):
        return self.name
