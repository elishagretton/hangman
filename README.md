# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

I have programmed this game as part of the Software Engineering bootcamp at AiCore.

With this project, I have learned:

- How to build functions to make my code more understandable
- How to refactor my code and use easy-to-understand variable and function names
- How to push new changes to this repository

# Installation

To install this project, please clone this repository and run the hangman_Template.py file.

# Usage

This project can be used to play hangman and learn Python fundamentals.

# File structure of the project
In the milestones folder, there is a python file for each milestone of the AiCore bootcamp walkthrough.

In milestone_2.py, we learned how to generate a random word and then ask for an input. This input had to be alphabetical and a simple character.

In milestone_3.py, we refactored the code into functions so that it is more understandable. We also learned how to do a continuous while loop till a condition is satisifed and check the validity of the input smoothly.

In milestone_4.py, we created the class Hangman and introduced attributes such as: num_lives, word_guessed, num_letters, list_of_guesses. As the user guesses letter, we replace the letters in word_guessed if correct or we take away a life from num_lives.

In milestone_5.py, we created the function play_game() to create an instance of the Hangman game. In this function, we set the instructions on how to win/lose the game. If the num_lives equal 0, they lose. If the user has guessed all the letters, num_letters equals 0 and then the user wins.

# License information
