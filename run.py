import random
import pyfiglet
import sys
from time import sleep

# class for green text


class bcolors:
    OKGREEN = '\u001b[32m'
    HEADER = '\033[95m'
    CWHITE = '\33[37m'
    CRED = '\33[31m'

# classes for characters you can choose to play as


class Neo:
    health = 40
    strength = 11
    score = 0


class Morpheus:
    health = 36
    strength = 9
    score = 0


class Trinity:
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


def game_over(character, full_health: bool = False):
    """
    Function for when user gets a gameover.
    Either via dying by having health > 1 or if they make a wrong decision
    """
    if full_health:
        # this empty string is to change the colour of the figlet text
        print(bcolors.CWHITE + "")
        gameover = pyfiglet.figlet_format("G A M E _ O V E R", font="alphabet")
        print("\n")
        print(gameover)
        print(bcolors.OKGREEN + "Your final score is", character.score)
        write_score(character.score)

        file = open("score.txt", "r")

        for line in file:
            xline = line.split(",")
            if len(xline) > 1:
                print(xline[0], xline[1])

        exit()

    if character.health < 1:
        print(bcolors.OKGREEN + "You are out of health and about to be"
                                "made slave concubine to the Deus Ex Machina"
                                "for the remainder of your days\n")
        # this empty string is to change the colour of the figlet text
        print(bcolors.CWHITE + "")
        gameover = pyfiglet.figlet_format("G A M E _ O V E R", font="alphabet")
        print("\n")
        print(gameover)
        print(bcolors.OKGREEN + "Your final score is", character.score)
        write_score(character.score)

        file = open("score.txt", "r")
        for line in file:
            xline = line.split(",")
            if len(xline) > 1:
                print(xline[0], xline[1])

        exit()


def write_score(score):
    """
    Function for writing the users final score to the .txt file
    """
    name = input("Type your name to add it to the high score list...")
    print("")
    print("HIGH SCORES")
    print("")
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def hero_select():
    """
    Function for choosing the hero character you wish to play as
    """
    print(bcolors.OKGREEN + "Who would you like to play as?\n")
    selection = input(bcolors.OKGREEN + "1. Neo \n2. Morpheus \n3. Trinity \n")
    if selection == "1":
        character = Neo
        print(bcolors.OKGREEN +
              "You have selected Neo... These are his game stats...\n")
        print(bcolors.OKGREEN + "Health - ", character.health)
        print(bcolors.OKGREEN + "Strength - ", character.strength)
        print("\n")
        return character

    elif selection == "2":
        character = Morpheus
        print(bcolors.OKGREEN +
              "You have selected Morpheus... These are his game stats...")
        print(bcolors.OKGREEN + "Health - ", character.health)
        print(bcolors.OKGREEN + "Strength - ", character.strength)
        print("\n")
        return character

    elif selection == "3":
        character = Trinity
        print(bcolors.OKGREEN +
              "You have selected Trinity... These are her game stats...")
        print(bcolors.OKGREEN + "Health - ", character.health)
        print(bcolors.OKGREEN + "Strength - ", character.strength)
        print("\n")
        return character

    else:
        print(bcolors.CRED + "Input Error! Only press 1,2 or 3")
        print("\n")
        hero_select()


def enemy_select(Agent, Sentinel, Smith):
    """
    Function for randomly selecting
    the enemy you will face
    when a battle occurs
    """
    enemyList = [Agent, Sentinel, Smith]
    chance = random.randint(0, 2)
    enemy = enemyList[chance]
    return enemy


def loot():
    """
    Function for randomly
    selecting the loot the
    enemy will drop after you fight it
    """
    loot = ["Uzi", "Leather Jacket", "Katana"]
    lootChance = random.randint(0, 2)
    lootDrop = loot[lootChance]
    return lootDrop


def loot_effect(lootDrop, character):
    """
    Function to for the
    loot you get adding
    to your characters strength attribute
    """
    if lootDrop == "Uzi":
        character.strength = character.strength + 5
        print(bcolors.OKGREEN +
              "You cock the Uzi and put "
              "it in your jacket! Increasing "
              "your strength by 5")
        print(bcolors.OKGREEN + "Your strength is now",
              character.strength, "\n")
        return character

    elif lootDrop == "Leather Jacket":
        character.strength = character.strength + 10
        print(bcolors.OKGREEN +
              "You put on the leather jacket! Increasing your strength by 10")
        print(bcolors.OKGREEN +
              "Your strength is now",
              character.strength, "\n")
        return character

    elif lootDrop == "Katana":
        character.strength = character.strength + 8
        print(bcolors.OKGREEN +
              "You sheath the katana and strap "
              "it to your back! "
              "Increasing your strength by 8")
        print(bcolors.OKGREEN +
              "Your strength is now",
              character.strength, "\n")
        return character


def battle_state(character):
    """
    Function for the fight sequences
    Random enemy is generated
    You have three options for how to fight
    These options have a hitchance
    that is randomly generated to keep the fights interesting
    Input validation if present if the user doesnt push either 1,2 or 3
    """
    enemy = enemy_select(Agent, Sentinel, Smith)
    # this empty string is to change the colour of the figlet text
    print(bcolors.CWHITE + "")
    result = pyfiglet.figlet_format("F I G H T - M O D E", font="alphabet")
    print("\n")
    print(result)
    print(bcolors.OKGREEN + "")
    print(bcolors.OKGREEN + "Shit!", enemy.name, "just crashed the party...")
    print(bcolors.OKGREEN + "You are probably"
                            "fucked but you have three options...\n")
    print(bcolors.OKGREEN +
          "Type either 1, 2 or 3 on your keyboard to make your selection")
    while enemy.health > 0:
        choice = input(
            "1. Shoot at enemy while holding gun sideways"
            "\n2. Slow-mo dodge the enemy then Kung Fu their ass"
            "\n3. Run for your life\n")

        if choice == "1":
            print(bcolors.OKGREEN + "You let off a clip, riddling",
                  enemy.name, "with bullets")
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print(bcolors.OKGREEN + "You hit", enemy.name,
                      "their health is now =", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - enemy.strength
                    print(bcolors.OKGREEN + enemy.name,
                          "retaliates like a maniac, "
                          "they clobber you! Reducing "
                          "your health to", character.health)
                    game_over(character)

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

                    print(bcolors.OKGREEN + "You kicked the shit out of",
                          enemy.name, "they are very dead... for now")
                    # empty string for color change
                    print(bcolors.CWHITE + "")
                    loot_text = pyfiglet.figlet_format("L O O T - F O U N D",
                                                       font="alphabet")
                    print("\n")
                    print(loot_text)
                    print(bcolors.OKGREEN + "But wait!",
                          enemy.name, "dropped something of value\n")
                    lootDrop = loot()
                    print("You just got a", lootDrop, "\n")
                    loot_effect(lootDrop, character)
                    return character.score
                    break
            else:
                print(
                    bcolors.OKGREEN + "You look class "
                    "holding your gun sideways but "
                    "sadly you miss", enemy.name)
                print(bcolors.OKGREEN + "You have angered",
                      enemy.name, "they attack viciously\n")
                character.health = character.health - enemy.strength
                print(bcolors.OKGREEN +
                      "Your health is now:",
                      character.health)
                game_over(character)

        elif choice == "2":
            print(bcolors.OKGREEN +
                  "You bend backwards in slow motion dodging",
                  enemy.name, "and then let fly with a Kung-Fu kick!")
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print(bcolors.OKGREEN + "You hit", enemy.name,
                      "their health is now =", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - enemy.strength
                    print(bcolors.OKGREEN + enemy.name,
                          "retaliates like a maniac, "
                          "they clobber you! Reducing "
                          "your health to", character.health)
                    game_over(character)

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

                    print(bcolors.OKGREEN + "You kicked the shit out of",
                          enemy.name, "they are very dead... for now\n")
                    # empty string for color change
                    print(bcolors.CWHITE + "")
                    loot_text = pyfiglet.figlet_format("L O O T - F O U N D",
                                                       font="alphabet")
                    print("\n")
                    print(loot_text)
                    print(bcolors.OKGREEN + "But wait!",
                          enemy.name, "dropped something of value\n")
                    lootDrop = loot()
                    print(bcolors.OKGREEN + "You just got a", lootDrop, "\n")
                    loot_effect(lootDrop, character)
                    return character.score
                    break
            else:
                print(bcolors.OKGREEN + "You slip on a banana skin and miss",
                      enemy.name, "with your kick")
                print(bcolors.OKGREEN + enemy.name,
                      "is furious and attacks wildly\n")
                character.health = character.health - enemy.strength
                print(bcolors.OKGREEN +
                      "Your health is now:",
                      character.health)
                game_over(character)

        elif choice == "3":
            print(bcolors.OKGREEN + "You try to run...")
            runchance = random.randint(1, 10)
            if runchance > 4:
                print(bcolors.OKGREEN +
                      "You leg it inside a phonebox and escape")
                break
            else:
                print(
                    bcolors.OKGREEN +
                    "As you try to run, your"
                    "leather snags on something and you slip\n")
                print(bcolors.OKGREEN + enemy.name,
                      "laughs at your cowardice"
                      "and then attacks in a bloodythirsty fashion\n")
                character.health = character.health - enemy.strength
                print(
                    bcolors.OKGREEN +
                    "Your health has taken a whack it is now:",
                    character.health)
                game_over(character)

        else:
            print(bcolors.CRED +
                  "Input Error! You must only type"
                  "the number 1,2 or 3 on the keyboard.\n")


def story_intro():
    """
    Function for the intro to the game with type delay and ascii art
    """
    line1 = "Wake Up.\n"
    line2 = "The Matrix has you.\n"
    line3 = "Follow the white rabbit...\n"
    for char in line1:
        sleep(0.1)
        print(bcolors.OKGREEN + char, end='', flush=True)
    for char in line2:
        sleep(0.1)
        print(bcolors.OKGREEN + char, end='', flush=True)
    for char in line3:
        sleep(0.1)
        print(bcolors.OKGREEN + char, end='', flush=True)
    print(bcolors.CWHITE + """
       /gg\           /gg\\
      /g.gg\         /gg.g\\
     |gg..gg\       /gg..gg|
     |gg...g|       |g...gg|
     |gg...g|       |g...gg|
      \gg..g/       \g..gg/
       |gg.gvgggggggvg.gg|
      /ggggggggggggggggggg\\
     /gggg(((ggggggg)))gggg\\
    |ggggg....ggggg....ggggg|
    |ggggg....ggggg....ggggg|
    |ggcccgggg\___/ggggcccgg|
    |ggcccccgggg|ggggcccccgg|
      \gcccggg\---/gggcccg/
         \ggggggggggggg/
        """)


def choice1(character):
    """
    The first decision point
    of this choose your own
    adventure game with input validation
    """
    answer = input(bcolors.OKGREEN +
                   "Would you like to follow"
                   "the white rabbit?(yes/no)\n").lower().strip()
    if answer.lower().strip() == "yes":
        battle_state(character)

    elif answer == "no":
        print(bcolors.OKGREEN + "that's too bad")
        game_over(character, True)

    else:
        print(bcolors.CRED + "Input Error please type either yes or no")
        choice1(character)


def choice2(character):
    """
    The second decision point of
    this choose your own
    adventure game with input validation
    """
    print(bcolors.OKGREEN +
          "You arrive in a strange "
          "techno club where they are playing Rob Zombie...\n")
    print(bcolors.OKGREEN +
          "A man you have never met "
          "wearing sunglasses invites you to sit down...\n")
    answer = input(bcolors.OKGREEN +
                   "Do you want to take the"
                   "red pill or the blue pill?(red/blue)\n").lower().strip()
    if answer == "red":
        battle_state(character)

    elif answer == "blue":
        print(bcolors.OKGREEN +
              "You wake up the next day in your bed and remember nothing\n")
        game_over(character, True)

    else:
        print(bcolors.CRED + "invalid choice, type either red or blue")
        choice2(character)


def choice3(character):
    """
    The third decision point
    of this choose your own
    adventure game with input validation
    """
    print(bcolors.OKGREEN +
          "The man explains to you that reality is a construct...\n")
    print(bcolors.OKGREEN +
          "He explains that you are potentially a saviour to all mankind...\n")
    answer = input("Do you trust him? (yes/no)\n").lower().strip()

    if answer == "yes":
        print(bcolors.OKGREEN +
              "Good he is going to teach you loads of cool shit...")
        print(bcolors.OKGREEN +
              "But just as he is about to "
              "teach you how to jump over buildings...")
        battle_state(character)

    elif answer == "no":
        print(bcolors.OKGREEN +
              "He senses your distrust and removes your mouth\n")
        print(bcolors.OKGREEN + "He then shoots you in the head\n")
        game_over(character, True)

    else:
        print(bcolors.CRED + "Input Error please type either yes or no")
        choice3(character)


def choice4(character):
    """
    The fourth decision point
    of this choose your own
    adventure game with input validation
    """
    answer = input(bcolors.OKGREEN +
                   "A woman called the Oracle "
                   "asks you if you want to "
                   "risk all for love? (yes/no)\n").lower().strip()
    if answer == "yes":
        print(bcolors.OKGREEN + "She smiles\n")
        print(bcolors.OKGREEN +
              "You brought peace between "
              "Man and Machine. You won the game you legend!")
        game_over(character, True)

    elif answer == "no":
        print(bcolors.OKGREEN + "The oracle thinks you are a prude...\n")
        print(bcolors.OKGREEN + "She stabs you with a bent spoon...\n")
        game_over(character, True)

    else:
        print(bcolors.CRED + "Input Error please type either yes or no")
        choice4(character)


story_intro()
character = hero_select()
choice1(character)
choice2(character)
choice3(character)
choice4(character)
