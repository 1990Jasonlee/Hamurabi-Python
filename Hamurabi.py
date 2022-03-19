import planning_phase


def play_game():
    game_over = False
    while planning_phase.year <= 10 and not game_over:
        planning_phase.summary()
        while True:
            choice = int(input('Input number 1 to buy, 2 to sell'))
            if choice == 1:
                planning_phase.ask_how_many_acres_to_buy(planning_phase.new_cost_of_land, planning_phase.bushels)
                break
            elif choice == 2:
                planning_phase.ask_how_many_acres_to_sell(planning_phase.acres,planning_phase.bushels)
                break
            else:
                print('Invalid input, Input number 1 to buy, 2 to sell')
        planning_phase.ask_how_much_grain_to_feed_people()
        planning_phase.ask_how_many_acres_to_plant()



        planning_phase.year += 1


play_game()
        #final summary

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