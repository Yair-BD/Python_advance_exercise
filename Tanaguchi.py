def animal():
    class Animal:

        def __init__(self, name):
            self._name = name
            self._hunger = 0
            self._fun = 0

        def play(self):
            self._fun += 1
            print("It's so fun to play with you ^_^")

        def eat(self):
            if self._hunger > 0:
                self._hunger -= 1
            else:
                print("Thank you but i'm already satiate ")

        def go_to_toilet(self):
            self._hunger += 1

        def print_hunger(self):
            print(self._hunger)

        def __str__(self):
            return f"My name is {self._name} and i love u ^_^"

    class Dog(Animal):

        def __init__(self, name, fur_color):
            Animal.__init__(self, name)
            self._fur_color = fur_color

        def eat(self):
            super().eat()
            print("Thanks Waff")

        def go_for_a_walk(self):
            self._fun += 3
            print(f"Waff Waff !! My fun is rising, and its: {self._fun}")

    def main():
        fluppy = Dog("Fluppy", "Brown")
        fluppy.play()
        fluppy.go_to_toilet()
        fluppy.eat()
        fluppy.go_for_a_walk()
        fluppy.print_hunger()
        print(fluppy)

    main()


if __name__ == '__main__':
    animal()