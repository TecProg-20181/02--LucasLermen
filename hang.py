from Classes.words import Words
from Classes.hangman import Hangman

words = Words()
secretWord = words.loadWord().lower()

hangman = Hangman(secretWord)

hangman.printHeader(words)
hangman.startGame()
