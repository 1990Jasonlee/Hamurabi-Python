from random import randint

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
total_immigrant = 0


def summary():
    print(f'O great Hammurabi!\n \
    You are in year {year} of your ten year rule.\n \
    In the previous year {starvation_deaths} people starved to death.\n \
    In the previous year {new_immigrant} people entered the kingdom.\n \
    The population is now {round(population)}.\n \
    We harvested {harvested} bushels at {harvest_ratio} bushels per acre.\n \
    Rats destroyed {grain_eaten} bushels, leaving {bushels - grain_eaten} bushels in storage.\n \
    The city owns {acres_owned} acres of land.\n \
    Land is currently worth {cost_of_land} bushels per acre.\n \
    -----------------------------------------------------\n')


def final_summary():
    if uprising == True:
        print(f'O Hammurabi!\n \
             In only year {year} of your rule,\n" \
             you have created a disaster, you have been overthrown as ruler.\n \
             GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        print(f'O great Hammurabi!\n \
             In your {year} year rule, {total_immigrant} people entered the kingdom.\n \
             The city owns {acres_owned} acres of land.\n \
             You own {bushels} bushels!\n \
             Congratulations on your retirement')


def ask_how_many_acres_to_buy():
    acres_to_buy = int(input('O Great Hammurabi, how many acres of land do you wish to buy?\n'))
    price = cost_of_land * acres_to_buy
    if bushels > price:
        return price
    else:
        print(
            f'O Great Hammurabi, surely you jest! We only have {bushels} bushels left. That would cost {price} bushels.\n')


def ask_how_many_acres_to_sell():
    acres_to_sell = int(input('O Great Hammurabi, how many acres of land do you wish to sell?\n'))
    if acres_to_sell < acres_owned:
        price = acres_to_sell * cost_of_land
        return price
    else:
        print(f'O Great Hammurabi, surely you jest! {acres_owned} is the limit!')


def ask_how_much_grain_to_feed_people():
    fed = int(input('O Great Hammurabi, how much grain do you wish to feed our people?\n'))
    if fed <= bushels:
        return fed
    else:
        print(f'O Great Hammurabi, surely you jest! {bushels} is the limit!')


def ask_how_many_acres_to_plant():
    global possible_plant
    possible_plant = int(input(f'O Great Hammurabi! How much acres would you like to plant? '))

    pop_possible = acres_owned / 10;
    bush_possible = bushels / 2;

    if population < pop_possible:
        pop_possible = population * 10

    if possible_plant <= acres_owned and pop_possible and bush_possible:
        return possible_plant
    else:
        print(f'O Great Hamurabi, surely you jest! The limit of acres you can plant is {acres_owned}')



def plague():
    if randint(0, 99) < 15:
        print("O Great Hammurabi we've experienced a plague! Half the population has died!")
        return population / 2
    else:
        return 0


def starved_deaths():
    if (bushels_to_feed / 20) < population:
        print(f'We lost {round(population - (bushels_to_feed / 20))} people to starvation')
        return round(population - (bushels_to_feed / 20))
    else:
        return 0


def immigrants():
    new_immigrants = int((20 * acres_owned + bushels) / (100 * population))
    if new_immigrants < 0:
        return 0
    else:
        return int(new_immigrants)


def uprising():
    percentage = starvation_deaths / (population + 1)
    if percentage > 45 / 100:
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


def play_game():
    game_over = False
    summary()
    global year
    global acres_owned
    global bushels
    global population
    global new_immigrant
    global starvation_deaths
    global harvested
    global grain_eaten
    global cost_of_land
    global acres_sold
    global bushels_to_feed
    global acres_planted
    global bushels_for_planting
    global harvest_ratio
    global total_immigrant

    while year <= 3 and not game_over:
        while True:
            buy_or_sell = int(input('Enter 1 to Buy \nEnter 2 to Sell \n'))
            if buy_or_sell == 1:
                acres_bought = ask_how_many_acres_to_buy() / cost_of_land
                bushels_spent = acres_bought * cost_of_land
                acres_owned += acres_bought
                bushels -= bushels_spent
                print(f'{bushels_spent} bushels used, {bushels} bushels left')
                break

            elif buy_or_sell == 2:
                acres_sold = ask_how_many_acres_to_sell() / cost_of_land
                bushels += acres_sold * cost_of_land
                acres_owned -= acres_sold
                print(f'You now have {bushels} bushels and {acres_owned} acres owned after selling {acres_sold} acres.')
                break

        bushels_to_feed = ask_how_much_grain_to_feed_people()
        bushels -= bushels_to_feed
        print(f'You now have {bushels} left after feeding your people.')

        acres_planted = ask_how_many_acres_to_plant()
        print(f'acres to plant = {acres_planted}')
        bushels -= acres_planted * 2  # update bushel totals. It takes 2 bushels to plant 1 acre.
        print(f'You now have {bushels} left after planting your acres of land.')

        harvested = harvest(acres_planted)
        if harvested == 0:
            harvest_ratio = 0
        else:
            harvest_ratio = harvested / acres_planted
            bushels += harvested

        year += 1

        plague_bodies = plague()
        population -= plague_bodies

        starvation_deaths = starved_deaths()
        if starvation_deaths == 0:
            new_immigrant += immigrants()
            total_immigrant += new_immigrant
            population += new_immigrant
        else:
            population -= starvation_deaths

        if uprising():
            game_over = True
            break
        grain_eaten = grain_eaten_by_rats(bushels)
        bushels -= grain_eaten

        cost_of_land = new_cost_of_land()

        summary()
    final_summary()


play_game()
