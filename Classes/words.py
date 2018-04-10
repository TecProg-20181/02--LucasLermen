import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
        self.inFile = ""
        self.line = ""
        self.wordlist = ""

    def loadWord(self):
        # inFile: file
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)
        return random.choice(self.wordlist)

    def wordMessage(self,secretWord):
        print '-------------------------------------------------'
        print "Loading word list from file..."
        print len(self.wordlist), "words loaded."
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(secretWord), 'letters long.'
        print '-------------------------------------------------'
