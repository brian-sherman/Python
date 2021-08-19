"""
9a.  More Set Examples:

Create a program that uses a set to add values to it.

Example One:
["dog", "lion", "giraffe"] # Expected Output

"""

animals = {"dog", "lion", "giraffe"}

animal = input("Enter an animal: ")
animal = animal.lower()

animals.add(animal)
print(animals)