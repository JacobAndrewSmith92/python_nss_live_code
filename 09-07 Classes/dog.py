from animal import Animal

class Dog(Animal):

    def __init__(self, breed):
        self.breed = breed
        super().__init__("dog", leg_num=4, domesticated=True)

    def __str__(self):
        return f"I am a {self.breed}."

    def speak(self):
        return f'{self.say_something()}'


labrador = Dog("Labrador")

# print(labrador)