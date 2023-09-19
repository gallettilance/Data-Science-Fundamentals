class Board:

    def __init__(self) -> None:
        self.board = [["_" for _ in range(8)] for _ in range(8)]
        

    def __repr__(self):
        res = ""
        for row in self.board:
            for col in row:
                res += col
                res += " "
            res += "\n"
        return res
    
    def search(self):
        row = 0
        col = 0


        while row >=0:
            if row < 8:
                if self.isLeagal(row,col):
                    self.setQueenAt(row,col)
                    row += 1
                    col = 0
                else:
                    col += 1
                    while col >= 8:
                        col = self.getQueenOn(row - 1)
                        self.unsetQueenOn(row - 1)
                        col += 1
                        row -= 1
            else:
                print("found solution")
                print(self)
                while col >= 8:
                        col = self.getQueenOn(row - 1)
                        self.unsetQueenOn(row - 1)
                        col += 1
                        row -= 1

            print("No more solution")     



    def isLegalRow(self,row,col):
        for j in range(len(self.board)):
            if self.board[row][j] == "Q":
                return False
        return True
        
    def isLegalCol(self,row,col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                return False
        return True

    def isOnBoard(self,row,col):
        return row>= 0 and row < 8 and col >=0 and col <8    
        
    def isLegalDiag(self,row,col):
        for i in range(len(self.board)):
            if self.isOnBoard(row-i, col-i) and self.board[row-i][col-i] == "Q":
                return False
            if self.isOnBoard(row-i, col+i) and self.board[row-i][col+i] == "Q":
                return False
            if self.isOnBoard(row+i, col-i) and self.board[row+i][col-i] == "Q":
                return False
            if self.isOnBoard(row+i, col+i) and self.board[row+i][col+i] == "Q":
                return False
        return True


    def isLeagal (self, row, col):
        if not self.isLegalRow(row,col):
            return False
        if not self.isLegalCol(row,col):
            return False
        if not self.isLegalDiag(row,col):
            return False
        return True 
    


    def setQueenAt(self, row, col):
        self.board[row][col] = "Q"

    def unsetQueenOn(self, row):
        self.board[row] = ["_" for _ in range(8)]

    def getQueenOn(self, row):
        for col in range(len(self.board)):
            if self.board[row][col] == "Q":
                return col
        return ValueError("program Error")



my_baord = Board()
my_baord.search()

