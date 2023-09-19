class Board:
    def __init__(self):
        self.board =[["_" for _ in range(8)] for _ in range(8)]

    def __repr__(self):
        res = ''
        for row in self.board:
            for col in row:
                res += col
                res += " "
            res += "\n"
        return res
    
    def is_legal_row(self,row,col):
        for j in range(len(self.board)):
            if self.board[row][j] == "Q":
                return False
            return True
    def is_legal_col(self, row, col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                return False
            else:
                return True
            
    def is_on_board(self,row,col):
        return row >= 0 and row < 8 and col >=0 and col <8
            
    def is_legal_diag(self, row, col):
        for i in range(len(self.board)):
            if self.is_on_board(row-i,col-i) and self.board([row-i][col-i]) == "Q": #checks diagonal to top left
                return False
            if self.is_on_board(row-i,col+i) and self.board([row-i][col+i]) == "Q": #checks diagonal to top right
                return False
            if self.is_on_board(row+i,col-i) and self.board([row+i][col-i]) == "Q": #checks diagonal to bottom left
                return False
            if self.is_on_board(row+i,col+i) and self.board([row+i][col+i]) == "Q": #checks diagonal to bottom right
                return False
        return True
    
    def is_legal(self, row, col):
        if not self.is_legal_row(row,col):
            return False
        if not self.is_legal_col(row,col):
            return False
        if not self.is_legal_diag(row,col):
            return False
        return True
    
    def set_queen_at(self, row, col):
       self.board[row][col] = "Q"
    
    def unset_queen_on(self, row):
        self.board[row] = ["_" for _ in range(8)]

    def get_queen_on(self,row):
        for col in range(len(self.board)): 
            if self.board[row][col] == "Q":
                return col
        raise ValueError("programmer error") #happens if we cant find a queen on the row which shouldnt happen in this case
    

    def search(self):
        row = 0
        col = 0
        while row < 8:
            if self.is_legal(row,col):
                self.set_queen_at(row,col)
                row +=1
                col = 0
            else: 
                col +=1
                while col >= 8: #this means we've gotten through every column and no queen has been put on the row, so we go back to the previous row. 
                    col = self.get_queen_on(row-1 )
                    self.unset_queen_on(row-1) #remove the queen on the previous row
                    col +=1
                    row -=1
        print("found a solution")
        print(self) #prints the board with the solution
        while col >= 8: #this means we've gotten through every column and no queen has been put on the row, so we go back to the previous row. 
                    col = self.get_queen_on(row-1 )
                    self.unset_queen_on(row-1) #remove the queen on the previous row
                    col +=1
                    row -=1
      


my_board = Board()
my_board.search()

