from random import randint

class hangman:

    def __init__(self,score,word,display):
        self.score=score
        self.word = word
        self.display = display
    
    def setDisplay(self,letter):
        for i in xrange(0,len(self.display)):
            if letter == self.word[i]:
                self.display = self.display[:i] + letter + self.display[i+1:]

    def findLetter(self,letter):
        if letter in self.word:
            self.setDisplay(letter)
            #print self.display
            return True
        else:
            self.wrongGuesses()

    def wrongGuesses(self):
        self.score=self.score-1

    def printScore(self):
        print self.score

    def getScore(self):
        return self.score

if __name__ == "__main__":
    #set up words and choose a word in random
    words = ["what is up","hello","hacking","rutgers","when did you","happy","happy feet","tomorrow","dragon ball z"]
    wordindex = randint(0,len(words)-1)
    word = words[wordindex]
    #set up display
    if ' ' in word:
        display = '_'*len(word.split()[0]) + ' ' + '_'*len(word.split()[1])
    else:
        display = '_'*len(word)
    a = hangman(8,word,display)
    letter=""
    while a.getScore()>0:
        print a.display
        if a.display.count('_')==0:
            print "All Done!"
            break
        letter = raw_input("Enter a letter: ")
        a.findLetter(letter)
        a.printScore()

