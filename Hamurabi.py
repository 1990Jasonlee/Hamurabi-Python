from random import randint


def play_game():
    # Default variables
    year = 1
    starvation_deaths = 0
    new_immigrant = 5
    population = 100
    harvested = 3000
    acres_owned = 1000
    grain_eaten = 200
    bushels = 3000
    cost_of_land = 19

    # New variables
    acres_sold = 0
    bushels_to_feed = 0
    acres_planted = 0
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

    def ask_how_many_acres_to_buy(bushels):
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

    def ask_how_many_acres_to_sell(bushels):
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
        if bushels_to_feed <= bushels:
            bushels -= bushels_to_feed
        else:
            print(f'O Great Hammurabi, surely you jest! {bushels} is the limit!')
        return bushels

    def ask_how_many_acres_to_plant(bushels):
        pop_possible = acres_owned / 10;
        bush_possible = bushels / 2;
        possible_plant = 0

        if population < pop_possible:
            pop_possible = population * 10

        acres_to_plant = int(input(f'O Great Hammurabi! How much acres would you like to plant? '))

        if pop_possible < bush_possible and pop_possible < acres_owned:
            possible_plant = pop_possible
        elif bush_possible < pop_possible and bush_possible < acres_owned:
            possible_plant = bush_possible
        elif possible_plant > acres_owned:
            print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')
        else:
            possible_plant = acres_owned

        return acres_to_plant

    def plague():
        if randint(0, 99) < 15:
            print("O Great Hammurabi we've experienced a plague! Half the population has died!")
            return population/2
        else:
            return 0

    def starved_deaths():
        if (bushels_to_feed/20) < population:
            print(f'We lost {round(population-(bushels_to_feed/20))} people to starvation')
            return round(population - (bushels_to_feed/20))
        else:
            return 0

    def immigrants():
        new_immigrants = int((20 * acres_owned + bushels) / (100 * population))
        if new_immigrants < 0:
            return 0
        else:
            return int(new_immigrants)

    def uprising():
        percentage = starvation_deaths /(population + 1)
        if percentage > .45:
            return True
        else:
            return False

    def harvest(acres_to_plant):
        rand = randint(1, 7)
        to_harvest = acres_to_plant * rand
        return to_harvest

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
    summary()
    while year <= 10 and not game_over:
        while True:
            buy_or_sell = int(input('Enter 1 to Buy \nEnter 2 to Sell \n'))
            if buy_or_sell == 1:
                bushels_spent = ask_how_many_acres_to_buy(bushels)
                acres_owned = acres_owned + (bushels - bushels_spent) / cost_of_land
                bushels -= bushels_spent
                break
            elif buy_or_sell == 2:
                acres_sold = ask_how_many_acres_to_sell(bushels)
                acres_owned -= acres_sold
                bushels += acres_sold + (bushels - bushels_spent) / cost_of_land
                break

        fed = ask_how_much_grain_to_feed_people(bushels)
        bushels -= fed

        acres_to_plant = ask_how_many_acres_to_plant(bushels)

        harvested = harvest(acres_to_plant)
        if harvested == 0:
            harvest_ratio = 0
        else:
            harvest_ratio = harvested/acres_to_plant
            bushels += harvested

        year += 1

        #plague_bodies = plague()
        #population -= plague_bodies

        starvation_deaths = starved_deaths()
        population -= starvation_deaths
        if uprising():
            game_over = True
            break

        if population == 0:
            game_over = True
        else:
            if starvation_deaths == 0:
                new_immigrant += immigrants()
                population += new_immigrant

        grain_eaten = grain_eaten_by_rats(bushels)
        bushels -= grain_eaten

        cost_of_land = new_cost_of_land()

        summary()
        # final summary
play_game()
