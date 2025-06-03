import os
import blessed
term = blessed.Terminal()
if os.name == 'nt':

    #Necessary imports and custom class for Windows systems

    import msvcrt

    import ctypes

 

    class _CursorInfo(ctypes.Structure):

        _fields_ = [("size", ctypes.c_int),

                    ("visible", ctypes.c_byte)]

 

def HideCursor():

    #Turns off the blinking cursor

    if os.name == 'nt':

        ci = _CursorInfo()

        handle = ctypes.windll.kernel32.GetStdHandle(-11)

        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))

        ci.visible = False

        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

    elif os.name == 'posix':

        sys.stdout.write("\033[?25l")

        sys.stdout.flush()

 

def ShowCursor():

    #Turns on the blinking cursor

    if os.name == 'nt':

        ci = _CursorInfo()

        handle = ctypes.windll.kernel32.GetStdHandle(-11)

        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))

        ci.visible = True

        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

    elif os.name == 'posix':

        sys.stdout.write("\033[?25h")

        sys.stdout.flush()

 

def MoveCursor (row, col):

    print(term.move_xy(col, row), end="", flush=True)

 

def GetKey():

    #Gets a key press without having to press enter

    while True:

        if msvcrt.kbhit():

            userInput = msvcrt.getch()

            userInput = ord(userInput)

            return userInput