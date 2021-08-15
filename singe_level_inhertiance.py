# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Animal:
    name = "animal"

    def __init__(self, color, type):
        self.color = color
        self.type = type

    def getDetails(self):
        return self.name + " : " + self.color + " " + self.type


class Plant:
    pass


class Dog(Animal):
    '''
     def __init__(self, color, name, breed):
        super(Dog, self).__init__(color, "dog")
        self.name = name
        self.breed = breed
    '''

    def __init__(self, color, name, breed):
        self.color = color
        self.type = "dog"
        self.name = name
        self.breed = breed

    def getInfo(self):
        return self.name + "," + self.breed

    def getComplete(self):
        return super().getDetails() + "|" + self.getInfo()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharms')
    rose = Plant()
    cat = Animal("black", "cat")
    dog = Animal("black", "dog")
    Animal.name = "Pet"
    print(f'{cat.getDetails()}')
    print(f'{dog.getDetails()}')

    # inheritance
    dog = Dog("black", "bruno", "pug")
    print(f'{dog.getDetails() + ", " + dog.getInfo()}')
    print(f'{dog.getComplete()}')
    print(f'{isinstance(dog, Animal)}')
    print(f'{isinstance(5, int)}')
    print(f'{issubclass(Dog, Animal)}')
    print(f'{issubclass(Animal, Dog)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
