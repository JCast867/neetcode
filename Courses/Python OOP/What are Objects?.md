# What are Obejcts?
An **object** is an instance of a class. It's a specific item created using the blueprint defined by the class.

## Creating Objects
We've seen creating an object before.

```py
class Player:
    def __init__(self, name: str, health: int, speed: int, power: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.power = power
```

We can create an object by calling the class and passing in the required arguments.

```py
# creating player objects
player1 = Player("Steve", 100, 100, 50)
player2 = Player("Bob", 75, 75, 75)
```

When we write `player1 = Player("Steve", 100, 100, 50)`, we're telling Python:
1. Create a new object variable called `player1`
2. Use the `Player` class to create it
3. Set its `name` attribute to `"Steve"`
4. Set its `health` attribute to `100`
5. Set its `speed` attribute to `100`
6. Set its `power` attribute to `50`

## More Example Code

```py
class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

# TODO: Create a pet named "Whiskers" that is a species of 'cat' with hunger level 6 and energy level 8
whiskers = Pet("Whiskers", "cat", 6, 8)

# Don't modify the following code
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
```

