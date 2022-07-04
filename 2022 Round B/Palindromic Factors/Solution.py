from math import floor

#import sys
#sys.stdin = open('input.txt', 'r')


t = int(input())

def factorsof(n):

    factrs = []
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            factrs.extend([str(n//i), str(i)])
    return set(factrs)

for case in range(1, t+1):
    a = int(input())
    factors = factorsof(a)
    ans = 0
    
    for i in factors:
        is_palindrome = True
        for j in range(floor(len(str(i))/2)):
            if str(i)[j] != str(i)[-j - 1]:
                is_palindrome = False
                continue
        if is_palindrome:
            ans += 1
    
    print("Case #{}: {}".format(case, ans))