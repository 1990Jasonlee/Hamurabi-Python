from random import random


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
    if immigrants < 0:
        immigrants= int((20 * acres_owned + grain_in_storage) / ((100 * population) + 1))
    else:
        return int(immigrants)
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
