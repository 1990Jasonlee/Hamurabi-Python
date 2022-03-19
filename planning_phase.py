class PlanningPhase:

    def __init__(self):
        pass


# Default variables
year = 1
starvation_deaths = 0
immigrants = 5
population = 100
harvest = 3000
acres = 1000
grain_eaten_by_rats = 200
bushels = 3000
new_cost_of_land = 19
acres_to_buy = 0

# New variables
bushels_spent = 0
buy_or_sell = 0
acres_sold = 0
bushels_to_feed = 0
acres_planted = 0
plague_bodies = 0
bushels_for_planting = 0
harvest_ratio = 3
immigrant_sum = 0


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


