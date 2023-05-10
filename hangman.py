print(
    """
                                                  __________ 
 _   _                                           |       |
| | | |                                          |      ( )
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __    |      /|\ 
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   |     / | \  
| | | | (_| | | | | (_| | | | | | | (_| | | | |  |      / \ 
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  |     /   \ 
                    __/ |                        |\ 
                   |___/                         |_\__________                                     

Create by: Mitchell Burcheri
Date created: 10/5/23
"""
)
print(
    """
Rules:

1. Select a word to guess
2. Type 1 letter in and click enter (the first alphabetic character is used)
3. Try to guess the correct letters to save the hangman from being hung.
4. If you guess the word before the hangman is hung you win. Otherwise you lose.
5. Enjoy!

"""
)

import re


class hangman_character:
    stick = 0
    hung = False

    def __init__(self):
        pass

    def add_stick(self):
        self.stick = self.stick + 1

    def show_figure(self):
        if self.stick == 0:
            print(
                """
 



 



     
            """
            )
        elif self.stick == 1:
            print(
                """
 



 



    ____________    
            """
            )
        elif self.stick == 2:
            print(
                """

    |
    |
    |
    |  
    |
    |
    |
    |____________   
            """
            )
        elif self.stick == 3:
            print(
                """

    |
    |
    |
    |
    |
    |
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 4:
            print(
                """
    ___________ 
    |
    |
    |
    |
    |
    |
    |\ 
    |_\__________ 
            """
            )
        elif self.stick == 5:
            print(
                """
    ___________ 
    |
    |       ( )
    |
    |   
    |      
    |     
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 6:
            print(
                """
    ___________ 
    |  
    |       ( )
    |        | 
    |        |  
    |     
    |     
    |\ 
    |_\__________   
            """
            )
        elif self.stick == 7:
            print(
                """
    ___________ 
    |        
    |       ( )
    |       /|
    |      / | 
    |           
    |      
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 8:
            print(
                """
    ___________ 
    |           
    |       ( )
    |       /|\ 
    |      / | \  
    |     
    |     
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 9:
            print(
                """
    ___________ 
    |     
    |       ( )
    |       /|\ 
    |      / | \  
    |       /
    |      /  
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 10:
            print(
                """
    ___________ 
    |       
    |       ( )
    |       /|\ 
    |      / | \  
    |       / \ 
    |      /   \ 
    |\ 
    |_\__________    
            """
            )
        elif self.stick == 11:
            self.hung = True
            print(
                """
    ___________ 
    |        |
    |       (_)
    |       /|\ 
    |      / | \  
    |       / \ 
    |      /   \ 
    |\ 
    |_\__________ 
       GAME OVER   
            """
            )
        else:
            print("THERE SEEMS TO BE AN ISSUE WITH THE DRAWING")

    def reset(self):
        self.stick = 0
        self.hung = False


def display_guessed():
    print()
    hangman.show_figure()
    print()
    print()
    print("Word to guess: " + str(hidden_word))
    print("Wrong guesses: " + str(wrong_guesses))
    print()


hangman = hangman_character()
word = str(input("Please type a word: ")).upper()  # Collect user word
print()
wrong_guesses = []

hidden_word = []
for i in word:
    hidden_word.append("_")

hangman_hung = False
win = False

for i in range(30):
    print()

display_guessed()

while hangman_hung == False and win == False:
    letter = str(input("Take a guess: ")).upper()

    if letter in word:
        if letter in hidden_word:
            display_guessed()
            print("The letter '" + str(letter) + "' has already been found.")
        else:
            for i, letter_in_enumerate in enumerate(word):
                if letter == letter_in_enumerate:
                    hidden_word[i] = letter
            display_guessed()
            print("'" + str(letter) + "' is a correct letter.")
    else:
        if letter not in wrong_guesses:
            wrong_guesses.append(letter)
            hangman.add_stick()
            display_guessed()
            print("'" + str(letter) + "' is a wrong letter.")
        else:
            display_guessed()
            print("The letter '" + str(letter) + "' has already been guessed.")
    print()

    if "_" not in hidden_word:
        print("You correctly guessed the word '" + str(word) + "'!")
        print("Congratulations, you won!")
        print()
        win = True

    hangman_hung = hangman.hung
    if hangman_hung:
        print("GAME OVER. The word to guess was '" + str(word) + "'.")
        print()
