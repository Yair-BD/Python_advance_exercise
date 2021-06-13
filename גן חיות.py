def hiton():
    class Animal:

        zoo_list = []
        zoo_name = "Hayaton"

        def __init__(self, name="BILI", hu=0):
            self._name = name
            self._hunger = hu
            Animal.zoo_list.append(self)

        def get_name(self):
            return f"My name is {self._name} and i love u ^_^"

        def print_list(self):
           for n in Animal.zoo_list:
               print(n)

        def is_hungry(self):
            if self._hunger > 0:
                return True
            else:
                print(f"Ho i'm fully fed right now love you, {self._name} ")
                return False

        def feed(self):
            self._hunger -= 1

            return f"I am {self._name} and i LOVE U ^_^"

        def talk(self):
            return "I am foo! "

    class Dog(Animal):

        def __init__(self, name, hu=0):
            super().__init__(name, hu)

        def talk(self):
            return "WOOF WOOF"

        def fetch_stick(self):
            return "There you go, sir"

    class Cat(Animal):

        def __init__(self, name, hu):
            super().__init__(name, hu)

        def talk(self):
            return "MEOW"

        def chase_lazer(self):
            return "Meeeeeeeoow"

    class Skunk(Animal):

        def __init__(self, name, hu, count=6):
            super().__init__(name, hu)
            self._stink_count = count

        def talk(self):
            return "TSSSS"

        def stink(self):
            return "Dear lord !"

    class Unicorn(Animal):

        def __init__(self, name, hu):
            super().__init__(name, hu)

        def talk(self):
            return "Good day, darling"

        def sing(self):
            return "I'm not your tooooy"

    class Dragon(Animal):

        def __init__(self, name, hu, color="Green"):
            super().__init__(name, hu)
            self._color = color

        def talk(self):
            return "ROOAAWWR"

        def breath_fire(self):
            return "#$#$$$$*#*"

    def main():
        Brownie = Dog("Brownie", 10)
        Zelda = Cat("Zelda", 3)
        Stinky = Skunk("Stinky", 0)
        Keith = Unicorn("Keith", 7)
        Lizzy = Dragon("Lizzy", 1450)
        Doggo = Dog("Doggo", 80)
        Kitty = Cat("Kitty", 80)
        Stinky_Jt = Skunk("Stinky Jr.", 80)
        Clair = Unicorn("Clair", 80)
        McFly = Dragon("McFly", 80)
        for animal in Animal.zoo_list:
            print(type(animal).__name__)
            while animal.is_hungry():
                animal.feed()
            print(animal.talk())
        print(isinstance(Kitty, Cat))
        print(Cat)






        # (Lizzy.print_list())

    main()


if __name__ == '__main__':
    hiton()
