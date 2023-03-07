import os 
from time import sleep
from colorama import Fore


print("Hello World")
print(Fore.RED + "The screen will clear in 4 seconds")

sleep(4)

os.system('clear')
