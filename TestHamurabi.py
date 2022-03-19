from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import planning_phase


class buying_test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_ask_how_many_acres_to_buy(self, stdout_mock):

        expected = 'O Great Hammurabi, how many acres of land do you wish to buy?\n'
        planning_phase.ask_how_many_acres_to_buy()
        self.assertEqual(expected, stdout_mock)  # add assertion here

# def test_welcome_message():
# def test_ask_to_buy(bushels, price):
# def test_ask_to_sell(acres_owned):
# def test_ask_to_feed_people(bushels):
# def test_ask_to_plant_land(acres_owned, population, bushels):
# def test_plague(population):
# def test_starved_deaths(population, bushels_to_feed_people):
# def test_immigrants(population, acres_owned, grain_in_storage):
# def test_uprising(population, people_starved):
# def test_harvest(acres, bushels_used_as_seed):
# def test_grain_eaten_by_rats(bushels):
# def test_new_cost_of_land():
# def test_final_message(acres, bushels, population, people_starved):

if __name__ == '__main__':
    unittest.main()
