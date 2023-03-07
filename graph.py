import math 
width = 50
height =25
w_low = -20
h_low = -20
i = height



def make_circle():
    x_cent = 1
    y_cent = 5
    radius = 5
    step = 0.01
    coords = []
    i = 0
    while i < 2*math.pi:
       # print(i)
        coords.append((int(x_cent+radius*math.cos(i)), int(y_cent+radius*math.sin(i))))
        i+=step
    #print(coords)
    return coords

coords = make_circle()

while i >= h_low:
    j = w_low
    while j <= width:
        if (j,i) in coords:
            dot = '@'
        elif j == 0 and (j,i) not in coords:
            dot = '|'
        elif i == 0 and (j,i) not in coords :
            dot = '-'
        else :
            dot = '.'
        #print(f"({j},{i})",end='')
        print(dot,end='')
        j+=1
    print()
    i = i - 1
