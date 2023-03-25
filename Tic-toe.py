

>>>  class Player:
...     def __init__(self,name,age,symbol):
...         self.name = name
...         if age < 18 : raise Exception("Cannot be a minor")
...         else : self.age = age
...         self.symbol = symbol
...         self.score = 0
... 
...     def associate_board(self,b):
...         self.board = b
...         
...     def make_move(self):
...         vals = input(self.name + " enter x(0,1,2),y(0,1,2) co-ordinates:")
...         vals = vals.split()
...         x = int(vals[0])
...         y = int(vals[1])
...         self.board.mark_symbol(x,y)
...         #how to make move on board
...  class Board:
...     def __init__(self,p1,p2):
...         self.grid = [['-','-','-'],['-','-','-'],['-','-','-']]
...         self.player1 = p1
...         self.player2 = p2
...         self.activePlayer = p1
...         self.totalmoves = 0
...         self.status = 'ongoing'
... 
...     def reset(self):
...         self.grid = [['-','-','-'],['-','-','-'],['-','-','-']]
...         self.totalmoves = 0
... 
...     def isValidMove(self,x,y):
...         return self.grid[x][y] == '-'
... 
...     def status(self):
...         
...         if self.totalmoves == 9 : self.status = 'draw'
...         
... 
...     def mark_symbol(self,x,y):
...         if self.isValidMove(x,y) :
...             self.grid[x][y] = self.activePlayer.symbol
...             if self.activePlayer == self.player1 : self.activePlayer = self.player2
...             else : self.activePlayer = self.player1
...             self.totalmoves += 1
...         else : raise Exception("Cell already taken")
... 
...     def print(self):
...         for i in self.grid:
...             for j in i : print(j,end=' ')
...             print()
def main():
    p1 = Player('hari',22,'X')
    p2 = Player('giri',23,'O')
    b = Board(p1,p2) #aggregation
    p1.associate_board(b)
    p2.associate_board(b)
    for i in range(4):
        p1.make_move()
        b.print()
        p2.make_move()
