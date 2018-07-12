from pet import Pet
from dog import Dog


german_shepherd = Dog("German Shepherd")
rudy = Pet("Rudy", german_shepherd)

rudy.set_owner("Sean Irwin", "999-999-9999")

print(rudy)
