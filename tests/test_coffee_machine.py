import unittest
# import mock
from src.CoffeeMachine import get_data_from_json
from lib.models.Machine import Machine


def create_machine_object(json_data):
    _, name, outlets, ingredient_dict, beverages_dict = get_data_from_json(json_data)
    return Machine(name, outlets, ingredient_dict, beverages_dict)


class TestCofeeMachine(unittest.TestCase):
    def setUp(self):
        self.json_data = {
          "machine": {
            "outlets": {
              "count_n": 2
            },
            "total_items_quantity": {
              "a": 500,
              "b": 500
            },
            "beverages": {
              "hot_tea": {
                "a": 200,
                "b": 100,
                "c": 10
              },
              "hot_coffee": {
                "a": 100,
                "b": 30,
                "d": 30
              },
              "black_tea": {
                    "a": 200,
                    "b": 100
                },
             "green_tea": {
                    "a": 500,
                    "b": 100
                },
            "random_tea": {
                    "a": 700,
                    "b": 100
                }
            }
          }
        }

    def test_initial_quantities(self):
        machine = create_machine_object(self.json_data)
        self.assertEqual({'a': 500, 'b': 500}, machine.current_quantities)

    def test_initial_outlet_status(self):
        machine = create_machine_object(self.json_data)
        self.assertEqual({1: 'free', 2: 'free'}, machine.current_outlets)

    def test_refill_method(self):
        machine = create_machine_object(self.json_data)
        machine.refill_ingredient('a', 100)
        self.assertEqual({'a': 600, 'b': 500}, machine.current_quantities)

    def test_check_quantities_with_available_quantity(self):
        machine = create_machine_object(self.json_data)
        self.assertTrue(machine.check_quantities('green_tea'))

    def test_check_quantities_with_unavailable_quantity(self):
        machine = create_machine_object(self.json_data)
        self.assertFalse(machine.check_quantities('random_tea'))

    def test_check_quantities_with_unavailable_ingredient(self):
        machine = create_machine_object(self.json_data)
        self.assertFalse(machine.check_quantities('hot_tea'))

    def test_set_outlet_status(self):
        machine = create_machine_object(self.json_data)
        machine.set_outlet_status(1, 'occupied')
        self.assertEqual({1: 'occupied', 2: 'free'}, machine.current_outlets)

    def test_get_free_outlet_1(self):
        machine = create_machine_object(self.json_data)
        outlet = machine.get_free_outlet_number()
        self.assertEqual(1, outlet)

    def test_get_free_outlet_2(self):
        machine = create_machine_object(self.json_data)
        machine.set_outlet_status(1, 'occupied')
        outlet = machine.get_free_outlet_number()
        self.assertEqual(2, outlet)

    def test_consume_ingredient(self):
        machine = create_machine_object(self.json_data)
        machine.consume_ingredients_for_beverage('black_tea')
        self.assertEqual({'a': 300, 'b': 400}, machine.current_quantities)

    # figured mock might not be there in your execution environment, if its present, uncomment this and import and verify
    # @mock.patch('lib.models.Machine.request_refill_ingredient', return_val=None)
    # def test_check_low_ingredient(self, mock_request_refill):
    #     machine = create_machine_object(self.json_data)
    #     machine.consume_ingredients_for_beverage('black_tea') # a will be fully consumed
    #     self.assertTrue(mock_request_refill.called)
    #
    # below tests are done by verifying quantities for make beverage function
    def test_make_beverage_regular(self):
        machine = create_machine_object(self.json_data)
        machine.make_beverage('green_tea')
        self.assertEqual({'a': 0, 'b': 400}, machine.current_quantities)

    def test_make_beverage_regular_invalid_beverage(self):
        machine = create_machine_object(self.json_data)
        machine.make_beverage('bhargav')
        self.assertEqual({'a': 500, 'b': 500}, machine.current_quantities)



