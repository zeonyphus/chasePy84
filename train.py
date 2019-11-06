from random import seed
from random import randint
from math import ceil

seed(1)

# todo give everything randomness, this will make cheesing the game harder
class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.dodge = False
        self.odometer = 0
        self.time = 0
        self.timeRemaining = 80
        self.fuel = 12000  # randint(12000, 25000)
        self.distance = 4000  # randint(5000, 1000)
        self.speedLimit = 80  # randint(12, 14) * 5

    def say_state(self):
        print("Current speed: {} kph".format(self.speed))
        print("Fuel remaining: {} liters".format(self.fuel))
        print("Time remaining: {} hours".format(self.timeRemaining))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    # todo need to make the step not give positive fuel, at least within reason, say when the cops are more random
    def step(self):
        self.odometer += self.speed
        self.time += 1
        if self.speed <= self.speedLimit:
            self.fuel -= ceil((self.speed ** 2) /10)
            print("DIFF:", (self.speed ** 2) /10)
        else:
            self.fuel -= ceil((((self.speed ** 2) / 10) - ((self.speed - self.speedLimit) ** 1.8)))
            print("DIFF:", (((self.speed ** 2) / 10) - ((self.speed - self.speedLimit) ** 1.8)))
        self.distance -= self.speed
        self.timeRemaining -= 1

    def set_speed(self, speed):
        self.speed = speed

    def set_dodge(self, value):
        self.dodge = value

    def add_fuel(self, fuel):
        self.fuel += fuel
        self.timeRemaining -= 2

    def check_dodge(self):
        return self.dodge


if __name__ == '__main__':
    my_car = Car(40)  # (randint(1, 8) * 5)
    infractionCount = 3
    dodgeCount = 0
    loss = True
    pursued = False
    stopped = False
    reason = "You got away!"
    print("You are on the road")
    print("You are currently traveling at {} kph".format(my_car.speed))
    print("You need to travel {} km to get away".format(my_car.distance))
    print("You have {} hours left to get there before you are cut off by overwhelming forces".format(
        my_car.timeRemaining))
    print("You have {} liters of fuel left in your tank".format(my_car.fuel))
    print("The speed limit is {} kph. Do not speed or lethal force will be used".format(my_car.speedLimit))
    while True:
        action = input(
            "What should I do? [A]ccelerate, [B]rake, [C]heck status, [W]ait, [D]odge, or [S]top for fuel?").upper()
        if action not in "ABCWDS" or len(action) != 1:
            print("Not a possible option")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'C':
            print("The car has driven {} kilometers".format(my_car.odometer))
            print("You still have {} kilometers to go".format(my_car.distance))
        # todo make stops infrequent
        elif action == 'S':
            my_car.add_fuel(8000)  # randint(3000, 12000)
            my_car.set_speed(0)
            print("You have stopped for fuel. You now have {} litres of fuel".format(my_car.fuel))
        elif action == 'W':
            pass
        elif action == 'D':
            my_car.set_dodge(True)
        if action != 'D':
            my_car.set_dodge(False)
        if my_car.timeRemaining <= 0 < my_car.distance:
            print("You ran out of time, there are too many pursuers now")
            reason = "Failed to get away in time"
            break
        if my_car.fuel <= 0:
            print("You have run out of fuel")
            if pursued:
                print("You were captured since you ran out of fuel")
            reason = "Ran out of fuel and was captured"
            break
        # todo add failure cases for time and distance
        elif my_car.speed > 80 and infractionCount > 0:
            infractionCount -= 1
            print("Slow down or you will be detained! You have {} violations before being pursued".format(
                infractionCount))
        elif infractionCount == 0:
            pursued = True
            if dodgeCount > 3 and my_car.speed >= my_car.speedLimit + 5:  # todo make random
                pursued = False
                infractionCount = 3
                dodgeCount = 0
                print("You have dodged the pursuers! Don't get caught speeding again or you will be pursed again!")
            # todo make high chance of dodge but still random
            elif my_car.check_dodge():
                print("|||You are being pursed!|||")
                dodgeCount += 1
                print("You have dodged the pursuers {} times! Keep dodging to escape!".format(dodgeCount))
            # todo make mid-low chance of dodge on acceleration
            elif dodgeCount % 3 == 0:
                print("|||You are being pursued!|||")
                dodgeCount += 1
                print("You have dodged the pursuers {} times! Keep dodging to escape!".format(dodgeCount))
            else:
                print("Too many violations! You have been caught!!!")
                my_car.set_speed(0)
                my_car.say_state()
                reason = "Failed to dodge the authorities"
                break
        if my_car.distance <= 0 and my_car.fuel > 0:
            loss = False
            my_car.distance = 0
            print("Destination reached!!!")
            break
        my_car.step()
        my_car.say_state()
    print("~~~~~~~~~~Final Stats~~~~~~~~~~")
    print("Distance Traveled: {}".format(my_car.odometer))
    print("Distance Remaining: {}".format(my_car.distance))
    print("Fuel Remaining: {}".format(my_car.fuel))
    print("Time Remaining: {}".format(my_car.timeRemaining))
    # print("Number of dodges performed: {}".format(dodgeCount))
    if loss:
        print("Reason for loss:", reason)
        print("GAME OVER")
    else:
        print(reason)
        print("YOU WIN")