
import random
from location import *
import my_utilities

class GameCharacter:
    def __init__(self):
        self.health = random.randint(10,30)
        self.name = GameCharacter.GenName() 
           
    def GenName():
        First_Name = ["Katreen","Peter","Jason","Jeremy","Bisho","Randa","Tommy","Fefe","Lolo","Evon", "Maria"]
        Last_Name = "Farah Amin Mamdouh Rasmy Jay Jim Roy Alex Jax ".split()
        FirstPiece = First_Name[random.randint(0,len(First_Name)-1)] 
        LastPiece = Last_Name[random.randint(0,len(Last_Name)-1)]
        Name = FirstPiece +" "+ LastPiece
        return Name

class Actor:
    def __init__(self, fc, bc, sym):
        self.row = 0
        self.row = 0
        self.forecolor = fc
        self.backcolor = bc
        self.symbol = sym
    def Interact(self, other_actor, board, hud):
        pass
    
    def Death(self, board, hud):
        board.game_board[self.row][self.col].occupied = None
        #board.game_board[self.row][self.col].Tile() 

        pass

    def PlaceActor (self, board):
        while True:
            row = random.randint(0,len(board)-1)
            col = random.randint(0,len(board[0])-1)
            if board[row][col].passable == True:
                break
        self.row = row
        self.col = col
        board[self.row][self.col].occupied = self

   
class Monster(GameCharacter, Actor):
    def __init__(self, health, monster_type, defense):
        super().__init__()  
        super(GameCharacter, self).__init__("Red", "Black", "M")
        self.health = health
        self.monster_type = monster_type
        self.defense = random.randint(0,10)

    def Death(self, board, hud):
        # Reset tile occupation status and remove monster from the board
        board.game_board[self.row][self.col].occupied = None
        board.game_board[self.row][self.col].DisplayTile()


    def PlaceActor(self, board):
        while True:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            if board[row][col].passable:
                break
        self.row = row
        self.col = col
        board[row][col].occupied = self
    
    def Interact(self, other_actor, board, hud):
        hud.Window1Message(f"{self.name} pushes you")
    
    def move_actor(self, board, player, hud):
        current_row = self.row
        current_col = self.col
        direction = random.choice(['119', '115', '97', '100'])
        

        if direction == '119':
            new_row = current_row - 1
            new_col = current_col
        elif direction == '115':
            new_row = current_row + 1
            new_col = current_col
        elif direction == '97':
            new_row = current_row
            new_col = current_col - 1
        elif direction == '100':
            new_row = current_row
            new_col = current_col + 1
        else:
            new_row, new_col = current_row, current_col

        if 0 <= new_row < len(board.game_board) and 0 <= new_col < len(board.game_board[0]):
            if board.game_board[new_row][new_col].passable and not board.game_board[new_row][new_col].occupied:
                
                self.row = new_row
                self.col = new_col
                board.game_board[current_row][current_col].occupied = None  
                #moveCUrsor to old position
                my_utilities.MoveCursor(current_row, current_col)
                #displaytile  of that position
                board.game_board[current_row][current_col].DisplayTile()
                board.game_board[new_row][new_col].occupied = self  
                #moveCUrsor to new position
                my_utilities.MoveCursor(new_row, new_col)
                #displaytile of that position
                board.game_board[new_row][new_col].DisplayTile()

            elif board.game_board[new_row][new_col].occupied:
                other_actor = board.game_board[new_row][new_col].occupied
                self.Interact(other_actor, board, hud)



