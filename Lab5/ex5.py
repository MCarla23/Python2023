class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        pass

    def print_details(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, age)
        self.furColor = color

    def action(self):
        return self.name + " is running."

    def print_details(self):
        return self.name + " is a mammal of age " + str(self.age) + ". It has " + self.furColor + " fur color."


class Bird(Animal):
    def __init__(self, name, age, speed):
        Animal.__init__(self, name, age)
        self.flyingSpeed = speed

    def action(self):
        return self.name + " is flying."

    def print_details(self):
        return self.name + " is a bird of age " + str(self.age) + ". It can fly with this speed: " + str(self.flyingSpeed) + '.'


class Fish(Animal):
    def __init__(self, name, age, habitat):
        Animal.__init__(self, name, age)
        self.habitat = habitat

    def action(self):
        return self.name + " is swimming."

    def print_details(self):
        return self.name + " is a mammal of age " + str(self.age) + ". It lives in " + self.habitat + '.'


cat = Mammal('Kitty', 13, 'white')
bird = Bird('Pheonix', 1351, 14.02)
fish = Fish('Nemo', 2, 'deep sea')
print(cat.print_details(), cat.action())
print(bird.print_details(), bird.action())
print(fish.print_details(), fish.action())