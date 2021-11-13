while True:
    print("Wake up Neo...\n")
    print("The Matrix has you.\n")
    print("Follow the white rabbit...\n")
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
