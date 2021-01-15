class Animal():
    def __init__(self):
        self.move = True
        self.cruelty = True

    def definition(self):
        print("created by Nature....")


class Monkey(Animal):
    def __init__(self):
        self.walk = True
        Animal.__init__(self)

class Human(Monkey):
    def __init__(self):
        Monkey.__init__(self)
        self.think = True
        self.cruelty = False

class Robot(Human):
    def __init__(self):
        Human.__init__(self)
        self.super_intelligent = True

    def definition(self):
        print("created by Humans....")


h = Human()
print("Human thinking",h.think)
print("human moving",h.move)
# Example for overriding attribute
print("human cruelty existence",h.cruelty)

robo=Robot()
# Example for overriding method
robo.definition()

