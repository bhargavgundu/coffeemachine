class Machine:
    # constructor to initialize the machine
    def __init__(self, name, outlets, ingredients, beverages):
        self.name = name
        self.outlets = outlets
        self.ingredients = ingredients
        self.beverages = beverages
        self.current_quantities = {}
        self.current_outlets = {}
        self.set_initial_quantities()
        self.set_all_outlets_open()

    # setting the initial quantities
    def set_initial_quantities(self):
        for k, v in self.ingredients.items():
            self.current_quantities[k] = v.getQuantity()

    # marking all outlets open at start
    def set_all_outlets_open(self):
        for i in range(self.outlets):
            self.current_outlets[i+1] = 'free'

    # checking if any outlet is free
    def check_outlet_free(self):
        return 'free' in self.current_outlets.values()

    # returns the first free outlet number
    def get_free_outlet_number(self):
        for outlet, status in self.current_outlets.items():
            if status == 'free':
                return outlet

    # setting the outlet status to free/occupied
    def set_outlet_status(self, outlet, status):
        self.current_outlets[outlet] = status

    # method to check if the ingredient quantities are enough to make a beverage
    def check_quantities(self, beverage_name):
        error_reason = None
        ingredients_needed = self.beverages[beverage_name].ingredients
        for ingredient_name, ingredient_object in ingredients_needed.items():
            error_msg = beverage_name + " cannot be prepared because item " + ingredient_name + " is"
            if ingredient_name not in self.current_quantities:
                error_reason = " not available"
            elif self.current_quantities[ingredient_name] < ingredient_object.getQuantity():
                error_reason = " is not sufficient"
            if error_reason:
                print error_msg, error_reason
                return False
        return True

    # method to consume quantities and dispense the beverage
    def make_beverage(self, beverage_name):
        if beverage_name not in self.beverages.keys():
            print "This kind of beverage is not served"
            return
        if not self.check_quantities(beverage_name):
            return
        if self.check_outlet_free():
            outlet = self.get_free_outlet_number()
            self.set_outlet_status(outlet, 'occupied')
            self.consume_ingredients_for_beverage(beverage_name)
            print beverage_name, " is prepared"  # on outlet number outlet
            self.set_outlet_status(outlet, 'free')
        else:
            print "No outlets free right now, try after some time"
        return

    # method to reduce the quantities of used ingredients
    def consume_ingredients_for_beverage(self, beverage_name):
        ingredients_needed = self.beverages[beverage_name].ingredients
        for ingredient_name, ingredient_object in ingredients_needed.items():
            self.current_quantities[ingredient_name] -= ingredient_object.getQuantity()

    # method to check if any ingredients are low
    def check_if_any_low_ingredients(self):
        for ingredient_name, quantity in self.current_quantities.items():
            if quantity == 0:
                self.request_refill_ingredient(ingredient_name)

    # user prompt to refill
    def request_refill_ingredient(self, ingredient_name):
        print ingredient_name, " is very low, please refill "

    # method to refill ingredients
    def refill_ingredient(self, ingredient_name, refill_quanity):
        self.current_quantities[ingredient_name] += refill_quanity
