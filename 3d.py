import math
import time #only for delay nothing else


##### OUR CANVUS VARIABLES #####
width = 50  #Max positive x 
height =50  #Max positive y 
w_low = -50 #negative x range
h_low = -30 #negative y range


def render(coords,height,widt,h_low, w_low):
    """
    Prins all the points on the screen 
    """
    #print('='*50)
    i = height
    while i >= h_low:
        j = w_low
        while j <= width:
            if (j,i) in coords:
                dot ='@'
# show axises
##            elif j == 0 and (j,i) not in coords:  #DEBUG to show axises
##                dot = '#'
##            elif i == 0 and (j,i) not in coords :
##                dot = '#'
            else :
                dot = '.'
            #print(f"({j},{i})",end='')
            print(dot,end='')
            j+=1
        print()
        i = i - 1


def connect_corn(coord_1,coord_2):
    """
    Finds all the points between two points
    connected by a straight line 
    """
    
    coords = []
    if coord_2[0] - coord_1[0] == 0: #case slope 0
        if coord_2[1] - coord_1[1] < 0 :
            for i in range(0, abs(int(coord_2[1]-coord_1[1]))+1):
                coords.append((coord_1[0], coord_1[1]-i))
        else:
            for i in range(0, abs(int(coord_2[1]-coord_1[1])+1)):
                coords.append((coord_1[0], coord_1[1]+i))
            
    elif coord_2[1] - coord_1[1] == 0: #case slope infinity 
        
        for i in range(0, abs(int(coord_2[0]-coord_1[0]))+1):
            if coord_2[0] - coord_1[0] < 0 : 
                coords.append((coord_1[0]-i,coord_1[1]))
            else:
                coords.append((coord_1[0]+i,coord_1[1]))
    else : #case slope non zero non infinity 
        m = (coord_2[1] - coord_1[1]) / (coord_2[0] - coord_1[0])
        m = math.atan(m)
        dist = int(math.sqrt( (coord_1[0]-coord_2[0])**2 + (coord_1[1]-coord_2[1])**2))
        if m > 0: #case slope positive
            if coord_1[1] > coord_2[1]: #point 1 above 2
                
                for i in range(dist):
                    x = coord_2[0] + i*math.cos(m)
                    y = coord_2[1] + i*math.sin(m)
                    coords.append((round(x,0), round(y,0)))
                
            elif coord_1[1] < coord_2[1]: #point 2 above 1
                
                for i in range(dist):
                    x = coord_1[0] + i*math.cos(m)
                    y = coord_1[1] + i*math.sin(m)
                    coords.append((round(x,0), round(y,0)))
        else: #case slope negative 
            if coord_1[1] > coord_2[1]: #point 1 above 2
                
                for i in range(dist):
                    x = coord_2[0] - i*math.cos(m)
                    y = coord_2[1] - i*math.sin(m)
                    coords.append((round(x,0), round(y,0)))
                
            elif coord_1[1] < coord_2[1]: #point 2 above 1
                
                for i in range(dist):
                    x = coord_1[0] - i*math.cos(m)
                    y = coord_1[1] - i*math.sin(m)
                    coords.append((round(x,0), round(y,0)))        
        
    return coords
    

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (int(qx), int(qy))


def make_circle(x_cent=1, y_cent=5, radius=5):
    """
    Calculates the Locus of a circle with given center
    """
    step = 0.01
    coords = []
    i = 0
    while i < 2*math.pi:
       # print(i)
        coords.append((int(x_cent+radius*math.cos(i)), int(y_cent+radius*math.sin(i))))
        i+=step
    #print(coords)
    return coords




############################[ A N I M A T I O N S ]###############################
'''
# No_1 - The cube goes up and down

x_o = -10
y_o = -10
for i in range(5):
    for j in range(5):
        x_o += j
        y_o += i

        point_1 = (10+x_o  ,  10+y_o )
        point_2 = (-10+x_o , 10+y_o  )
        point_3 = (-10+x_o , -10+y_o )
        point_4 = (10+x_o  , - 10+y_o)
        z = 1.2
        z_point_1 = (int(point_1[0]/z), int(point_1[1]/z))
        z_point_2 = (int(point_2[0]/z), int(point_2[1]/z))
        z_point_3 = (int(point_3[0]/z), int(point_3[1]/z))
        z_point_4 = (int(point_4[0]/z), int(point_4[1]/z))
        coords = []
        coords.extend(connect_corn(point_1,point_2))
        coords.extend(connect_corn(point_2,point_3))
        coords.extend(connect_corn(point_3,point_4))
        coords.extend(connect_corn(point_4,point_1))

        coords.extend(connect_corn(z_point_1,z_point_2))
        coords.extend(connect_corn(z_point_2,z_point_3))
        coords.extend(connect_corn(z_point_3,z_point_4))
        coords.extend(connect_corn(z_point_4,z_point_1))

        coords.extend(connect_corn(z_point_1,point_1))
        coords.extend(connect_corn(z_point_2,point_2))
        coords.extend(connect_corn(z_point_3,point_3))
        coords.extend(connect_corn(z_point_4,point_4))

        #coords=[point_1,z_point_1,point_2,z_point_2,point_3,z_point_3,point_4,z_point_4]
        
        render(coords,height, width, h_low, w_low)

for i in range(5):
    for j in range(5):
        x_o -= j
        y_o -= i

        point_1 = (10+x_o  ,  10+y_o )
        point_2 = (-10+x_o , 10+y_o  )
        point_3 = (-10+x_o , -10+y_o )
        point_4 = (10+x_o  , - 10+y_o)
        z = 1.2
        z_point_1 = (int(point_1[0]/z), int(point_1[1]/z))
        z_point_2 = (int(point_2[0]/z), int(point_2[1]/z))
        z_point_3 = (int(point_3[0]/z), int(point_3[1]/z))
        z_point_4 = (int(point_4[0]/z), int(point_4[1]/z))
        coords = []
        coords.extend(connect_corn(point_1,point_2))
        coords.extend(connect_corn(point_2,point_3))
        coords.extend(connect_corn(point_3,point_4))
        coords.extend(connect_corn(point_4,point_1))

        coords.extend(connect_corn(z_point_1,z_point_2))
        coords.extend(connect_corn(z_point_2,z_point_3))
        coords.extend(connect_corn(z_point_3,z_point_4))
        coords.extend(connect_corn(z_point_4,z_point_1))

        coords.extend(connect_corn(z_point_1,point_1))
        coords.extend(connect_corn(z_point_2,point_2))
        coords.extend(connect_corn(z_point_3,point_3))
        coords.extend(connect_corn(z_point_4,point_4))

        #coords=[point_1,z_point_1,point_2,z_point_2,point_3,z_point_3,point_4,z_point_4]
                
        render(coords,height, width, h_low, w_low)
            

'''
#2) The Cube Goes round and Round

x = 0
z = 1
point_1_o = (20,15) #x z 
point_2_o = (-20,15)
point_3_o = (-20,-15)
point_4_o = (20,-15)


y = 10 # our y prespective

width = 10 #cube width

#Rotating cente
cent = ((point_1_o[0]+point_3_o[0])/2, (point_1_o[1]+point_3_o[1])/2)
print(cent)
r_p=0
for i in range(50):
    r_p+=0.1
    
    y-=1

    if y == 0:
        print("ZERO")
        y = -2
   
    
        
    coords = []
    point_1 = rotate(cent,point_1_o, r_p) #rotating 
    point_2 = rotate(cent,point_2_o ,r_p)
    point_3 = rotate(cent, point_3_o,r_p)
    point_4 = rotate(cent,point_4_o ,r_p)
    
    #connecting the points
    
    coords.extend(connect_corn( (point_1[0],point_1[1]/y), (point_2[0],point_2[1]/y) ))  #our top/parent points
    coords.extend(connect_corn( (point_2[0],point_2[1]/y), (point_3[0],point_3[1]/y) ))
    coords.extend(connect_corn( (point_3[0],point_3[1]/y), (point_4[0],point_4[1]/y) ))
    coords.extend(connect_corn( (point_4[0],point_4[1]/y), (point_1[0],point_1[1]/y) ))

    coords.extend(connect_corn( (point_1[0],point_1[1]/y-width), (point_2[0],point_2[1]/y-width) )) #interconnecting the bottom points
    coords.extend(connect_corn( (point_2[0],point_2[1]/y-width), (point_3[0],point_3[1]/y-width) ))
    coords.extend(connect_corn( (point_3[0],point_3[1]/y-width), (point_4[0],point_4[1]/y-width) ))
    coords.extend(connect_corn( (point_4[0],point_4[1]/y-width), (point_1[0],point_1[1]/y-width) ))

    coords.extend(connect_corn( (point_1[0],int(point_1[1]/y)), (point_1[0],int(point_1[1]/y)-width) )) #connecting the bottom with the top 
    coords.extend(connect_corn( (point_2[0],int(point_2[1]/y)), (point_2[0],int(point_2[1]/y)-width) ))
    coords.extend(connect_corn( (point_3[0],int(point_3[1]/y)), (point_3[0],int(point_3[1]/y)-width) ))
    coords.extend(connect_corn( (point_4[0],int(point_4[1]/y)), (point_4[0],int(point_4[1]/y)-width) ))
    
    render(coords,height, width, h_low, w_low) #render
    time.sleep(1/5) #delay
    
    

