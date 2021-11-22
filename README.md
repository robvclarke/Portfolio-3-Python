# Enter the Matrix - Choose your own adventure game

![Am I responsive](/assets/images/project_image.png)

[Link to live website](https://enter-the-matrix.herokuapp.com/)

A choose your own adventure game based on the sci-fi classic the matrix. 

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

4. Choice 1 

- The first decision point you reach in the game is the same decision Neo has to make in the film 'Do you want to follow the white rabbit?' 
- If you select 'yes' the battle_state() function is triggered and you will fight your first enemy. 
- If you select 'no' the gameover() function is called and you will have a score of '0' which the user can choose to write to the highscore list in the .txt file via the writescore() function within the gameover() function.
- If you type anything other than yes or no their is input validation asking you to type either yes or no and reprompting you to make your decision. 

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


## Testing
### PEP8 Online Code Checker

After correcting lines that were too long and some indentations/white space after text the code in my run.py file passed the Pep8 online code checker with no errors
![Pep8](/assets/images/pep8_testing.png)

The text colors I chose based the lighthouse test for accessibility with an overall score of 98 
![Lighthouse](/assets/images/lighthouse.png)

## Credits

- Code institute gave us the python essentials template which got the terminal into the browser for this project

- Heroku for providing the deployment site

- I used 'Figma' to create the flow chart in this readme

- The 'Love Sandwhiches' code institute essentials project was a great reference when troubleshooting bugs

- Stack Overflow for helping me figure out how to print colored text to the terminal [Stack Overflow](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)

- Stack Overflow for helping me figure out how to have a typing effect in the terminal [Stack Overflow](https://stackoverflow.com/questions/20302331/typing-effect-in-python)

- I used the website 'Am I Responsive' to create the banner image at the top of this readme [Am I responsive?](http://ami.responsivedesign.is)
 
- When I was first trying to get my head around how I might make this game this video was helpful [Youtube Tutorial](https://www.youtube.com/watch?v=DEcFCn2ubSg&t=2s&ab_channel=TechWithTim)

- This series of youtube tutorials provided a good base which I was able to build on when creating my game [Youtube Tutorial](https://www.youtube.com/playlist?list=PLJPiff845eg8hBMJNo6Y2Yo7LKAB8oedh)

- The ASCII art of the white rabbit in the intro section is by Susie Oviatt [Ascii Art](https://www.asciiart.eu/animals/rabbits)

- The Fight-Mode and Game-Over text banners were created using Figlet [Figlet](https://en.wikipedia.org/wiki/FIGlet)

- My mentor Reuben Ferrante for his guidance throughout the project

 