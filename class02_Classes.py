class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("BugsBunny")

hawk = Hawk("Guille")

fish = Fish("Nemo")

hawk.hunt()
rabbit.eat()