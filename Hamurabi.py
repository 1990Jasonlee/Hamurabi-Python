from random import randint


def play_game():
    # Default variables
    year = 1
    starvation_deaths = 0
    immigrants = 5
    population = 100
    harvested = 3000
    acres_owned = 1000
    grain_eaten = 200
    bushels = 3000
    cost_of_land = 19
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
    new_immigrant = 0

    def summary():
        print(f'O great Hammurabi!\n \
        You are in year {year} of your ten year rule.\n \
        In the previous year {starvation_deaths} people starved to death.\n \
        In the previous year {new_immigrant} people entered the kingdom.\n \
        The population is now {population}.\n \
        We harvested {harvested} bushels at {harvest_ratio} bushels per acre.\n \
        Rats destroyed {grain_eaten} bushels, leaving {bushels - grain_eaten} bushels in storage.\n \
        The city owns {acres_owned} acres of land.\n \
        Land is currently worth {cost_of_land} bushels per acre.\n \
        -----------------------------------------------------\n')

    def ask_how_many_acres_to_buy(price, bushels):
        acres_to_buy = int(input('O Great Hammurabi, how many acres of land do you wish to buy?\n'))
        price = cost_of_land * acres_to_buy
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
        acres_sold = int(input('O Great Hammurabi, how many acres of land do you wish to sell?\n'))
        if acres_sold < acres_owned:
            bushels += acres_sold * cost_of_land
            print(f' Acres sold = {acres_sold * cost_of_land} bushels.')
            print(f' You have {bushels} bushels.\n')
        else:
            print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')
        return bushels

    def ask_how_much_grain_to_feed_people(bushels):
        bushels_to_feed = int(input('O Great Hammurabi, how much grain do you wish to feed our people?\n'))
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

        acres_planted = int(input(f'O Great Hammurabi! How much acres would you like to plant? '))

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
        if randint(0, 99) < 15:
            return population
        else:
            return 0

    def starved_deaths(population, bushels_to_feed):
        people_starved = population - bushels_to_feed / 20
        if people_starved > 0:
            return people_starved
        else:
            return 0

    def immigrants(population, acres_owned, bushels):
        new_immigrants = int((20 * acres_owned + bushels) / ((100 * population) + 1))
        if new_immigrants < 0:
            return 0
        else:
            return int(new_immigrants)
            new_immigrant += new_immigrant

    def uprising(population, starvation_deaths):
        percentage = starvation_deaths / population;
        if percentage > 45:
            return 0
        else:
            return uprising

    def harvest(acres_owned):
        rand = randint(1, 7)
        harvested = acres_owned * rand
        return harvested

    def grain_eaten_by_rats(bushels):
        if randint(0, 99) < 40:
            grains_eaten = round(randint(10, 30) * bushels / 100)
            bushels -= grains_eaten
            return grains_eaten
        else:
            return 0

    def new_cost_of_land():
        cost_of_land = randint(17, 23)
        return cost_of_land

    game_over = False
    while year <= 10 and not game_over:
        summary()
        while True:
            try:
                buy_or_sell = int(input('Enter 1 to Buy \nEnter 2 to Sell \n'))
                if buy_or_sell == 1:
                    bushels_spent = ask_how_many_acres_to_buy(cost_of_land, bushels)
                    acres_owned = acres_owned + (bushels - bushels_spent) / cost_of_land
                    bushels = bushels_spent
                    break
                elif buy_or_sell == 2:
                    bushels_spent = ask_how_many_acres_to_sell(acres_owned, bushels)
                    acres_owned -= acres_sold
                    bushels += acres_sold + (bushels - bushels_spent) / cost_of_land
                    break
            except ValueError:
                print('Apologies Great Hammurabi, I did not understand you!\n'
                      'Invalid input, Input number 1 to buy, 2 to sell')

        ask_how_much_grain_to_feed_people(population)
        ask_how_many_acres_to_plant(acres_owned, population, bushels)
        if acres_planted == 0:
            harvest_ratio = 0
        else:
            harvest_ratio = harvested/acres_planted
        year += 1
        plague(population)
        starved_deaths(population, bushels_to_feed)
        uprising(population, starvation_deaths)

        if starvation_deaths == 0:

            new_immigrant += immigrants(population, acres_owned, bushels)
            population += new_immigrant

        grain_eaten = grain_eaten_by_rats(bushels)
        bushels -= grain_eaten

        new_cost_of_land()
        cost_of_land = new_cost_of_land()
        # final summary

play_game()
