class Dog:
    species = "Bulldog"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)


dog1 = Dog("tom", "American Bulldog")
dog2 = Dog("max", "English Bulldog")

print("Details of Dog 1:")
dog1.display()

print("\nDetails of Dog 2:")
dog2.display()
