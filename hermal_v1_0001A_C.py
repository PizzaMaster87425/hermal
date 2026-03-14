input("WARNING - WILL FAIL TO START OR WORK WITHOUT 'time' OR 'colorama'! IF YOU DO NOT HAVE COLORAMA, GO INTO TERMINAL AND TYPE 'pip install colorama'! PRESS ENTER TO CONTINUE.")

import socket
import time
from colorama import init, Fore, Back, Style

commands = {

    'run XXX': 'if found, executes the program with the name entered. In this case, it would be XXX.',
    'exit': 'exits the execution terminal.',
    'help': 'opens the help menu.',
    'test': 'activates the terminal test system.',
    'info': 'shows the terminal info.',
}

specs = {

    'Version': 'V1 Color',
    'DOVR': '03142026',
    'Build Number': '0001A',
}

def is_connected():
    try:
        # Connect to Google's public DNS at port 53 (standard DNS port)
        # Timeout of 3 seconds prevents the script from hanging
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def giveok():
    print(Style.RESET_ALL + Fore.GREEN + "[OK]" + Style.RESET_ALL)

def givefail():
    print(Style.RESET_ALL + Fore.RED + "[FAILED]" + Style.RESET_ALL)


def showhelp():
    for command, description in commands.items():
        # .ljust(10) ensures the command takes up 10 spaces
        print(f"{command.ljust(20)} : {description}")
    

def runtest():
    print("running system test...")
    print(Style.RESET_ALL + "Testing connection to internet...", end=" ")
    if is_connected():
        giveok()
    else:
        givefail()
    
    
    
def showinfo():
    for spec, description in specs.items():
        # .ljust(10) ensures the command takes up 10 spaces
        print(f"{spec.ljust(10)} : {description}")
    

def bob():
    print(Style.RESET_ALL + "activating BOB...")
    time.sleep(1)
    print("initializing 'bob.face'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    print("initializing 'bob.menu'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    print("initializing 'bob.prompts'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    print("initializing 'bob.dialogue'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    print("initializing 'bob.otherrandomstuf'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    print("initializing 'bob.finalcheck'...", end=" ")
    time.sleep(0.5)
    giveok()
    time.sleep(0.7)
    

def main():
    while True:
        user_choice = input(Fore.GREEN + Style.BRIGHT + "hermal:" + Fore.BLUE + " ~ " + Style.RESET_ALL)

        # Check the user's input using if/elif/else statements
        if user_choice == 'run bob':
            bob()
        elif user_choice == 'help':
            showhelp()
        elif user_choice == 'exit':
            return "end"
        elif user_choice == 'test':
            runtest()
        elif user_choice == 'info':
            showinfo()
#         elif user_choice == '':
#             ()
#         elif user_choice == '':
#             ()
#         elif user_choice == '':
#             ()
#         elif user_choice == '':
#             ()

        
        else:
            # Handle invalid input
            print(f"'{user_choice}' is not a valid input. type 'help' for valid commands.")

if __name__ == "__main__":
    main()
