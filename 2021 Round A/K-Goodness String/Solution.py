#import sys
#sys.stdin = open('input.txt', 'r')

t = int(input())

for i in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    s = [char for char in input()]

    calck = 0
    j = 1
    while j < len(s)/2 + 1:
        if s[j - 1] != s[n - j]:
            calck += 1
        j += 1
    
    ans = 0
    if calck != k:
        ans = abs(k - calck)
    
    print('Case #{}: {}'.format(i, ans))

