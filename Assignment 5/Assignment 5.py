class Animals:
    def __init__(self, l, e):
        self.legs = l
        self.eyes = e


class wild_animals(Animals):
    def place(self):
        print("Lives in Jungle")


class carnivores(wild_animals):
    def food(self):
        print("Eats Meat")


class tiger(carnivores):
    def speak(self):
        print("Roars")

    def colour(self):
        print("Yellow with black strips")


class fox(carnivores):
    def speak(self):
        print("gekkering")

    def colour(self):
        print("red")


class lion(carnivores):
    def speak(self):
        print("Roars")

    def colour(self):
        print("Body colour is yellow")


class herbivores(wild_animals):
    def food(self):
        print("Eat Plant-based diet")


class deer(herbivores):
    def personality(self):
        print("Shy and demure")

    def colour(self):
        print("Body colour is brown")


class elephant(herbivores):
    def personality(self):
        print("Attentiveness and sociability")

    def colour(self):
        print("Body colour is grey")


class zebra(herbivores):
    def personality(self):
        print("Aggressive streak")

    def colour(self):
        print(" Body colour is black and white")


class domestic_animals(Animals):

    def place(self):
        print("Areas habitated by human beings")


class dog(domestic_animals):
    def speak(self):
        print("bark")

    def colour(self):
        print("Body colour is brown, black, white, golden, etc")

    def quality(self):
        print("Honest")


class cat(domestic_animals):
    def speak(self):
        print("meow")

    def colour(self):
        print("Body colour is grey,brown, black, white, etc")

    def quality(self):
        print("Active and vigilant")


class cow(domestic_animals):
    def speak(self):
        print("moo")

    def colour(self):
        print("Body colour is white, brown,etc")

    def quality(self):
        print("Shyness and sociability")


print("About Aslan the lion:")
Aslan = lion(4, 2)

Aslan.speak()
Aslan.colour()
Aslan.place()
Aslan.food()
print()
print("About Benjamin the cat:")
Benjamin = cat(4, 2)

Benjamin.speak()
Benjamin.quality()
Benjamin.colour()
Benjamin.place()
