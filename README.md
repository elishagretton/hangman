# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

I have programmed this game as part of the Software Engineering bootcamp at AiCore.

With this project, I have learned:

- How to create the class Hangman
- How to organise my class into functions like check_letter and ask_letter to make my code easy to understand
- How to use an instance of the Hangman class to create the game
- How to create a README.md file
- How to write docstrings
- And finally, I have learned how to push changes to GitHub!

# Installation

To install this project, please clone this repository and run the hangman_Template.py file to play the game.

# Usage

To use this project, run the hangman_Template.py.

The game will prompt you to guess letters. Keep on guessing till you run out of lives, or till you guess the word right!

# File structure of the project

To view and play the final version of the game, please go to the hangman folder and run the hangman_Template.py file. This puts together all of the skills learned from the Milestone Mini Projects from the AiCore Software Engineering Bootcamp.

To view the milestones, go to the milestones folder.

In milestone_2.py, we learned how to generate a random word and then ask for an input. This input had to be alphabetical and a simple character.

In milestone_3.py, we refactored the code into functions so that it is more understandable. We also learned how to do a continuous while loop till a condition is satisifed and check the validity of the input smoothly.

In milestone_4.py, we created the class Hangman and introduced attributes such as: num_lives, word_guessed, num_letters, list_of_guesses. As the user guesses letter, we replace the letters in word_guessed if correct or we take away a life from num_lives.

In milestone_5.py, we created the function play_game() to create an instance of the Hangman game. In this function, we set the instructions on how to win/lose the game. If the num_lives equal 0, they lose. If the user has guessed all the letters, num_letters equals 0 and then the user wins.

The final hangman_Template.py file is an improved version of milestone_5.py. It has more clear docstrings and better function names.

# License information

This projected is licensed by the MIT license. Please go to LICENSE.txt for more information.
