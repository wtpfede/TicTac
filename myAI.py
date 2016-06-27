
class aAI():
    #AI must be player 2
    def __init__(self,aTTT):
        self.lengthStreak = 3
        self.aTTT=aTTT
        print("printerBoard")

    def askAiNextMove(self):
        print 'AI turn!'
        if self.checkVerticals(0, 0) == False:
            print 'none Found'
            return
        print 'finished AI'
        #print self.aTTT.printBoard()
        self.aTTT.askForChoice(1)


    def checkVerticals(self, row, col):
        #print "AI checkVertical", row, col
        emptyVerticalFound = False
        for colI in range(col,self.aTTT.nCol):
            emptySlotStreak = 0
            alreadyPlacedStreak = 0
            print 'emptiedstreak'
            for rowI in range (0, self.aTTT.nRow):
                print 'hello', rowI, colI
                if(self.aTTT.myBoard[self.aTTT.indexFromRowCol(rowI, colI)] != 'O'):
                    emptySlotStreak +=1
                    if (self.aTTT.myBoard[self.aTTT.indexFromRowCol(rowI, colI)] == 'X'):
                        alreadyPlacedStreak +=1
                    #print "empty streak", + self.emptySlotStreak
            if emptySlotStreak>=self.lengthStreak:
                print "found at", + row +alreadyPlacedStreak, colI
                self.aTTT.signChoice(2, row+alreadyPlacedStreak, colI)
                return True
        return False
