coords =[]
import os 
from time import sleep

def find_locus():
    global coords
    i = 0
    while i < 50:
        os.system('clear')
        y = i**2+i+6
        coords.append((i,y))
        render()
        #sleep(0.5)
        i+=1


    
    

def render(coords=coords, length = 25, breadth = 50):
    y_val = length
    
    while y_val >=0: # y coord goes from max to 0
        
        print(str(y_val).ljust(2), end='')
        x_val = 0
        while x_val <= breadth: #x_coord goes from 0 to max 
            dot = '.'
            if (x_val, y_val) in coords:
                dot ='@'
            #print(f"({x_val},{y_val})",end='') #debug 
            print(f'{dot}',end='')
            x_val = x_val + 1
            
        print()
        y_val = y_val -1
    #coords.clear()
    print('   ',end='')
    """for i in range(breadth+1):
        if i < 9:
            print(f"|{i}  ".ljust(2),end='')
        else:
            print(f" |{i}".ljust(2),end='')
"""
find_locus()
