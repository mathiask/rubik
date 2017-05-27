sides = ['front', 'back', 'left', 'right', 'top', 'bottom']

def rotate(l, n):
    return l[n:] + l[:n]

class Cube:
    def __init__(self):
        self.d = {}
        for s in sides:
            self.d[s] = [s, s, s, s]
        self.orbits= {
            'front': [[['top', 3], ['right', 0], ['bottom', 1], ['left', 2]],
                [['top', 2], ['right', 3], ['bottom', 0], ['left', 1]]]
            }

    def __str__(self):
        return '\n'.join([s + ': ' + '-'.join(self.d[s]) for s in sides])

    def move(self, face, dir):
        self.d[face] = rotate(self.d[face], dir)
        for o in self.orbits[face]:
            p = rotate(o, dir)
            x = self.d[p[0][0]]
            for i in range(0, 3):
                self.d[p[i][0]][p[i][1]] = self.d[o[i][0]][o[i][1]]
            self.d[p[3][0]][p[3][1]] = x[o[3][1]]
