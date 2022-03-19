from random import random

def play_game():
# Default variables
    year = 1
    starvation_deaths = 0
    immigrants = 5
    population = 100
    harvest = 3000
    acres_owned = 1000
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

    def summary():
        print(f'O great Hammurabi!\n \
        You are in year {year} of your ten year rule.\n \
        In the previous year {starvation_deaths} people starved to death.\n \
        In the previous year {immigrants} people entered the kingdom.\n \
        The population is now {population}.\n \
        We harvested {harvest} bushels at {harvest_ratio} bushels per acre.\n \
        Rats destroyed {grain_eaten_by_rats} bushels, leaving {bushels - grain_eaten_by_rats} bushels in storage.\n \
        The city owns {acres_owned} acres of land.\n \
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


    def plague(population):
            if random.randint(0, 99) < 15:
                return population
            else:
                return 0
    def starved_deaths(population, bushels_to_feed_people):
        people_starved = population - bushels_to_feed_people / 20
        if people_starved > 0:
            return people_starved
        else:
            return 0

    def immigrants(population, acres_owned, grain_in_storage,):
        new_immigrants = int((20 * acres_owned + grain_in_storage) / ((100 * population) + 1))
        if immigrants < 0:
            return 0
        else:
            return int(new_immigrants)


    def uprising(population, people_starved):
        percentage =  people_starved / population;
        if percentage > 45:
            return 0
        else:
            return uprising


    def harvest(acres, bushels_used_as_seed):
        bushels_used_as_seed = acres * harvest
        return bushels_used_as_seed


    def grain_eaten_by_rats(harvest):
        if random.randint(0, 99) < 40:
            bushels_destroyed = random.randint(10, 30) * harvest / 100
            return bushels_destroyed
        else:
            return 0



    def new_cost_of_land():
            new_cost_of_land = random.randint(17, 23)
            return new_cost_of_land

    game_over = False
    while year <= 10 and not game_over:
        summary()
        while True:
            print(f'O Great Hammurabi! It is a new year! \nWould you like to buy or sell land?')
            choice = int(input('Enter 1 to Buy \nEnter 2 to Sell \n'))
            if choice == 1:
                ask_how_many_acres_to_buy(new_cost_of_land, bushels)
                bushels_spent = ask_how_many_acres_to_buy(new_cost_of_land, bushels)
                # acres = acres + (bushels - bushels_spent) / new_cost_of_land
                # bushels = bushels_spent
                break
            elif choice == 2:
                ask_how_many_acres_to_sell(acres_owned, bushels)
                # acres_sold = ask_how_many_acres_to_sell(acres)
                # acres -= acres_sold;
                # bushels += acres_sold * new_cost_of_land
                break
            else:
                print('Apologies Great Hammurabi, I did not understand you!\n'
                      'Invalid input, Input number 1 to buy, 2 to sell')
        ask_how_much_grain_to_feed_people(bushels)
        ask_how_many_acres_to_plant(acres_owned, population, bushels)


        year += 1


            #final summary

        # def final_message(acres, bushels, population, people_starved):
        # def plague(population):
        # def starved_deaths(population, bushels_to_feed_people):
        # def immigrants(population, acres_owned, grain_in_storage):
        # def uprising(population, people_starved):
        # def harvest(acres, bushels_used_as_seed):
        # def grain_eaten_by_rats(bushels):
        # def new_cost_of_land():





play_game()