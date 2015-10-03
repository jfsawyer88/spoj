## dragon curve
## starting from project euler code

# this fractal is generatred by repeatedly the whole curve
# by the latest point. first find all power of 2 points
# along the curve and rotate approprate ones around
# each other to find the final result


def mp(A, v):
    '''apply matrix A to vector v'''
    return [A[0][0]*v[0] + A[0][1]*v[1],
            A[1][0]*v[0] + A[1][1]*v[1]]
def diff(v, w):
    '''vector difference of v and w'''
    return [v[0]-w[0], v[1]-w[1]]
def add(v, w):
    '''vector addition of v and w'''
    return [v[0]+w[0], v[1]+w[1]]

def rot270(a, b):
    '''rotates point a 90 degrees about point b'''
    return add(b, mp([[0, 1], [-1, 0]], diff(a, b)))
    

def path(n):
    '''returns the path we need to take
       through the dragon curve to reach
       the point at the given step'''
    res = []
    while n != 2**(n.bit_length()-1):
        res.append(n.bit_length()-1)
        n = 2**(res[-1]+1) - n
    res.append(n.bit_length()-1)
    return res


# where the dragon will be at 2^i seconds
# for each index i. we only need to go
# up to 2^30 for this problem
tab = [[1, 0]]
for i in xrange(30):
    tab.append(rot270([0,0], tab[-1]))


def dragon_position(t):
    '''gives the dragon's position after t seconds'''

    if t == 0:
        return [0,0]

    dragon_path = path(t)
    pos = tab[dragon_path.pop()]

    while dragon_path:
        pos = rot270(pos, tab[dragon_path.pop()])
    return pos


if __name__ == "__main__":

    import sys

    s = sys.stdin
    t = int(s.readline())
    while t != -1:
        out = dragon_position(t)
        sys.stdout.write('(' + str(out[0]) + ',' + str(out[1]) + ')\n')
        t = int(s.readline())
