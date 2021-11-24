# Enter the Matrix - Choose your own adventure game

![Am I responsive](/assets/images/project_image.png)

[Link to live website](https://enter-the-matrix.herokuapp.com/)

A choose your own adventure game based on the sci-fi film classic 'The Matrix'. 

## Table of contents
1. [Project Inspiration](#Project-Inspiration)
2. [UX](#UX)
    * [Site owner goals](#site-owner-goals)
    * [User needs](#user-needs)
3. [Features](#features)
    * [Existing features](#existing-features)
    * [Features left to implement](#fPotential-Future-Features)
4. [Technologies](#Technologies)
5. [Testing](#testing)
    * [User needs](#user-needs)
    * [Challenges](#challenges)
    * [PEP8 Online Code Checker](#PEP8-Online-Code-Checker)
    * [Unfixed bugs](#Unfixed-bugs)
6. [Deployment](#deployment)
7. [Credits](#credits)
    
## Project Inspiration

For a lot of people of my generation, when we think of a computer terminal it is synonymous with the classic opening scene of the film 'The Matrix' with the classic lines:

Wake up, Neo...
The Matrix has you...
Follow the white rabbit..

Appearing on the screen as the main character Neo's computer is hacked.

![Scene from the matrix](/assets/images/follow_the_white_rabbit.png)

[Watch the White Rabbit Scene in the Matrix on Youtube](https://www.youtube.com/watch?v=6IDT3MpSCKI&ab_channel=TheMatrixFan314)

I decided I wanted to make a choose your own adventure game based on this classic scene and some other seminal scenes from the film as I felt it was a cool theme to explore and a fun way to try put my python skills to the test.

## UX

### Site Owners Goals

The objectives of the site owner are: 
1. To create an intuitive, command line programme, that sticks to good UX Principles while being a fun game to play. 
2. To create a programme that shows off the python skills I have learned in this course. 
3. To create a choose your own adventure game with input validation, multiple choice and randomly generated enemies, rewards and fights.

### User Needs

1. To have their curiosity picked by the opening Alice in Wonderland style call to action
2. To find the programme easy to play
3. To find the choices they take interesting and reward their knowledge of the Matrix film. 
4. To play a game with a variety of decision points, enemies and rewards so it has replayability.
5. To be able to log their final score and see the HIGH SCORE list of other players.

## Features

### Existing Features

1. Structure and formatting

- I used a green font to align with the style of the terminal that appears in the matrix film. I used white for the 'white rabbit' ascii illustration as I felt it was natural and then white for the Fight Mode Pfiglet Fonts. I used red for the error messages to make them stand out. 

- I created a flow diagram at the beginning of the project to guide the code and help me plan out the game 

![Flow Chart](/assets/images/data_model.jpg)

[Link to the Figma File where I created the flow chart](https://www.figma.com/file/TMEWK4XjZFX8ABdLRUKPY8/Flow-Chart?node-id=0%3A1)

2. Intro to the story

- The intro text is the exact text that Neo sees appear on his screen at the start of the film. Like in the film what is happening is still a mystery at this point. The user is told to follow the white rabbit down the rabbit hole like alice in wonderland if they are curious.

- I imported sys and sleep and used the time delay to make the text appear as if it is being typed like in the film and create the sense that you are having a real time conversation with the machine.

- I used color classes to make the text in the terminal appear green

- I used an ascii art illustration for the white rabbit that appears which I have credited in the 'credits' section of this readme

![Intro Section](/assets/images/intro_section.png)

3. Selecting your Character

- You have three options for the character you wish to play the game. They are the main characters from the film. Neo, Morpheus and Trinity. Each have their own stats for health/strength which effect your ability to fight the enemies you will encounter in the game. Each character starts off with a score of zero. 

- These attributes are printed out once you make your selection.

![Selecting your Character](/assets/images/character_select.png)

- the user makes their selection by typing either 1,2 or 3 in on their keyboard. If they type anything else input validation throws up an error message in red and reprompts them to enter a valid choice.

![Error Validation](/assets/images/error_validation.png)

4. Choice Sections 

- The first decision point you reach in the game is the same decision Neo has to make in the film 'Do you want to follow the white rabbit?' 
- If you select 'yes' the battle_state() function is triggered and you will fight your first enemy. 
- If you select 'no' the gameover() function is called and you will have a score of '0' which the user can choose to write to the highscore list in the .txt file via the writescore() function within the gameover() function.
- If you type anything other than yes or no their is input validation asking you to type either yes or no and reprompting you to make your decision. 
- The other four choices that occur in the game are structured the same except the final 'choice4' does not trigger a fight mode which is shown in the flow diagram above.

![choice1](/assets/images/choice1.png)

5. Fight Mode

- The fight modes are triggered by the battlestate() function which randomly generates an enemy using the random module to select from the three enemy classes I created which represent bad guys that appear in the Matrix film. 

![Fight Mode](/assets/images/fight_mode.png)

- the fight mode text illustration is generated using Figlet

- You can type either 1,2 or 3 on the keyboard for a choice of 2 attacks and 1 option to try run away. All of these have a randomly generated likelyhood of whether they will connect or not generated via the hitchance variable and the random module.
If you miss you don't remove any enemy health. 
Each time you connect you take health off the enemy and then he retaliates taking health off of you. If you health drops to zero or below it is a gameover. A while loop keeps the fight going until either your health is zero or the enemies health is zero. 

- There is input validation if you enter anything other than 1,2 or 3 into the keyboard.

![Fight Mode 2](/assets/images/fight_mode_two.png)

- Depending on which enemy you have defeated your characters score increases appropriatley which will then be printed out to you at the end of the game where you can add it to the high score list 

- Your score however will run increase if you choose to just run away from your enemy

6. Loot items

- Each enemy carries a loot of either an uzi, a leather jacket or a katana. Each increase your characters strength by different amounts. Which loot they carry is selected using the random module and after you defeat them they drop it via the lootDrop() function called at the end of battlestate.

![Loot Drop](/assets/images/loot_feature.png)

7. Game Over

- When a users health goes to zero the gameover function declares that it is gameover with a figlet text banner. The users final score is printed to the screen.

- A game over can also be triggered if the user has made an incorrect decision at a choice point and this is differentiated in my code through the use of a boolean to account for when the users health is not 0 as in the case of a wrong decision. 

![Gameover](/assets/images/game_over.png)

8. Writing your score/viewing high scores

- The write score function is called within gameover which allows the user to add their name to their final score. 
- The game over function then prints out this list for the user so they can compare their score to their previous one or other peoples scores who have played the game. 

![Gameover](/assets/images/write_score.png)

### Potential Future Features

- If I had more time I would have liked to have made a shop where you could potentially visit to buy and sell items which would increase your stats.

- I would like to have the high score list appear in order of 'Top to Bottom' highest scores when it is printed out at the end. 

## Technolgies

Key technologies used to create this game are shown below:

- [Python 3](https://www.python.org/downloads/) used to programme the game
- [Gitpod](https://gitpod.io/) used for version control and coding the project
- [Heroku](https://www.heroku.com) used to deploy the application
- [Github](https://github.com) used to host the repository
- [Figma](https://www.figma.com/) was used to create the flowchart in the readme
- [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) provided by the code institute was used to display the terminal on the webpage via Heroku
- [Random](https://docs.python.org/3/library/random.html) module was used to create randomly selected enemies, loot and success in the fight mode
- [Time](https://docs.python.org/3/library/time.html) Module was used to create the typing effect in the intro
- [Figlet](http://www.figlet.org/) used to create the text banners

## Testing

### User Needs

I will now go through my user needs and how my application is meeting them: 

1. To have their curiosity picked by the opening Alice in Wonderland style call to action

I feel like this goal is being achieved via the use of the exact dialogue that appears in the film, the type delay effect making it seem like it is happening in real time and the colors in the terminal being in line with what appears in the film. 

2. To find the programme easy to play

Playing the game requires just simple keyboard inputs like (yes/no) or (1,2,3) and error validation occurs if users stray from these. I feel like when the user makes a wrong decision and the game ends there is a humorous pay off in the script that means they want to play again. 

3. To find the choices they take interesting and reward their knowledge of the Matrix film. 

The choices that result in continuation or death in the game might seem arbitrary if you are not familiar with the film but they follow the choices of the main protagonist in the original motion picture. You have to take the red pill, trust Morpheus and ultimatley risk everything for love in order to complete the game just like Neo had to in the film. 

4. To play a game with a variety of decision points, enemies and rewards so it has replayability.

The game has multiple decision points, three different enemies which are randomly selected each time you enter Fight Mode and a humours take on the matrix universe which I feel will lend the game to having replayability. 

5. To be able to log their final score and see the HIGH SCORE list of other players.

Users are able to have their high score logged to the .txt file and see the file printed out with other peoples scores each time they get a game over which makes the game competitive with both you yourself and others. 

### Challenges

1. I intially had all my decision points in a function called main_storyline() but I kept getting trapped in the while loops
and thus had no input validation for when users entered something other than what was requested. I split these out into a seperate function for each decision point and thus was able to have input validation with error messaging.

![Input Validation Code](/assets/images/input_validation_code.png)

2. There is two types of gameover. When you die as a result of running out of health and when you die as a result of making a wrong decision in the game. Figuring out how to trigger the gameover function in both instances was challenging with my eventual solution using a boolean to solve it and indicating it was true when a game over was triggered not as a result of low health. 

![Gameover Code](/assets/images/gameover_code.png)

3. I initially had the score as a global variable that I was passing into the functions but it was resulting in errors so I switched to the score being an attribute of the character objects that gets added to and this worked with the score carrying over with the character. 

![Score code](/assets/images/score_code.png)

4. The trickiest bug I encountered was occasionally my character object attributes were not being found but then if I ran the code and did the exact same thing the bug would not appear so was very confusing to me. 

![Tricky Bug](/assets/images/tricky_bug.png)

I ended up changing the function for when you select your character to the below and managed to resolve this via having the character initally = none and then using a while not statement.

![Solution](/assets/images/character_code.png)

### PEP8 Online Code Checker

After correcting lines that were too long and some indentations/white space after text the code in my run.py file passed the Pep8 online code checker with no errors
![Pep8](/assets/images/pep8_testing.png)

The text colors I chose based the lighthouse test for accessibility with an overall score of 98 
![Lighthouse](/assets/images/lighthouse.png)

### Unfixed bugs

There are not any bugs left in the application that I am aware of. 

## Deployment 

The deployment of my application was done in the following way:

1. Push the latest version of my code to the project repo in Github
2. Make sure all requirements will be accounted for when it is in heroku by entering 'pip install -r requirements.txt'
3. Push again to make sure these requirments have been sent to Github
4. Login to the Heroku website
5. Create a new app
6. Add a name and region for the app
7. Once the app has been created go into the settings tab
8. Click on Reveal Config Vars
9. For the key add 'PORT' and for the value add '8000'
10. Add a buildpack and choose python. Then repeat this step for Node.js
11. Go into the deploy tab
12. For deployment method you want to select Github, it will then say connected
13. Connect the correct repo in github by searching for it in the bar provided
14. Enable Automatic deploys
15. Any time new code is pushed to github it will then automatically build in Heroku
16. You can click open app on the application page in heroku to view it and it will open in a new tab

My deployed site is viewable at: [My Live Site](https://enter-the-matrix.herokuapp.com/)


## Credits

- Code institute gave us the python essentials template which got the terminal into the browser for this project

- Heroku for providing the deployment site

- I used 'Figma' to create the flow chart in this readme

- The 'Love Sandwhiches' code institute essentials project was a great reference when troubleshooting bugs and deploying to Heroku. 

- Stack Overflow for helping me figure out how to print colored text to the terminal [Stack Overflow](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)

- Stack Overflow for helping me figure out how to have a typing effect in the terminal [Stack Overflow](https://stackoverflow.com/questions/20302331/typing-effect-in-python)

- I used the website 'Am I Responsive' to create the banner image at the top of this readme [Am I responsive?](http://ami.responsivedesign.is)
 
- When I was first trying to get my head around how I might make this game this video was helpful [Youtube Tutorial](https://www.youtube.com/watch?v=DEcFCn2ubSg&t=2s&ab_channel=TechWithTim)

- This series of youtube tutorials provided a good base which I was able to build on when creating my game [Youtube Tutorial](https://www.youtube.com/playlist?list=PLJPiff845eg8hBMJNo6Y2Yo7LKAB8oedh)

- The ASCII art of the white rabbit in the intro section is by Susie Oviatt [Ascii Art](https://www.asciiart.eu/animals/rabbits)

- The Fight-Mode and Game-Over text banners were created using Figlet [Figlet](https://en.wikipedia.org/wiki/FIGlet)

- My mentor Reuben Ferrante for his guidance throughout the project

- My girlfriend Anne for being understanding about me spending all my weekends doing this course.

 