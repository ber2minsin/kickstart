
import numpy

#import sys
#sys.stdin = open('input.txt', 'r')


# Sieve of Eratosthenes
def primesof(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


T = int(input())
for case in range(1, T+1):
    z = int(input())
    result = None
    primes = primesof(min(z, 1000000))


    difference = numpy.Infinity
    for i in range(len(primes)):
        if i + 1 < len(primes):
            product = int((primes[i] * primes[i + 1]))
            
            if product <= z:
                difference = min(difference, abs(z - product))
            else:
                break

        result = z - difference
    
    print("Case #{}: {}".format(case, result))

