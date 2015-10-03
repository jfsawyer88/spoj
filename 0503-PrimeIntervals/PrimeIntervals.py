## SPOJ
## Prime Intervals
## Same code as Prime Generator (id: 0002)

def primes_upto(limit):
    '''returns all primes up to limit'''
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in xrange(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in xrange(n**2, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def primes_between(a, b):
    '''returns a list of primes between a and b, inclusively'''
    a = max(a, 2)
    ps = primes_upto(int(b**0.5) + 1)
    P = [1] * (b - a + 1)
    for p in ps:
        for k in xrange((-a)%p, b-a+1, p):
            if k + a <= p: continue
            P[k] = 0
    return [a+i for i, prime in enumerate(P) if prime]


import sys

s = sys.stdin
n = int(s.readline())

for i in xrange(n):
    a, b = map(int, s.readline().strip().split(' '))
    for p in primes_between(a, b):
        sys.stdout.write(str(p) + '\n')
    sys.stdout.write('\n')
