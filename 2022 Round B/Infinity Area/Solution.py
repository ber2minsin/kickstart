from math import pi
# import sys
# sys.stdin = open('input.txt', 'r')
t = int(input())

# There is def. a better way to do this
def solve(r, last, last_op):
    if last_op == 'a':
        # Break case
        if int(r / b) <= 0:
            return last + [r]
        else:
            return solve(int(r/b), last + [r], 'b')
    elif last_op == 'b':
        return solve(int(r*a), last + [r], 'a')
    

# Solves in O(n^2)
for case in range(1, t+1):
    r, a, b = [int(x) for x in input().split()]

    radii = solve(r, [], 'b')
    ans = 0
    for radius in radii:
        ans += radius * radius

    ans = ans * pi
    print("Case #{}: {}".format(case, ans))