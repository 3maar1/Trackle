from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import sys
import time
import os
import logging
import shutil
from colorama import init,Fore 
import random
init(autoreset=True)
while True:
    print(Fore.BLUE + """  Made with ♥︎ by 3maar. All rights reserved.
      """)
    print(Fore.GREEN +"  Hi! I'm Trackle, your personal file manager assistant.")
    print(Fore.GREEN +"""
            █████████████
         ███             ███
        ██     █     █     ██
       ██     █ █   █ █     ██
       ██                   ██
       ██     █       █     ██
        ██     ███████     ██
         ███             ███
            █████████████
    """)
    print(Fore.GREEN +"""  I can:
        1. Help you move, delete and rename your file/s in a chosen path.
        2. Give you a log of all the activites happening in a specified directory.
        3. Play a game with you!
        (you can enter 'q' to quit anytime)""")

# Option One -------------------------------------------------------------------------------------------
    option = input(Fore.YELLOW +"  Please select an option (1-3): ")
    if option == 'q':
        sys.exit(0)
    elif option == '2':
        if __name__ == '__main__':
            logging.basicConfig(filename='dev.log',filemode='a',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            input_paths = input(Fore.YELLOW +"  Enter the path/s you want to select separated by commas: ").split(',')
            input_paths = [p.strip() for p in input_paths if os.path.isdir(p.strip())]
            if not input_paths:
                print(Fore.GREEN +"  Path is invalid..")
            else:
                event_handler = LoggingEventHandler()
                observer = Observer()
                for path in input_paths:
                    observer.schedule(event_handler, path, recursive=True)
                observer.start()

                try:
                    print(Fore.BLUE +"  Monitoring started! Any changes will be logged here, check dev.log for saved data.")
                    while True:
                        user_inp = input(Fore.YELLOW + "  ->")
                        if user_inp.strip().lower()=='q':
                            break
                        time.sleep(1)
                except Exception as e:
                    print(Fore.RED +"  An error occured: ")
                finally:
                    observer.stop()
                    observer.join()
            

# Option Two -------------------------------------------------------------------------------------------
    elif option == '1':
        choice = input(Fore.YELLOW +"""  Do you want to:
                1. Move the file to a new location
                2. Rename the file
                3. Delete the file
                       """)
        if choice == '1':
            names = input(Fore.YELLOW +"  Enter the name of the file/s you want ot move (separated by commas): ").split(',')
            cur = input(Fore.YELLOW+"  Enter the current directory of the file/s: ").strip()
            dest = input(Fore.YELLOW+"  Enter the directory you want to move the file/s to: ").strip()

            if not os.path.exists(dest):
                print(Fore.GREEN +"  Path does not exist..")
            else:
                for name in names:
                    name = name.strip()
                    cur_path = os.path.join(cur, name)
                    dest_path = os.path.join(dest, name)

                    if os.path.isfile(cur_path):
                        try:
                            shutil.move(cur_path, dest_path)
                            print(Fore.GREEN +f"  File moved successfully from {cur_path} to {dest_path}")
                        except Exception as e:
                            print(Fore.GREEN +f"  An error occured..")
                    else:
                        print(Fore.GREEN +"  File not Found.")

        elif choice == '2':
            folder = input(Fore.YELLOW+"  Enter the directory path of the file: ").strip()
            cur = input(Fore.YELLOW+"  Enter the current name of the file: ").strip()
            new = input(Fore.YELLOW+"  Enter the new name for the file: ").strip()
            cur_path = os.path.join(folder, cur)
            new_path = os.path.join(folder, new)

            if os.path.isfile(cur_path):
                try:
                    os.rename(cur_path, new_path)
                    print(Fore.GREEN +f"  File renamed successfully from {cur} to {new}")
                except Exception as e:
                    print(Fore.GREEN +f"  An error occured..")
            else:
                print(Fore.GREEN +"  File not Found.")

        elif choice == '3':
            names = input(Fore.YELLOW+"  Enter the name of the file/s you want to delete (separated bby commas): ").split(',')
            folder = input(Fore.YELLOW+"  Enter the directory path of the file/s: ").strip()

            for name in names:
                path = os.path.join(folder, name.strip())
                try:
                    os.remove(path)
                    print(Fore.GREEN +"  File removed successfully.")
                except FileNotFoundError:
                    print(Fore.GREEN +"  File not found..")
                except PermissionError:
                    print(Fore.GREEN +"  Permission denied..")
                except Exception as e:
                    print(Fore.GREEN +"  An error occured..")

# Option Three -------------------------------------------------------------------------------------------
    elif (option == '3'):
        print (Fore.RED+"  Let's play rock paper scissors!")
        choices = ['rock','paper','scissors']
        while True:
                user = input(Fore.YELLOW+"  Enter your choice: ")
                if user == 'q':
                    print(Fore.GREEN+"  It was a good game!")
                    break
                if user == 'rock' or user == 'paper' or user == 'scissors':
                    rand = random.choice(choices)
                    if user == rand:
                        print(Fore.GREEN + f"  I chose {rand}, It's a tie. Let's play again!")
                        rand = 0
                        continue
                    elif (user == 'rock' and rand == 'scissors') or (user == 'paper' and rand == 'rock') or (user == 'scissors' and rand == 'paper'):
                        print (Fore.BLUE + f"  I chose {rand}, YOU WIN!")
                        rand = 0
                        continue
                    else:
                        print(Fore.RED + f"  Haha, I chose {rand}. You lose!")
                        rand = 0
                        continue
