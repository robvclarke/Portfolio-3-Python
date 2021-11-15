import random

# good character classes
class neo (object):
    health = 150
    strength = 10
    defence = 10
    magic = 1

class morpheus (object):
    health = 125
    strength = 7 
    defence = 7
    magic = 10

class trinity (object):
    health = 100
    strength = 6
    defence = 8
    magic = 5


#bad guy classes

class agent (object):
    name = "Standard Agent"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0,2)

class sentinel (object):
    name = "Sentinel"
    health = 15
    strength = 3
    defence = 3
    loot = random.randint(0,2)

class smith (object):
    name = "Agent Smith"
    health = 20
    strength = 4
    defence = 3
    loot = random.randint(0,2)

def heroselect():
    print("Who would you like to play as?")
    selection = input("1. Neo \n2. Morpheus \n3. Trinity \n")
    if selection == "1":
        character = neo
        print("You have selected Neo... These are his game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = morpheus
        print("You have selected Morpheus... These are his game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = trinity
        print("You have selected Trinity... These are his game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Magic - ", character.magic)
        return character

    else:
        print("Input Error! Only press 1,2 or 3")
        heroselect()

def enemyselect(agent,sentinel,smith):
    enemyList = [agent,sentinel,smith]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["Uzi","Leather Jacket","Katana"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def battleState(): 
    enemy = enemyselect(agent,sentinel,smith)
    print("Shit!", enemy.name, "just crashed the party...")
    print("You are probably fucked but you have three options...")
    while enemy.health > 0 : 
        choice = input("1. Shoot at enemy while holding gun sideways\n2. Slow-mo dodge the enemy then Kung Fu their ass\n3. Run for your life\n")

        if choice == "1":
            print("You let off a clip, riddling", enemy.name,"with bullets")
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("You hit," enemy.name, "their health is now =", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print (enemy.name, "retaliates like a maniac, they clobber you! Reducing your health to", character.health)

                else:
                    if enemy.name == "Standard Agent":
                        enemy.health = 20
                    
                    elif enemy.name == "Sentinel":
                        enemy.health = 15
                    
                    elif enemy.name == "Agent Smith":
                        enemy.health = 15
                    
                    print("You kicked the shit out of", enemy.name,"they are very dead... for now")
                    print("But wait!", enemy.name,"dropped something of value")
                    

def main_storyline():
    while True:
        print("Wake Up.\n")
        print("The Matrix has you.\n")
        print("Follow the white rabbit...\n")
        print("""
       /gg\           /gg\ 
      /g.gg\         /gg.g\ 
     |gg..gg\       /gg..gg| 
     |gg...g|       |g...gg| 
     |gg...g|       |g...gg| 
      \gg..g/       \g..gg/ 
       |gg.gvgggggggvg.gg| 
      /ggggggggggggggggggg\ 
     /gggg(((ggggggg)))gggg\ 
    |ggggg....ggggg....ggggg| 
    |ggggg....ggggg....ggggg| 
    |ggcccgggg\___/ggggcccgg| 
    |ggcccccgggg|ggggcccccgg| 
      \gcccggg\---/gggcccg/ 
         \ggggggggggggg/
        """)
        answer = input("Would you like to follow the white rabbit?(yes/no)\n")

        if answer.lower().strip() == "yes":

            answer = input("Would you like to follow it left or right?(left/right)\n").lower().strip()
            if answer == "left":
                answer = input("You encounter an agent, would you like to run or attack?\n")

                if answer == "attack":
                    print("that was not the greatest idea, you lost")
                else:
                    print("good choice you made it away")

                    answer = input("Another agent appears in the distance and fires a gun at you? Do you try and dodge it or run? (dodge/run)\n").lower().strip()

                    if answer == "run":
                        print("You can't outrun a bullet... Game over\n")
                    else:
                        print("You dodged the bullet and brought peace between Man and Machine. You won the game you legend! The game will start over below\n")


            elif answer == "right":
                print("You chose the wrong hole. Game Over\n")

            else: 
                print("invalid choice, you lost")


        else:
            print("that's too bad")
            break

#main_storyline()
battleState()

