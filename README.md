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

- 