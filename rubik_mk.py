import random, copy

random.seed()

sides = ['front', 'back', 'left', 'right', 'top', 'bottom']
orbits= {
    'front': [[['top', 3], ['right', 0], ['bottom', 1], ['left', 2]],
              [['top', 2], ['right', 3], ['bottom', 0], ['left', 1]]],
    'back': [[['top', 0], ['left', 3], ['bottom', 2], ['right', 1]],
             [['top', 1], ['left', 0], ['bottom', 3], ['right', 2]]],
    'top': [[['front', 0], ['left', 0], ['back', 0], ['right', 0]],
            [['front', 1], ['left', 1], ['back', 1], ['right', 1]]],
    'bottom': [[['front', 2], ['right', 2], ['back', 2], ['left', 2]],
               [['front', 3], ['right', 3], ['back', 3], ['left', 3]]],
    'left': [[['top', 0], ['front', 0], ['bottom', 0], ['back', 2]],
             [['top', 3], ['front', 3], ['bottom', 3], ['back', 1]]],
    'right': [[['top', 1], ['back', 3], ['bottom', 1], ['front', 1]],
              [['top', 2], ['back', 0], ['bottom', 2], ['front', 2]]]
}

def rotate(l, n):
    return l[-n:] + l[:-n]

class Cube:
    def __init__(self):
        self.d = {}
        for s in sides:
            self.d[s] = [s, s, s, s]

    def __str__(self):
        return '\n'.join([s + ': ' + '-'.join(self.d[s]) for s in sides])

    def __repr__(self):
        return '<class Cube(' + str(self.d) + ')>'

    def move(self, face, dir):
        self.d[face] = rotate(self.d[face], dir)
        for o in orbits[face]:
            x = rotate([self.d[s][i] for [s, i] in o], dir)
            for i in range(0, 4):
                self.d[o[i][0]][o[i][1]] = x[i]
        return self

    def shuffle(self, n):
        for i in range(0, n):
            s = random.choice(sides)
            d = random.choice([-1, 1])
            print '[', s, d, ']'
            self.move(s, d)
        return self

    def copy(self):
        return copy.deepcopy(self)

    def solve(self):
        q = [Position(self)]
        while len(q) > 0:
            p = q[0]
            if p.solved():
                print "Solution: ", p.moves
                return
            q = q[1:] + [p.next(m) for m in p.candidate_moves()]

    def solved(self):
        for s in sides:
            if self.d[s] != [s, s, s, s]:
                return False
        return True


class Position:
    def __init__(self, cube, moves = []):
        self.cube = cube
        self.moves = moves

    def __str__(self):
        return str(self.moves) + '\n' + str(self.cube)

    def next(self, move):
        c = self.cube.copy().move(move[0], move[1])
        return Position(c, self.moves + [move])

    def candidate_moves(self):
        if len(self.moves) == 0:
            return [[s, d] for s in sides for d in [1, -1]]
        else:
            sx, dx = self.moves[-1]
            return [[s, d] for s in sides for d in [1, -1] if s != sx or d != dx]

    def solved(self):
        return self.cube.solved()
