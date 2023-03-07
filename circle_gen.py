import math

cent_x = 2
cent_y = 3
r = 3

#The lower this value the higher quality the circle is with more points generated
stepSize = 0.4

#Generated vertices
positions = []

t = 0
while t < 2 * math.pi:
    positions.append((int(r * math.cos(t) + cent_x), int(r * math.sin(t) + cent_y)))
    t += stepSize

print(positions)
