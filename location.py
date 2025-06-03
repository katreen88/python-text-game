
"""Katreen Farah
2/15/2024
location class
"""
import blessed
term = blessed.Terminal()
import os
from player import *
import math
import my_utilities
from Game_Character import Monster

class Location:
    def __init__(self):
        self.manager = Player.GenName()
        self.foreColor = "deepskyblue4" 
        self.backColor = "steelblue1"

    def Enter(self):
        os.system('cls')
        print(getattr(term, self.foreColor)+"welcome with us "+term, self.backColor)
        print(f"Managed by: {self.manager}")

    def Exit(self):
        print(f"{getattr(term, self.foreColor)}Goodbye!{getattr(term, self.backColor)}")

    def Upkeep(self):
        pass

class Town(Location):
    def __init__(self,player):
        super().__init__()
        self.palace = Palace(player)
        self.lumbermill = Lumbermill()
        self.dungeon = Dungeon()
    

    def Enter(self, player):
        while True:
            result = ""
            os.system('cls')
            print(f"{getattr(term, self.foreColor)}****Welcom to TOWN SQUARE *****{getattr(term, self.backColor)}\n")
            print(f"Current Date: Week {player.current_week} of {Player.seasons[player.current_season]}\n")

            print("Locations:")
            print("1. Palace")
            print("2. Lumbermill")
            print("3.Dungeon")
            print("0.  Quit")
            choice = input("Enter your choice (1/2/0):\n ")
            if choice == "1":
                result = self.palace.Enter(player)
            elif choice == "2":
                self.lumbermill.Enter(player)
            elif choice =="3":
                self.dungeon.Enter(player)
            elif choice == "0":
                self.Exit()
            else:
                print("Invalid choice")
            if result == "REST":
                self.Upkeep()
                player.rest()

    def Exit(self):
        print(f"{getattr(term, self.foreColor)}**Exiting the Town. Goodbye!**{getattr(term,self.backColor)}")
        exit()

    def Upkeep(self):
        self.palace.Upkeep()
        self.lumbermill.Upkeep()


class Palace(Location):
    def __init__(self, player):
        super().__init__()
        self.deposited_gold = 50
        self.manager = player.name

    def Enter(self,player):
        os.system('cls')
        print(f"{getattr(term, self.foreColor)}****Welcome to the Palace*****{getattr(term, self.backColor)}\n")
        print(f"Managed by: {self.manager}")
        print(f"Deposited Gold : {self.deposited_gold}")
        print("1. Deposit /withdraw Gold")
        print("2. Rest for a week")
        print("0.Leave")
        choice = input("enetr you choice: ")
        if choice == "1":
            amount = int(input("enetr the amount of gold: "))
            self.DepositGold(amount)
            self.Enter(player)

        if choice =="2":
            return "REST"
           
        elif choice =="0":
            exit()
            return True
        else:
            print("invalid option")


    def DepositGold(self, amount):
        self.deposited_gold += amount
        print(f"successfuly deposited {amount} gold .")

    def Rest(self):
        print("You rest and feel happy.")
        


class Lumbermill(Location):
    def __init__(self):
        super().__init__()
        self.rate = 10
        self.capacity = 100
        self.stock = 0

    def Enter(self, player):
        os.system('cls')
        print(f"{getattr(term, self.foreColor)}****Welcome to the Lumbermill*****{getattr(term, self.backColor)}\n")
        print(f"Managed by: {self.manager}")
        print(f"Rate: {self.rate} wood per day")
        print(f"Capacity: {self.capacity} wood")
        print(f"Current Stock: {self.stock} wood\n")
        choice = input("[enter] to return to town")
              

    def Upkeep(self):
        
        self.stock += self.rate
        if self.stock > self.capacity:
            self.stock = self.capacity

class Tile:
    def __init__(self, symbol = "#", foreColor = "mediumpurple", backColor = "maroon1", passable = False):
        self.symbol = symbol
        self.foreColor = foreColor
        self.backColor =  backColor
        self.passable = passable
        self.stairsHere = False
        self.occupied = None
        

    def DisplayTile(self):
        if self.occupied:
            
            print(self.occupied.symbol, end="")
            #print(self.occupied.symbol, end = "")
        elif self.stairsHere:
            print("*", end='')
        
        else:
            #print(getattr(term,self.foreColor + "_on_"+ self.backColor) (self.symbol), end="")
            print(self.symbol, end='')

class Board: 
    def __init__(self, width, height) :
        self.width = width   
        self.height = height
        self.midpoints = []

    def CreateBoard(self):
        self.game_board = []
        for i in range(0, self.height):
            self.game_board.append([])
            for j in range(0, self.width):
                self.game_board[i].append(Tile())
       
    
    def MakeRoom(self,height, width, row, col):
        if row + height > self.height or col + width > self.width:
            return 
        midpoint = (row + height // 2, col + width // 2)  
        self.midpoints.append(midpoint) 
        for i in range(row, row + height):
            for j in range(col, col + width):
                self.game_board[i][j] = Tile(symbol = ".", passable=True)
    
    def CreateRooms(self, num_rooms):
        room_counter = 0
        self.num_rooms = num_rooms
        while room_counter < num_rooms:
        
            room_width = random.randint(5, 8)
            room_height = random.randint(5, 8)
            x = random.randint(1,self.width -room_width - 1)
            y = random.randint(1,self.height- room_height -1)

            if x + room_width < self.width and y + room_height < self.height:
                self.MakeRoom(room_height,room_width,x, y)
                room_counter += 1
            if room_counter== self.num_rooms:
                break
        #return self.midpoints

  
    def BuildCorridors(self):
        for c in range(len(self.midpoints) -1):
            midpoint1 = self.midpoints[c]
            midpoint2 = self.midpoints[c + 1]

            if midpoint1[0] < midpoint2[0]:  
                for row in range(midpoint1[0], midpoint2[0] + 1):
                    self.game_board[row][midpoint1[1]] = Tile(symbol=".", passable=True)  
            elif midpoint1[0] >= midpoint2[0]:  
                for row in range(midpoint1[0], midpoint2[0] - 1, -1):
                    self.game_board[row][midpoint1[1]] = Tile(symbol=".", passable=True)  
            if midpoint1[1] < midpoint2[1]:  
                for col in range(midpoint1[1], midpoint2[1] + 1):
                    self.game_board[row][col] = Tile(symbol=".", passable=True)  

            elif midpoint1[1] >= midpoint2[1]:  
                for col in range(midpoint1[1], midpoint2[1] - 1, -1):
                    self.game_board[row][col] = Tile(symbol=".", passable=True) 
    
      
    def PlaceStairs(self):
        while True:
            row = random.randint(0, len(self.game_board) - 1)
            col = random.randint(0, len(self.game_board[0]) - 1)
            if self.game_board[row][col].symbol == "." and self.game_board[row][col].passable == True:
                self.game_board[row][col].stairsHere = True 
                break 
    
    
    def ShowBoard(self):
        for row in self.game_board:
            for tile in row:
                tile.DisplayTile()
            print()

    
        
class Dungeon(Location):

    def __init__(self):
        super().__init__()
       
    def Enter(self, player):
        os.system('cls')
        board = Board(30,30)
        board.CreateBoard()   
        board.CreateRooms(5)
        #board.MakeRoom(4,5,6,9)
        board.BuildCorridors()
        
        player.PlaceActor(board.game_board)
        self.monsterList = []

        for i in range(5):
            x = random.randint(0, 29)  
            y = random.randint(0, 29)  
            health = random.randint(0, 30)  # Generate random health value
            monster_type = random.choice(["G", "S", "D", "Z", "O"])
            defense = random.randint(0, 50)  # Generate random defense value

            monster = Monster(health, monster_type, defense)  # Create Monster instance
            monster.PlaceActor( board.game_board)  
            self.monsterList.append(monster)

            #monsterList.append(Monster)# Pass the health argument to Monster constructor
          
    
        board.ShowBoard()
        
        #input()
        hud = HUD()
        hud.DrawHud(0,31,30,8)
        hud.DrawHud(9,31,30,7)
        hud.DrawHud(31,1,30,15)
        """
        for monster in monsterList:
            monster.PlaceActor( board.game_board) 
        """
        while True:
            player.MoveActor(board, player, hud)
            for monster in self.monsterList:
                if monster.health > 0:
                    monster.move_actor(board, player, hud)
                else:
                    monster.Death(board, hud)  # Handle death of the monster
            self.monsterList = [monster for monster in self.monsterList if monster.health > 0]
  
        """
        for i in range(100):
            hud.SystemMessage(f"System Message {i+1}", "white", "black")
            hud.Window1Message(f"Window 1 Message {i+1}")
            hud.Window2Message(f"Window 2 Message {i+1}")
        
        for i  in range(100):
            #os.system('cls')

            message = "You found the treasure  "+ str(i)
            message2 = "you evaded the trap "+str(i+1)
            hud.SystemMessage(message, "white", "black")
            #hud.SystemMessage(message2, "white", "black")
            hud.Window1Message(message)
            #hud.Window2Message(message2)

            input()
        """
        #board.CreateRooms(5)
        #Board.BuildCorridors()
        #Board.PlaceStairs()
        

    def ShowBoard(self):
        Board.ShowBoard(self.board)

class HUD:
    def __init__(self):
        self._SystemMessages = []
        self._window1Messages = []
        self._window2Messages = []
        self.MaxMesaage = 6

    #def MoveCursor( row, col):
        #print(term.move_xy(col, row), end="")

    def DrawHud(self, row, col, width, height):
        # Top Border
        for c in range(col, col + width):
            my_utilities.MoveCursor(row, c + 1)
            print(getattr(term,"green_on_black")("="), end="")

        # Bottom Border
        for c in range(col, col + width):
            my_utilities.MoveCursor(row + height, c + 1)
            print(getattr(term,"green_on_black")("="), end="")

        # Left Border
        for r in range(row, row + height):
            my_utilities.MoveCursor(r, col)
            print(getattr(term,"green_on_black")("║"), end="")

        # Right Border
        for r in range(row , row + height):
            my_utilities.MoveCursor(r, col + width )
            print(getattr(term, "green_on_black")("║"), end="")

        # Corners
        my_utilities.MoveCursor(row, col)
        print(getattr(term, "green_on_black")("╔"), end="")
        my_utilities.MoveCursor(row + height, col)
        print(getattr(term, "green_on_black")("╚"), end="")
        my_utilities.MoveCursor(row, col + width)
        print(getattr(term, "green_on_black")("╗"), end="")
        my_utilities.MoveCursor(row + height, col + width)
        print(getattr(term, "green_on_black")("╝"), end="")
        for i in range(1,4):
            my_utilities.MoveCursor(row+i, col+1)
            print("message" )

    def PlayerWindow(self):
        
        # Display player stats
        my_utilities.MoveCursor(2, 3)

        print(f"Player Name: {Player.GenName()}")
        my_utilities.MoveCursor(3, 3)
        print(f"Health: ", random.randint(0, 50))
        my_utilities.MoveCursor(4, 3)
        print(f"Level: ", random.randint(0, 50))
        my_utilities.MoveCursor(5, 3)
        print(f"attack", random.randint(0, 50))
        my_utilities.MoveCursor(6, 3)
        print(f"attack", random.randint(0, 50))

    
    def SystemMessage(self, message, fc= "white", bc = "black"):
        #message = [message, fc+"_on_"+bc]
        #if number of  messages equals the max number of messages,
        if len(self._SystemMessages)>= self.MaxMesaage:
            self._SystemMessages.pop(0)
        self._SystemMessages.append([message, f"{fc}_on_{bc}"])

        for i in range (1,7):
            (32 + i, 2)
            print(" "*20)
        
        #self.DrawHud(31,0,20,5)
        #self.MoveCursor(31, 30)

        currentRow = 32
        for m in self._SystemMessages: 
            self.MoveCursor(currentRow, 2)
            print(m[0])
            currentRow += 1
        
        
    def Window1Message(self, message, fc= "white", bc = "black"):
        if len(self._window1Messages) >= self.MaxMesaage:
            self._window1Messages.pop(0)
        self._window1Messages.append([message, f"{fc}_on_{bc}"])
        for i in range (1,7):
            my_utilities.MoveCursor( i, 32)
            print(" "*20)
        my_utilities.MoveCursor(32,0)

        currentRow = 1
        for m in self._window1Messages: 
            my_utilities.MoveCursor(currentRow, 32)
            print(m[0])
            currentRow += 1
        
       
    def Window2Message(self, message, fc= "white", bc = "black"):
        if len(self._window2Messages) >= self.MaxMesaage:
            self._window2Messages.pop(0)
        self._window2Messages.append([message, f"{fc}_on_{bc}"])
        for i in range (1,7):
            my_utilities.MoveCursor( i, 32)
            print(" "*20)
        my_utilities.MoveCursor(32,0)

        currentRow = 10
        for m in self._window2Messages: 
            my_utilities.MoveCursor(currentRow, 32)
            print(m[0])
            currentRow += 1
        

"""
    def Window2Message(self, message):
        self._window2Messages.append(message)
        if len(self._window2Messages) >= self.MaxMesaage:
            self._window2Messages.pop(0)
        my_utilities.MoveCursor(36, 2)

    """

    
        
"""
hud = HUD()
hud.DrawHud()

for i  in range(100):
    message = "You found the treasure "+ str(i)
    hud.SystemMessage(message)
    hud._window1Messages.append(message)
    input()
"""
    
    
           


    

    

