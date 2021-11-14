import random

# good character classes
class Neo (object):
    health = 150
    strength = 10
    defence = 10
    magic = 1

class Morpheus (object):
    health = 125
    strength = 7 
    defence = 7
    magic = 10

class Trinity (pbject):
    health = 100
    strength = 6
    defence = 8
    magic = 5


#bad guy classes

class Agent (object):
    name = "Standard Agent"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0,2)

class Sentinel (object):
    name = "Sentinel"
    health = 15
    strength = 3
    defence = 3
    loot = random.randint(0,2)
    

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

main_storyline()
