import random

# classes for characters you can choose to play as


class neo (object):
    health = 25
    strength = 5
    defence = 10
    agility = 1
    score = 0


class morpheus (object):
    health = 125
    strength = 7
    defence = 7
    agility = 10
    score = 0


class trinity (object):
    health = 100
    strength = 6
    defence = 8
    agility = 5
    score = 0

# classes for the enemies you will face


class agent (object):
    name = "Standard Agent"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0, 2)


class sentinel (object):
    name = "Sentinel"
    health = 15
    strength = 3
    defence = 3
    loot = random.randint(0, 2)


class smith (object):
    name = "Agent Smith"
    health = 20
    strength = 4
    defence = 3
    loot = random.randint(0, 2)


def gameOver(character, name, full_health = False):

    if full_health:
        print("Game Over")
        print("Your final score is", character.score)
        name = input("Add your name to your score...")
        writeScore(name)

        file = open("score.txt", "r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()

    if character.health < 1:
        print("You are out of health and about to be made slave concubine to the Deus Ex Machina for the remainder of your days\n")
        print("Game Over")
        print("Your final score is", character.score)
        name = input("Add your name to your score...")
        writeScore(name)

        file = open("score.txt", "r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()


def writeScore(name):
    name = ""
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def heroselect():
    print("Who would you like to play as?")
    selection = input("1. Neo \n2. Morpheus \n3. Trinity \n")
    if selection == "1":
        character = neo
        print("You have selected Neo... These are his game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Agility - ", character.agility)
        return character

    elif selection == "2":
        character = morpheus
        print("You have selected Morpheus... These are his game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Agility - ", character.agility)
        return character

    elif selection == "3":
        character = trinity
        print("You have selected Trinity... These are her game stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defence)
        print("Agility - ", character.agility)
        return character

    else:
        print("Input Error! Only press 1,2 or 3")
        heroselect()


def enemyselect(agent, sentinel, smith):
    enemyList = [agent, sentinel, smith]
    chance = random.randint(0, 2)
    enemy = enemyList[chance]
    return enemy


def loot():
    loot = ["Uzi", "Leather Jacket", "Katana"]
    lootChance = random.randint(0, 2)
    lootDrop = loot[lootChance]
    return lootDrop


def lootEffect(lootDrop, character):
    if lootDrop == "Uzi":
        character.strength = character.strength + 5
        print("You cock the Uzi and put it in your jacket! Increasing your health by 5")
        print("Your strength is now", character.strength)
        return character

    elif lootDrop == "Leather Jacket":
        character.agility = character.agility + 10
        print("You put on the leather jacket! Increasing your defense by 10")
        print("Your defense is now", character.defence)
        return character

    elif lootDrop == "Katana":
        character.strength = character.strength + 8
        print(
            "You sheath the katana and strap it to your back! Increasing your strength by 8")
        print("Your strength is now", character.strength)
        return character


def battleState(character):
    enemy = enemyselect(agent, sentinel, smith)
    print("Shit!", enemy.name, "just crashed the party...")
    print("You are probably fucked but you have three options...")
    print("Type either 1, 2 or 3 on your keyboard to make your selection")
    while enemy.health > 0:
        choice = input(
            "1. Shoot at enemy while holding gun sideways\n2. Slow-mo dodge the enemy then Kung Fu their ass\n3. Run for your life\n")

        if choice == "1":
            print("You let off a clip, riddling", enemy.name, "with bullets")
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("You hit", enemy.name,"their health is now =", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - enemy.strength
                    print(enemy.name, "retaliates like a maniac, they clobber you! Reducing your health to", character.health)
                    gameOver(character, name)

                else:
                    if enemy.name == "Standard Agent":
                        enemy.health = 20
                        character.score = character.score + 10

                    elif enemy.name == "Sentinel":
                        enemy.health = 15
                        character.score = character.score + 7

                    elif enemy.name == "Agent Smith":
                        enemy.health = 15
                        character.score = character.score + 13

                    print("You kicked the shit out of", enemy.name,"they are very dead... for now")
                    print("But wait!", enemy.name,"dropped something of value")
                    lootDrop = loot()
                    print("You just got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return character.score
                    break
            else:
                print("You look class holding your gun sideways but sadly you miss", enemy.name)
                print("You have angered", enemy.name, "they attack viciously")
                character.health = character.health - enemy.strength
                print("Your health is now:", character.health)
                gameOver(character, name)

        elif choice == "2":
            print("You bend backwards in slow motion dodging",enemy.name, "and then let fly with a Kung-Fu kick!")
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("You hit", enemy.name,
                      "their health is now =", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - enemy.strength
                    print(enemy.name, "retaliates like a maniac, they clobber you! Reducing your health to", character.health)
                    gameOver(character, name)

                else:
                    if enemy.name == "Standard Agent":
                        enemy.health = 20
                        character.score = character.score + 10
                    

                    elif enemy.name == "Sentinel":
                        enemy.health = 15
                        character.score = character.score + 7

                    elif enemy.name == "Agent Smith":
                        enemy.health = 15
                        character.score = character.score + 13

                    print("You kicked the shit out of", enemy.name,"they are very dead... for now")
                    print("But wait!", enemy.name,"dropped something of value")
                    lootDrop = loot()
                    print("You just got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return character.score
                    break
            else:
                print("You slip on a banana skin and miss",enemy.name, "with your kick")
                print(enemy.name, "is furious and attacks wildly")
                character.health = character.health - enemy.strength
                print("Your health is now:", character.health)
                gameOver(character, name)

        elif choice == "3":
            print("You try to run...")
            runchance = random.randint(1, 10)
            if runchance > 4:
                print("You leg it inside a phonebox and escape")
                break
            else:
                print("As you try to run, your leather snags on something and you slip\n")
                print(enemy.name, "laughs at your cowards and then attacks in a bloodythirsty fashion\n")
                character.health = character.health - enemy.strength
                print("Your health has taken a whack it is now:", character.health)
                gameOver(character, name)

        else:
            print("Input Error! You must only type the number 1,2 or 3 on the keyboard.")


def main_storyline(score):
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
    character = heroselect()
    answer = input("Would you like to follow the white rabbit?(yes/no)\n").lower().strip()
    if answer.lower().strip() == "yes":
        battleState(character)
        print("You arrive in a strange techno club where they are playing Rob Zombie...\n")
        print("A man you have never met wearing sunglasses invites you to sit down...\n")
        answer = input("Do you want to take the red pill or the blue pill?(red/blue)\n").lower().strip()
        if answer == "red":
            print("The man explains to you that reality is a construct...\n")
            print("He explains that you are potentially a saviour to all mankind...\n")
            answer = input("Do you trust him? (yes/no)\n").lower().strip()

            if answer == "no":
                print("He senses your distrust and removes your mouth\n")
                print("He then shoots you in the head\n")
                gameOver(character, name)

            else:
                print("Good he is going to teach you loads of cool shit...")
                print("But just as he is about to teach you how to jump over buildings...")
                battleState(character)
                answer = input("A woman called the Oracle asks you if you want to risk all for love? (yes/no)\n").lower().strip()
                if answer == "yes":
                    print("She smiles\n")
                    print("You brought peace between Man and Machine. You won the game you legend!")

                else:
                    print("The oracle thinks you are a prude...\n")
                    print("She stabs you with a bent spoon...\n")
                    gameOver(character, name, True)

        elif answer == "blue":
            print("You wake up the next day in your bed and remember nothing\n")
            gameOver(character, name, True)

        else:
            print("invalid choice, type one of the options in brackets in the statement above ")

    else:
        print("that's too bad")
        gameOver(character, name, True)


score = 0
name = ""
score = main_storyline(score)
writeScore(name)
