# coding=utf-8
import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def speak(self):
        print(f"{self.name} can speak.")

    def run(self):
        print(f'{self.name} can run.')


class Cat(Animal):
    def __init__(self, name, color, age, gender, hair="short"):
        super(Cat, self).__init__(name, color, age, gender)
        self.hair = hair

    def speak(self):
        print(f"{self.name} can MewMew.")

    def catch(self):
        print(f"{self.name} can catch mice.")


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair="long"):
        super(Dog, self).__init__(name, color, age, gender)
        self.hair = hair

    def speak(self):
        print(f"{self.name} can bark.")

    def lookafter(self):
        print(f"{self.name} can look after houses.")


if __name__ == '__main__':
    catty = Cat(**yaml.load(open("Ani.yml"), Loader=yaml.FullLoader)[0])
    print(f"{catty.name}, {catty.color}, {catty.age}, {catty.gender}, {catty.hair}")
    catty.catch()

    doggy = Dog(**yaml.load(open("Ani.yml"), Loader=yaml.FullLoader)[1])
    print(f"{doggy.name}, {doggy.color}, {doggy.age}, {doggy.gender}, {doggy.hair}")
    doggy.lookafter()
