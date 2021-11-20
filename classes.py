import random

# class for green text

class bcolors:
    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    CWHITE  = '\33[37m'

# classes for characters you can choose to play as


class Neo:
    health = 30
    strength = 5
    defence = 10
    score = 0
    
class Morpheus:
    health = 28
    strength = 7
    defence = 7
    score = 0
    
class Trinity:
    health = 26
    strength = 6
    defence = 8
    score = 0

# classes for the enemies you will face

class Agent:
    name = "Standard Agent"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0, 2)

class Sentinel:
    name = "Sentinel"
    health = 15
    strength = 3
    defence = 3
    loot = random.randint(0, 2)

class Smith:
    name = "Agent Smith"
    health = 20
    strength = 4
    defence = 3
    loot = random.randint(0, 2)

