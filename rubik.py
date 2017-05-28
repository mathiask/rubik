#!/usr/bin/python

import random
import sys

N=2
S=N*N

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

class Cube:
    cube = []

    # print cube
    def show(self) :
        for i in range(0,6):
            for j in range(0,N):
                sys.stdout.write(colors[self.cube[i][j]])
            sys.stdout.write(' ')
        sys.stdout.write('\n')

        if N==3:
            for i in range(0,6):
                sys.stdout.write(colors[self.cube[i][4*(N-1)-1]])
                sys.stdout.write(colors[i])
                sys.stdout.write(colors[self.cube[i][N]])
                sys.stdout.write(' ')
            sys.stdout.write('\n')

        for i in range(0,6):
            for j in range(0,N):
                sys.stdout.write(colors[self.cube[i][3*(N-1)-j]])
            sys.stdout.write(' ')
        sys.stdout.write('\n')
        print("===")

    # rotate a plane counter/clockwise
    def rotate(self, s, d):
        # rotate the plane
        #print(self.cube)
        self.cube[s]=self.cube[s][(N-1)*d:]+self.cube[s][:(N-1)*d]
        #print(self.cube)

        k=[]
        # find neighbor planes
        for i in range(0,4):
            n=neighbors[s][i]
            # find neighbor's row adjacent to the rotated plane
            p=neighbors[n].index(s)
            k.append((self.cube[n][(N-1)*p:]+self.cube[n][:(N-1)*p])[0:N])

        #print(k)
        #print(self.cube)
        # rotate one row of neighbor planes
        for i in range(0,4):
            n=neighbors[s][i]
            # find neighbor's row adjacent to the rotated plane
            p=neighbors[n].index(s)
            t=self.cube[n][(N-1)*p:]+self.cube[n][:(N-1)*p]
            #print(t)
            # replace it by neighbor's neighbor's row
            t[0:N]=k[(i+4+d)%4]
            #print(t)
            self.cube[n]=t[S-(N-1)*p:]+t[:S-(N-1)*p]

        #print(self.cube)
        return

    def __init__(self):
        # the ordered cube
        self.cube=[]
        self.cube.append([0,0,0,0,0,0,0,0][:4*(N-1)])
        self.cube.append([1,1,1,1,1,1,1,1][:4*(N-1)])
        self.cube.append([2,2,2,2,2,2,2,2][:4*(N-1)])
        self.cube.append([3,3,3,3,3,3,3,3][:4*(N-1)])
        self.cube.append([4,4,4,4,4,4,4,4][:4*(N-1)])
        self.cube.append([5,5,5,5,5,5,5,5][:4*(N-1)])
        return

    def ordered(self):
        for s in range(0,6):
            for i in range(0,4):
                if self.cube[s][i]!=s:
                    return False
        return True

    def test(self):
        self.show()
        for s in range(0,6):
            print("rotate side ", colors[s], " back and forth")
            self.rotate(s, -1)
            self.show()
            self.rotate(s, 1)
            self.show()
            for d in range(-1,3,2):
                print("rotate side ", colors[s], " by ", d)
                for i in range(0,4):
                    self.rotate(s, d)
                    self.show()
        if self.ordered():
            print("ok")
        else:
            print("bad")

        return

    def shuffle(self, n):
        for i in range(0,n):
            s=random.randint(0,5)
            d=2*random.randint(0,1)-1
            print(colors[s], " ", d)
            self.rotate(s, d)
        return

    def solve(self, depth):
        if depth==0:
            if self.ordered():
                self.show()
                return True
            return False

        for s in range(0,6):
            for d in range(-1,3,2):
                self.rotate(s,d)
                if self.solve(depth-1):
                    self.rotate(s,-d)
                    print(colors[s], " ", d)
                    self.show()
                    return True
                self.rotate(s,-d)

        return False

c=Cube()

if len(sys.argv)==2 and sys.argv[1]=="-t":
    print("test")
    c.test()
    exit(0)

try:
    depth=int(sys.argv[1]) if len(sys.argv)>1 else 100
except:
    print("usage: rubik.py <depth>")
    exit(-1)

print("shuffle")
c.shuffle(depth)
c.show()

print("solve")
for d in range(0,depth+1):
    if c.solve(d):
        break;
