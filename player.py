import blessed
term = blessed.Terminal()
import random
import os
import my_utilities
import time

from Game_Character import GameCharacter
from Game_Character import Actor 

class Player( GameCharacter , Actor):
    seasons = ["Spring", "Summer", "Fall", "Winter"]
   

    def __init__(self, row, col, fc, bc , sym):
        super().__init__()  
        super(GameCharacter, self).__init__(fc, bc, sym)
        
        self.history = Player.History()
        self.attack = random.randint(10,20)
        self.defense = random.randint(0, 40)
        self.health = random.randint(10, 20)
        self.current_week = 1
        self.current_season = 0
        self.seasons = 0
        self.steps = 0
    
    def Interact(self, other_actor, board, HUD):
        # Attack the monster
        damage =  self.attack - other_actor.defense
        other_actor.health -= damage
        HUD.Window2Message(f"You attack for {damage} damage")

    def Death(self, HUD, board):
       
        board.game_board[self.row][self.col].occupied = None
        board.game_board[self.row][self.col].DisplayTile()
        #HUD.SystemMessage("You have been defeated!")

           
    def History():
        Jobs = ["your job is : engineer","your job is :software developer", "your job is doctor", "your job is teacher" , "your job is acconter"]
        background = ["you love your job", "you love shopping", "you love travelling", "you love football", "you love swimming", "you love business"]
        extra = ["you graduated from education faculty", "you graduated from medicine faculty", "you graduated from engineering faculty", "you grew in village", "you have a good memories"]

        first_job = Jobs[random.randint(0,len(Jobs)-1)]
        yourbackground = background[random.randint(0,len(background)-1)]
        yourextra = extra[random.randint(0,len(extra)-1)]
        brief = "\n" + first_job +"\n" + yourbackground + "\n" + yourextra

        return brief
    
            

    def rest(self):

        self.current_week += 1
        if self.current_week > 13:
            self.current_week = 1
            self.current_season = (self.current_season + 1) % len(Player.seasons)
    
    def Clear():
        if os.name =='nt':
            os.system('cls')
        else:
            os.system('clear')

    def MoveActor(self, board, player, hud):
       
        userKey = my_utilities.GetKey() #use GetKEy instead
        currentRow = self.row
        currentCol = self.col
        #print(userKey)
        #userKey = chr(userKey)
        if userKey == 119:
            newRow = currentRow - 1
            newCol = currentCol           

        elif userKey == 115:
            newRow = currentRow + 1  
            newCol = currentCol

        elif userKey == 97:
            newRow = currentRow
            newCol = currentCol - 1

        elif userKey == 100:
            newRow = currentRow
            newCol = currentCol + 1 
        else:
            newRow = currentRow
            newCol = currentCol 

        if 0 <= newRow < len(board.game_board) and 0 <= newCol < len(board.game_board[0]):

            if board.game_board[newRow][newCol].passable and not board.game_board[newRow][newCol].occupied:
              
                self.row = newRow
                self.col = newCol
                board.game_board[currentRow][currentCol].occupied = None  
                #moveCUrsor to old position
                my_utilities.MoveCursor(currentRow, currentCol)
                #displaytile  of that position
                board.game_board[currentRow][currentCol].DisplayTile()
                board.game_board[newRow][newCol].occupied = self  
                #moveCUrsor to new position
                my_utilities.MoveCursor(newRow, newCol)
                #displaytile of that position
                board.game_board[newRow][newCol].DisplayTile()
                if self == player:
                    player.steps += 1
            elif board.game_board[newRow][newCol].occupied:
                other_actor = board.game_board[newRow][newCol].occupied
                self.Interact(other_actor, board, hud)

            else:
                my_utilities.MoveCursor(currentRow, currentCol)
                
                pass

