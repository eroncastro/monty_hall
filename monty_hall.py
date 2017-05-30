from random import choice, randint


class MontyHall(object):
    def __init__(self, simulations):
        self.simulations = simulations

    def simulate_choosing_remaining_door(self):
        car_door = randint(1, 3)
        wins = 0

        for i in range(self.simulations):
            # person chooses door
            person_first_door = randint(1, 3)
            # host shows door where the car is not
            host_door = choice(list(({1, 2, 3} - {car_door, person_first_door})))
            # person chooses the remaining door
            person_last_door = ({1, 2, 3} - {person_first_door, host_door}).pop()
            if person_last_door == car_door:
                wins += 1

        print(wins)
        print('Winning rate choosing remaining door: %s' % (wins / self.simulations))
