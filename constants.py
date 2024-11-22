import random

# class for green text
class TerminalColors:
    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    CWHITE = '\33[37m'
    CRED = '\33[31m'

# classes for characters you can choose to play as
class Neo:
    name = "Neo"  # Add name attribute
    health = 40
    strength = 11
    score = 0

class Morpheus:
    name = "Morpheus"  # Add name attribute
    health = 36
    strength = 9
    score = 0

class Trinity:
    name = "Trinity"  # Add name attribute
    health = 37
    strength = 7
    score = 0

# classes for the enemies you will face
class Agent:
    name = "Standard Agent"
    health = 20
    strength = 5
    loot = random.randint(0, 2)

class Sentinel:
    name = "Sentinel"
    health = 15
    strength = 4
    loot = random.randint(0, 2)

class Smith:
    name = "Agent Smith"
    health = 20
    strength = 6
    loot = random.randint(0, 2)
