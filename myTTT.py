import myAI

class aTTT(object):

    def __init__(self):
        self.myBoard = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]
        self.rowLength = 4
        self.player1sym = 'O'
        self.player2sym = 'X'
        self.myAI = myAI.aAI(self)
        self.nRow = len(self.myBoard)/self.rowLength
        self.nCol = self.rowLength
        print "there are ", self.nRow,"rows and ",self.nCol, " cols"


    def printBoard(self):
        print ''
        for i in range(0, len(self.myBoard)/self.rowLength):
            for j in range (0, self.rowLength):
                print self.myBoard[j+i*self.rowLength],
            print ''

    def indexFromRowCol(self, row, col):
        self.myIndex =  ((self.rowLength*(row))+col)
        if self.myIndex <= len(self.myBoard):
            return self.myIndex
        else:
            print ("index too long")
            raise AttributeError

    def signChoice(self, player, row, col):
        print "inserting data at", row, col
        self.i = self.indexFromRowCol(row,col)
        print "inserting data at index", self.i
        if self.myBoard[self.i] != '_':
            raise IOError
        if player==1:
            self.myBoard[self.i] = self.player1sym
        if player==2:
            self.myBoard[self.i] = self.player2sym
        self.printBoard()

    def askForChoice(self, player):
        print 'players turn!'
        print 'row,col ',
        input = raw_input()
        myString = input.split(',')
        self.row = 1
        self.col = 2
        try:
            self.row = int(myString[0])
            self.col = int(myString[1])
            self.signChoice(player, self.row, self.col)
        except:
            print "something is wrong. please try again!"
            self.askForChoice(player)
            return
        num = self.row+1

        if player == 1:
            #self.askForChoice(2)
            self.myAI.askAiNextMove()
            pass
        if player == 2:
            self.askForChoice(1)




