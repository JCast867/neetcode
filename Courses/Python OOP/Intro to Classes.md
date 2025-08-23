# Intro To Classes
Imagine you have a player. Something you can do to define characteristics of this player. For example:

```py
player1_name = "Steve"
player1_health = 100
player1_speed = 80

player2_name = "Bob"
player2_health = 75
player2_speed = 60
```

This approach has problems. 
1. **Repetition**: You have to define each player individually
2. **Messy Code**: It's hard to keep track of all the player's attributes and their values
3. **Scalability**: What if you want to keep track of 50 players? Your code will be huge and would me unmanageable very quickly

## Classes
A *class* is a blueprint for creating objects. This is the basic syntax for defining a class in Python.

```py
class Player:
    def __init__(self, name: str, health: int, speed: int, power: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.power = power
```

In Python, a class is defined with the keyword `class` followed by the name of the class and a colon. The `__init__` method is a special method that belongs to the class. It creates an object and initializes it's attributes.

Notice that the `__init__` method has an argument `self`. This is required. The `self` variable allows us to add attributes to our object. It also prevents name conflicts, since `name` and `self.name` are different variable.

## More Example Code

```py
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
```
