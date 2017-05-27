#!/usr/bin/python

import sys

# 6 planes red, blue, yellow, orange, green, white
# 0 r: b y g w
# 1 b: y r w o
# 2 y: o g r b
# 3 o: g y b w
# 4 g: w r y o
# 5 w: r g o b

# neighbors of each plane in clockwise order
neighbors=[]
neighbors.append([1,2,4,5])
neighbors.append([2,0,5,3])
neighbors.append([3,4,0,1])
neighbors.append([4,2,1,5])
neighbors.append([5,0,2,3])
neighbors.append([0,4,3,1])

# print planes
colors=["R","B","Y","O","G","W"]

def showSide(s) :
    sys.stdout.write('\n')
    sys.stdout.flush()

def showCube(c) :
    for i in range(0,6):
        sys.stdout.write(colors[c[i][0]])
        sys.stdout.write(colors[c[i][1]])
        sys.stdout.write(' ')
    sys.stdout.write('\n')

    for i in range(0,6):
        sys.stdout.write(colors[c[i][3]])
        sys.stdout.write(colors[c[i][2]])
        sys.stdout.write(' ')
    sys.stdout.write('\n')
    print("==");

# rotate a plane counter/clockwise
def rotate(c, s, d):
    if d>0:
        t=c[s][0]
        c[s][0:3]=c[s][1:4]
        c[s][3]=t
    else:
        t=c[s][3]
        c[s][1:4]=c[s][0:3]
        c[s][0]=t

    k=[]
    for i in range(0,4):
        n=neighbors[s][i]
        p=neighbors[n].index(s)
        k.append([c[n][p], c[n][(p+1)%4]])

    for i in range(0,4):
        n=neighbors[s][i]
        p=neighbors[n].index(s)
        c[n][p]=k[(i+4+d)%4][0]
        c[n][(p+1)%4]=k[(i+4+d)%4][1]

    return

# the ordered cube
cube=[]
cube.append([0,0,0,0])
cube.append([1,1,1,1])
cube.append([2,2,2,2])
cube.append([3,3,3,3])
cube.append([4,4,4,4])
cube.append([5,5,5,5])

# rotate all planes four times counter/clockwise
showCube(cube)
for s in range(0,5):
    print("rotate side ", colors[s], " forth and back")
    rotate(cube, s, -1)
    showCube(cube)
    rotate(cube, s, 1)
    showCube(cube)
    for d in range(-1,3,2):
        print("rotate side ", colors[s], " by ", d)
        for i in range(0,4):
            rotate(cube, s, d)
            showCube(cube)
