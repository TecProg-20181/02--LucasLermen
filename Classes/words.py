import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.wordDifLetters = []

    def loadWord(self):
        # inFile: file
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)

        chosenWord = random.choice(self.wordlist)
        self.differentLetters(chosenWord)

        return chosenWord

    def wordListSize(self):
        return len(self.wordlist)

    def differentLettersSize(self):
        return len(self.wordDifLetters)

    def differentLetters(self, chosenWord):
        for letter in chosenWord:
            if letter in self.wordDifLetters:
                pass
            else:
                self.wordDifLetters.append(letter)
