import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import Hamurabi


class HamurabiTest(TestCase):
    @patch('sys.stdout', return_value='1')
    def test_ask_how_many_acres_to_buy(self, user_input):

        actual = Hamurabi.ask_how_many_acres_to_buy()
        expected = 19
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    def test_ask_how_many_acres_to_sell(self, user_input):
        expected = 19
        actual = Hamurabi.ask_how_many_acres_to_sell()
        self.assertEqual(expected, actual)



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
