import random

class Hangman():
    """
    This class is used to represent the main functions for the Hangman game.

    Attributes:
        word_list (list): the list of words to choose from
        num_lives (int): the number of lives
        word (str): the chosen word for the game
        word_guessed (list): the list of empty spaces representing letters to be guessed in the word
        num_letters (int): the number of letters left to guess in the word
        list_of_guesses (list): a list to keep track of previous guessed letters

    """
    def __init__(self, word_list, num_lives):
        """
        See help(Hangman) for accurate signature.
        """
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        """
        This function checks the guess is in the word.

        Args:
            guess (str): the guessed letter from the user

        """
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in word.')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i]=guess
                    self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        """
        The function asks the user to guess a letter and then checks the guess is a single alphabetical letter.
        
        """
        print('word',self.word)
        guess = input('Guess a letter: ')
        if not guess.isalpha():
            print('Invalid letter. Please, enter a single alphabetical character')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    """
    This function runs the Hangman game.

    It creates an instance of the Hangman class and then sets the conditions for winning the game.

    Args:
        word_list (list): a list of words to choose from
        
    """
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            print('second loop')
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

word_list = ['apple','bananas','grapes','kiwis']

play_game(word_list)