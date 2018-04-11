import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
        self.__inFile = ''
        self.__line = ''
        self.__wordlist = ''

    def loadWord(self):
        # inFile: file
        self.__inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.__line = self.__inFile.readline()
        self.__wordlist = string.split(self.__line)
        return random.choice(self.__wordlist)

    def wordListSize(self):
        return len(self.__wordlist)
