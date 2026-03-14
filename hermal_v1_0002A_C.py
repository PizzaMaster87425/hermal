input("WARNING - WILL FAIL TO START OR WORK WITHOUT 'time' OR 'colorama'! IF YOU DO NOT HAVE COLORAMA, GO INTO TERMINAL AND TYPE 'pip install colorama'! PRESS ENTER TO CONTINUE.")

import socket
import time
from colorama import init, Fore, Back, Style

settings = {
    "debug_mode": False
}

def toggle_debug():
    # This flips the True/False value
    settings["debug_mode"] = not settings["debug_mode"]
    status = "ENABLED" if settings["debug_mode"] else "DISABLED"
    print(f"Debug Mode is now {status}")

commands = {

    'run XXX': 'if found, executes the program with the name entered. In this case, it would be XXX.',
    'exit': 'exits the execution terminal.',
    'help': 'opens the help menu.',
    'test': 'activates the terminal test system.',
    'info': 'shows the terminal info.',
    'NOTE': 'some commands may not be shown here.',
}

fullcommands = {

    'run XXX': 'if found, executes the program with the name entered. In this case, it would be XXX.',
    'force run XXX': 'forces the program (in this case, XXX,) to run, does NOT depend on the mode.',
    'List of run commands': '(shown below)',
    '     fullhelp': 'opens this menu.',
    '     toggle_debug': 'toggles the debug mode.',
    '     giveok': 'runs the giveok program',
    '     givefail': 'runs the givefail program',
#     '     ': '',
#     '     ': '',
    
    'exit': 'exits the execution terminal.',
    'help': 'opens the help menu.',
    'test': 'activates the terminal test system.',
    'info': 'shows the terminal info.',
    'NOTE': 'some commands may not be shown here.',
}

specs = {

    'Version': 'V1 Color',
    'DOVR': '03142026',
    'Build Number': '0002A',
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
    
def fullhelp():
    for command, description in fullcommands.items():
        # .ljust(10) ensures the command takes up 10 spaces
        print(f"{command.ljust(20)} : {description}")

def runtest():
    print("running system test...")
    print(Style.RESET_ALL + "Testing connection to internet...", end=" ")
    if is_connected():
        giveok()
    else:
        givefail()
    
    print("Testing delay...", end=" ")
    time.sleep(1)
    giveok()
    print("Finishing up...", end=" ")
    time.sleep(0.1)
    giveok()
    
    
    
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



force_run_commands = {
    'bob': bob,
    'runtest': runtest,
    'showinfo': showinfo,
    'giveok': giveok,
    'givefail': givefail,
    'toggle_debug': toggle_debug,   
}

normal_run_commands = {
    'bob': bob,
    'runtest': runtest,
    'showinfo': showinfo,
    'help': showhelp,
}

restricted_normal_run_commands = {
    'giveok': giveok,
    'givefail': givefail,
    'toggle_debug': toggle_debug,
    'fullhelp': fullhelp,
}

def main():
    while True:
        if settings["debug_mode"]:
            user_choice = input(Fore.YELLOW + "[DEBUG] " + Fore.GREEN + Style.BRIGHT + "hermal:" + Fore.BLUE + " ~ " + Style.RESET_ALL)
        else:
            user_choice = input(Fore.GREEN + Style.BRIGHT + "hermal:" + Fore.BLUE + " ~ " + Style.RESET_ALL)

        # Check the user's input using if/elif/else statements
#         if user_choice == 'run bob':
#             bob()
        if user_choice == 'help':
            showhelp()
#         elif user_choice == 'run giveok':
#             if not settings["debug_mode"]:
#                 print(Fore.RED + f"Error: '{target}' has failed to run. Reason: 'access_denied'" + Style.RESET_ALL)
#             else:
#                 
#         elif user_choice == 'run givefail':
#             print(Fore.RED + f"Error: '{target}' has failed to run. Reason: 'access_denied'" + Style.RESET_ALL)
#         elif user_choice == 'run DVMD':
#             print(Fore.RED + f"Error: '{target}' has failed to run. Reason: 'access_denied'" + Style.RESET_ALL)
        elif user_choice == 'exit':
            return "end"
        elif user_choice == 'test':
            runtest()
        elif user_choice == 'info':
            showinfo()
        elif user_choice.startswith('force run '):
            # This grabs everything after 'force run '
            target = user_choice.replace('force run ', '').strip()
            
            if target in force_run_commands:
                print(f"Force starting {target}...")
                time.sleep(0.5)
                # This actually calls the function mapped in the dictionary
                force_run_commands[target]()
            else:
                print(Fore.RED + f"Error: '{target}' is not a valid force-run target." + Style.RESET_ALL)
                
        elif user_choice.startswith('run '):
            # This grabs everything after 'force run '
            target = user_choice.replace('run ', '').strip()
            
            if target in normal_run_commands:
                print(f"Starting {target}...")
                time.sleep(0.5)
                # This actually calls the function mapped in the dictionary
                normal_run_commands[target]()
            elif target in restricted_normal_run_commands:
                if settings["debug_mode"]:
                    print(f"Starting {target}...")
                    time.sleep(0.5)
                    # This actually calls the function mapped in the dictionary
                    restricted_normal_run_commands[target]()
                else:
                    print(Fore.RED + f"Error: '{target}' // Reason: 'denied'" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Error: '{target}' is not a valid target." + Style.RESET_ALL)
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
