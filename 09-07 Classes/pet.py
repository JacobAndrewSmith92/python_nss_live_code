# 1) Give a pet its own prop of name
# 2) Give it a property of animal_type
# 3) animal_type needs to be an instance of a dog
# 4) assign an owner via a method
# 5) __str__ return a string with pet's name, # of legs, and what it says


class Pet():

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def set_owner(self, name=None, phone=None):
        self.owner_name = name
        self.phone = phone

    def __str__(self):
        return f"My name is {self.name} and I am a {self.animal_type.breed}. I have {self.animal_type.leg_num} legs and I say '{self.animal_type.speak()}'. My owner is {self.name}. If I'm lost call {self.phone}"



