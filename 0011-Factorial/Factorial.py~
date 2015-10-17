## SPOJ
## FCTRL
## code from project euler 320

def Z(n):
    '''number of zeros at the end of n!'''
    q = n
    res = 0
    while q>0:
        q /= 5
        res += q
    return res

if __name__ == "__main__":

    import sys

    s = sys.stdin
    T = int(s.readline())
    for i in xrange(T):
        sys.stdout.write(str((Z(int(s.readline())))) + '\n')
