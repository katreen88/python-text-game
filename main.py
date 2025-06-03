
"""Katreen Farah
2/22/2024
Dungeon assignment
"""

from location import *
from player import *
import Game_Character
def main():
    while True:
        os.system('cls')
        
        p1 = Player(3,2,"Red","Black","@")    
        
        print("\n"+term.red+"the Name is :"+getattr(term,"purple")+p1.name)
        print("\n"+term.white_on_blue(" The History "), p1.history)
        print("\n"+ term.yellow_on_green("attack:"),p1.attack )
        print("\n"+ term.blue_on_yellow("defense: "), p1.defense)
        print("\n"+term.pink_on_purple("Health: "), p1.health ,"\n")
        userCharacter = input(term.white_on_brown(" press enter to generate another character or (0)to quit ")+"\n")
        if userCharacter == "0":
            break
    
    town = Town(p1)
    town.Enter(p1)
    input()
   
    """
    hud = HUD()
    hud.PlayerWindow()

    for i  in range(10):
        message = "You found the treasure "+ str(i)
        message2 = "you evaded the trap"+str(i)
        hud.SystemMessage(message)
        hud._window1Messages.append(message)
        hud._window2Messages.append(message2)
        input()
    """
main() 