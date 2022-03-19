import Hamurabi


class PlanningPhase:

    def __init__(self):
        super().__init__(Hamurabi.year,)


def play_game():
    game_over = False


# My Functions
def summary():
    print(f'O great Hammurabi!\n \
    You are in year {year} of your ten year rule.\n \
    In the previous year {starvation_deaths} people starved to death.\n \
    In the previous year {immigrants} people entered the kingdom.\n \
    The population is now {population}.\n \
    We harvested {harvest} bushels at {harvest_ratio} bushels per acre.\n \
    Rats destroyed {grain_eaten_by_rats} bushels, leaving {bushels - grain_eaten_by_rats} bushels in storage.\n \
    The city owns {acres} acres of land.\n \
    Land is currently worth {new_cost_of_land} bushels per acre.\n \
    -----------------------------------------------------\n')


def ask_how_many_acres_to_buy(price, bushels):
    start = True
    acres_to_buy = int(input('O Great Hammurabi, how many acres of land do you wish to buy?\n'))
    price = new_cost_of_land * acres_to_buy
    if bushels > price:
        bushels -= price
        print(f' Total price cost {price} bushels.')
        print(f' You have {bushels} bushels.\n')
        return bushels
    else:
        print(
            f'O Great Hammurabi, surely you jest! We only have {bushels} bushels left. That would cost {price} bushels.\n')
    return bushels


def ask_how_many_acres_to_sell(acres_owned, bushels):
    acres_sold_ = int(input('O Great Hammurabi, how many acres of land do you wish to sell?\n'))
    if acres_sold < acres_owned:
        bushels += acres_sold * new_cost_of_land
    else:
        print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')
    return bushels


def ask_how_much_grain_to_feed_people(bushels):
    bushels_to_feed_ = int(input('O Great Hammurabi, how much grain do you wish to feed our people?\n'))
    if bushels_to_feed < bushels:
        bushels -= bushels_to_feed
    else:
        print(f'O Great Hammurabi, surely you jest! {bushels} is the limit!')
    return bushels


def ask_how_many_acres_to_plant(acres_owned, population, bushels):
    pop_possible = acres_owned / 10;
    bush_possible = bushels / 2;
    possible_plant = 0

    if population < pop_possible:
        pop_possible = population * 10

    possible_plant = int(input(f'O Great Hammurabi! How much acres would you like to plant? \n \
                                     The limit is {possible_plant}.\n'))

    if pop_possible < bush_possible and pop_possible < acres_owned:
        possible_plant = pop_possible
    elif bush_possible < pop_possible and bush_possible < acres_owned:
        possible_plant = bush_possible
    elif possible_plant > acres_owned:
        print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')
    else:
        possible_plant = acres_owned

    return possible_plant
