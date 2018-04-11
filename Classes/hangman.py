class Hangman():
    def __init__(self, secretWord):
        self.guesses = 8
        self.secretWord = secretWord

    def printHeader(self, words):
        print '-------------------------------------------------'
        print "Loading word list from file..."
        print words.wordListSize(), "words loaded."
        print "Welcome to the game, Hangam!"
        print "I am thinking of a word that is", len(self.secretWord), "letters long."
        print "-------------------------------------------------"

    def isWordGuessed(self, lettersGuessed):
        # Retorna falso enquanto houver letra na secretWord que nao esta nas lettersGuessed
        for letter in self.secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self,lettersGuessed):
        guessed = ''
        for letter in self.secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += ' _ '
        return guessed

    def getAvailableLetters(self, lettersGuessed):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        return available

    def resultLetter(self, letter, lettersGuessed):
        if letter in lettersGuessed:
            guessed = self.getGuessedWord(lettersGuessed)
            return 'Oops! You have already guessed that letter: ' + guessed

        lettersGuessed.append(letter)
        guessed = self.getGuessedWord(lettersGuessed)

        if letter in self.secretWord:
            return 'Good Guess: ' + guessed

        self.guesses -=1
        return 'Oops! That letter is not in my word: ' + guessed

    def gameResult(self,lettersGuessed):
        if self.isWordGuessed(lettersGuessed):
            return 'Congratulations, you won!'
        else:
            return 'Sorry, you ran out of guesses. The word was ' + self.secretWord + '.'


    def startGame(self):

        lettersGuessed = []
        self.guesses = 8

        while self.isWordGuessed(lettersGuessed) == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            print 'Available letters', self.getAvailableLetters(lettersGuessed)
            letter = raw_input('Please guess a letter: ')

            print self.resultLetter(letter,lettersGuessed)

            print '--------------------------------------------------'

        print self.gameResult(lettersGuessed)
