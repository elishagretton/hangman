import random

class Hangman():
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        
    def check_guess(self, guess):
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
        while True:
            guess = input('Guess a letter: ')
            if not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ['apple','banana','grapes','strawberries','kiwis']
hangman = Hangman(word_list, 5)
hangman.ask_for_input()