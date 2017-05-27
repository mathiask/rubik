#!/usr/bin/python

import array
import sys

# 0 r: b y g w red
# 1 b: y r w o blue
# 2 y: o g r b yellow
# 3 o: g y b w orange
# 4 g: w r y o green
# 5 w: r g o b white

neighbors=[]
neighbors.append([1,2,4,5])
neighbors.append([2,0,5,3])
neighbors.append([3,4,0,1])
neighbors.append([4,2,1,5])
neighbors.append([5,0,2,3])
neighbors.append([0,4,3,1])

colors=["R","B","Y","O","G","W"]

def showSide(s) :
    sys.stdout.write(colors[s[0]])
    sys.stdout.write(colors[s[1]])
    sys.stdout.write('\n')
    sys.stdout.write(colors[s[3]])
    sys.stdout.write(colors[s[2]])
    sys.stdout.write('\n')
    sys.stdout.flush()

def showCube(c) :
    for i in range(0,6):
        showSide(c[i])
        if i<5:
            sys.stdout.write('\n')
    print("==");

def rotate(c, s):
    t=c[s][0]
    c[s][0:3]=c[s][1:4]
    c[s][3]=t

    k=[]
    for i in range(0,4):
        n=neighbors[s][i]
        p=neighbors[n].index(s)
        k.append([c[n][p], c[n][(p+1)%4]])

    for i in range(0,4):
        n=neighbors[s][i]
        p=neighbors[n].index(s)
        c[n][p]=k[(i+3)%4][0]
        c[n][(p+1)%4]=k[(i+3)%4][1]

    return

cube=[]
cube.append([0,0,0,0])
cube.append([1,1,1,1])
cube.append([2,2,2,2])
cube.append([3,3,3,3])
cube.append([4,4,4,4])
cube.append([5,5,5,5])

showCube(cube)
for s in range(0,5):
    print("rotate side ", colors[s])
    for i in range(0,4):
        rotate(cube, s)
        showCube(cube)
