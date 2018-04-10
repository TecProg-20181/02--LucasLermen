from Classes.words import Words
from Classes.hangman import Hangman

words = Words()
hangman = Hangman()

secretWord = words.loadWord().lower()

words.wordMessage(secretWord)
hangman.startGame(secretWord)
