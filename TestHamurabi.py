import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import planning_phase


class summary_test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_summary(self, stdout_mock):
        summary = (f'O great Hammurabi!\n \
        You are in year 1 of your ten year rule.\n \
        In the previous year 0 people starved to death.\n \
        In the previous year 5 people entered the kingdom.\n \
        The population is now 100.\n \
        We harvested 3000 bushels at 3 bushels per acre.\n \
        Rats destroyed 200 bushels, leaving 2800 bushels in storage.\n \
        The city owns 1000 acres of land.\n \
        Land is currently worth 19 bushels per acre.\n \
        -----------------------------------------------------\n')
        expected = (f'O great Hammurabi!\n \
    You are in year 1 of your ten year rule.\n \
    In the previous year 0 people starved to death.\n \
    In the previous year 5 people entered the kingdom.\n \
    The population is now 100.\n \
    We harvested 3000 bushels at 3 bushels per acre.\n \
    Rats destroyed 200 bushels, leaving 2800 bushels in storage.\n \
    The city owns 1000 acres of land.\n \
    Land is currently worth 19 bushels per acre.\n \
    -----------------------------------------------------\n\
    \n')

        planning_phase.summary()
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('builtins.input', return_value='1')
    def test_acres_to_buy(self, user_input):
        actual = planning_phase.acres_to_buy()
        self.assertEqual(1, actual)



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
