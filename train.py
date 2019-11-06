class Car:
    def __init__(self, speed = 0):
        self.speed = speed
        self.dodge = False
        self.odometer = 0
        self.time = 0
    def say_state(self):
        print("I'm going {} kph!".format(self.speed))
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def step(self):
        self.odometer += self.speed
        self.time += 1
    def setSpeed(self, speed):
        self.speed = speed
    def setDodge(self, value):
        self.dodge = value
    def checkDodge(self):
        return self.dodge
    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ == '__main__':
    my_car = Car()
    infractionCount = 3
    dodgeCount = 0
    print("You are on the road.")
    print("The speed limit is 80 kph. Do not speed or lethal force will be used")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, [W]ait, [D]odge, or show [S]peed?").upper()
        if action not in "ABOWDS" or len(action) != 1:
            print("I do not know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'W':
            pass
        elif action == 'D':
            my_car.setDodge(True)
        if action != 'D':
            my_car.setDodge(False)

        if my_car.speed > 80 and infractionCount > 0:
            infractionCount -= 1
            print("You are going too fast! Slow down or you will be detonated! You have {} violations left".format(infractionCount))
        elif infractionCount == 0:
            if my_car.checkDodge():
                print("You are being hunted!")
                dodgeCount += 1
                print("You have dodged the attack {} times! Keep dodging to escape!".format(dodgeCount))
            elif dodgeCount % 3 == 0:
                print("You are being hunted!")
                dodgeCount += 1
                print("You have dodged the attack {} times! Keep dodging to escape!".format(dodgeCount))
            else:
                print("Too many violations! You have been destroyed!!!")
                my_car.setSpeed(0)
                my_car.say_state()
                break
        my_car.step()
        my_car.say_state()