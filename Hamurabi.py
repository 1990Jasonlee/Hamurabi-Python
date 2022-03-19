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
    year = 1
    game_over = False
    summary()

    while year < 10 and not game_over:
        print(f'O Great Hammurabi! It is a new year! \nWould you like to buy or sell land?')

        while True:
            bushels = 2800
            acres = 1000
            buy_or_sell = int(input('Enter 1 to Buy \nEnter 2 to Sell \n'))
            if buy_or_sell == 1:
                bushels_spent = ask_how_many_acres_to_buy(new_cost_of_land, bushels)
                acres = acres + (bushels - bushels_spent) / new_cost_of_land
                bushels = bushels_spent
                break
            elif buy_or_sell == 2:
                acres_sold = ask_how_many_acres_to_sell(acres)
                acres -= acres_sold;
                bushels += acres_sold * new_cost_of_land
                break
            else:
                print('Apologies Great Hammurabi, I did not understand you!\n'
                      'Would you like to buy or sell land?\n')

        # final summary

    # def ask_to_buy(bushels, price):
    # def ask_to_sell(acres_owned):
    # def ask_to_feed_people(bushels):
    # def ask_to_plant_land(acres_owned, population, bushels):
    # def final_message(acres, bushels, population, people_starved):
    # def plague(population):
    # def starved_deaths(population, bushels_to_feed_people):
    # def immigrants(population, acres_owned, grain_in_storage):
    # def uprising(population, people_starved):
    # def harvest(acres, bushels_used_as_seed):
    # def grain_eaten_by_rats(bushels):
    # def new_cost_of_land():


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

    acres_planted = int(input(f'O Great Hammurabi! How much acres would you like to plant? \n \
                                     The limit is {possible_plant}.\n'))

    if pop_possible < bush_possible and pop_possible < acres_owned:
        possible_plant = pop_possible
    elif bush_possible < pop_possible and bush_possible < acres_owned:
        possible_plant = bush_possible
    elif possible_plant > acres_owned:
        print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')
    else:
        possible_plant = acres_owned

    return acres_planted


play_game()
