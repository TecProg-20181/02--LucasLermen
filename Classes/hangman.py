import string

class Hangman():
    def __init__(self):
        self.guesses = 8

    def isWordGuessed(self, secretWord, lettersGuessed):
        secretLetters = []

    #    for letter in secretWord:
    #        if letter in secretLetters:
    #            secretLetters.append(letter)
    #        else:
    #            pass

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True


    def getGuessedWord(self):
         guessed = ''
         return guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase


        return available


    def startGame(self,secretWord):

        lettersGuessed = []
        self.guesses = 8

        while  self.isWordGuessed(secretWord, lettersGuessed) == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            available = self.getAvailableLetters()
            for letter in available:
                if letter in lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')
            if letter in lettersGuessed:

                guessed = self.getGuessedWord()
                for letter in secretWord:
                    if letter in lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! You have already guessed that letter: ', guessed
            elif letter in secretWord:
                lettersGuessed.append(letter)

                guessed = self.getGuessedWord()
                for letter in secretWord:
                    if letter in lettersGuessed:
                        guessed += letter
                    else:
                        guessed += ' _ '

                print 'Good Guess: ', guessed
            else:
                self.guesses -=1
                lettersGuessed.append(letter)

                guessed = self.getGuessedWord()
                for letter in secretWord:
                    if letter in lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! That letter is not in my word: ',  guessed
            print '------------'

        else:
            if self.isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'
