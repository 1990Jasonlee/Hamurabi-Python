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
bushels = 2800
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
harvest_ratio = 0
immigrant_sum = 0


def play_game():
    game_over = False


# My Functions
def ask_how_many_acres_to_buy(bushels):
    global price
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
