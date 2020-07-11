from lib.models.Machine import Machine
from lib.models.Ingredient import Ingredient
from lib.models.Bevarage import Bevarage
import os
import json


def initialize_machine():
    input, name, outlets, ingredient_dict, beverages_dict = get_data_from_json()
    coffee_machine = Machine(name, outlets, ingredient_dict, beverages_dict)
    # since order is not specified, i have done according to the example in the pdf given
    # case 1 of the example output
    print "case #1"
    for beverage in input[name]['beverages'].keys():
        coffee_machine.make_beverage(beverage)

    coffee_machine = Machine(name, outlets, ingredient_dict, beverages_dict)
    print "case #2"
    for beverage in ['hot_tea', 'black_tea', 'green_tea', 'hot_coffee']:
        coffee_machine.make_beverage(beverage)

    coffee_machine = Machine(name, outlets, ingredient_dict, beverages_dict)
    print "case #3"
    for beverage in ['hot_coffee', 'black_tea','green_tea', 'hot_tea']:
        coffee_machine.make_beverage(beverage)


def get_data_from_json(json_data=None):
    if not json_data:
        input = json_from_file()
    else:
        input = json_data
    name = input.keys()[0]
    outlets = input[name]['outlets']['count_n']
    ingredient_dict = {}
    for k, v in input[name]['total_items_quantity'].items():
        object = Ingredient(k, v)
        ingredient_dict[object.getName()] = object
    beverages_dict = {}
    for k, v in input[name]['beverages'].items():
        d = {}
        for i, j in v.items():
            object = Ingredient(i, j)
            d[object.getName()] = object
        object = Bevarage(k, d)
        beverages_dict[object.getName()] = object
    return input, name, outlets, ingredient_dict, beverages_dict


def json_from_file():
    with open(os.path.join(os.path.dirname(__file__), 'input.json')) as fd:
        input = json.load(fd)
    return input


initialize_machine()
