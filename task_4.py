class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool

    def go(self):
        print("The car went.")

    def stop(self):
        print("The car stopped.")

    def turn(self, turn=None):
        if turn is None:
            print("The car is driving straight")
        else:
            print(f"The car turns to the {turn}")

    def show_speed(self):
        print(f"Car rides at speed {self.speed} km/h")


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print("You are speeding")
        else:
            print("Well done.")


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 520:
            print("Go to the record!!!")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print("You are speeding")
        else:
            print("You are doing everything right. You have a salary.")


class PoliceCar(Car):
    def __init__(self, speed, color, name, chase):
        Car.__init__(self, speed, color, name)
        self.chase = chase
        self.is_police = True

    def show_speed(self):
        if self.chase.upper() == "YES":
            print("We have a chase! Gas to the floor!")
        elif self.speed > 60:
            print("You are speeding. No chase - set an example")
        else:
            print("Well done.")


car = PoliceCar(40, "Blue", "Ford", input("Write yes if the chase: "))
car_town = TownCar(70, "Red", "Lada")
car_sport = SportCar(576, "Yellow", "Ferrari")
car_work = WorkCar(32, "Green", "Zil")

print(car_sport.color)
print(car_sport.is_police)
car_town.show_speed()
car_work.show_speed()
car.show_speed()
car.turn(input("Intro direction if you turn: "))