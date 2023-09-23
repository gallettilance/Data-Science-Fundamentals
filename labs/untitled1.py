#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:39:52 2023

@author: ljialei
"""
class Board:
    def __init__(self):
        self.board = [["_" for _ in range(8)] for _ in range(8)]

    def __repr__(self):
        res = ""

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

    def is_legal_col(self,row,col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                return False
        return True

    def is_on_board(self,row,col):
        return row >= 0 and row < 8 and col >= 0 and col <8

    def is_legal_diag(self,row,col):
        for i in range(len(self.board)):
            if self.is_on_board(row-i, col-i) and self.board[row-i][col-i] == "Q":
                return False
            if self.is_on_board(row-i, col+i) and self.board[row-i][col+i] == "Q":
                return False
            if self.is_on_board(row+i, col-i) and self.board[row+i][col-i] == "Q":
                return False
            if self.is_on_board(row+i, col+i) and self.board[row+i][col+i] == "Q":
                return False
        return True


    def is_legal(self,row,col):
        if not self.is_legal_row(row,col):
            return False
        if not self.is_legal_col(row,col):
             return False
        if not self.is_legal_diag(row,col):
            return False
        return True

    def set_queen_at(self,row,col):
        self.board[row][col] = "Q"

    def unset_queen_on(self,row):
        self.board[row] = ["_" for _ in range(8)]

    def get_queen_on(self,row):
        for col in range(len(self.board)):
            if self.board[row][col] == "Q":
                return col
        raise ValueError("Programming error")

    def search(self):
       
       r = 0
       c = 0
       
       while r < 8:

           if self.is_legal(r,c):
               self.set_queen_at(r,c)
               r += 1
               c = 0
           else:
               c += 1
               while c >= 8:
                   c = self.get_queen_on(r - 1)
                   self.unset_queen_on(r - 1)
                   c += 1
                   r -= 1
       print(self)
       print("found solution")


    def search_all(self):
        row = 0
        col = 0
        sols = 0

        while row >= 0:
            if row < 8:
                if self.is_legal(row,col):
                    self.set_queen_at(row,col)
                    row += 1
                    col = 0
                else:
                    col +=1
                    while col >= 8:
                        if row == 0:
                            row -= 1
                            break
                        col = self.get_queen_on(row-1)
                        self.unset_queen_on(row-1)
                        col += 1
                        row -= 1

            else:
                print("Found a solution")
                sols += 1
                print(self)
                col = self.get_queen_on(row-1)
                self.unset_queen_on(row-1)
                col += 1
                row -= 1

                while col >= 8:
                    col = self.get_queen_on(row-1)
                    self.unset_queen_on(row-1)
                    col += 1
                    row -= 1
                    
        print("No more solutions")
        print("Total solutions:", sols)

my_board = Board()
my_board.search_all()