
#import sys
#sys.stdin = open('input.txt', 'r')

T = int(input())

for case in range(1, T+1):
    n = int(input())
    s = input()

    result = '1 '
    alphabet = [chr(c) for c in range(ord('A'),ord('Z')+1)]

    values = [alphabet.index(letter) for letter in list(s)]

    succesion = 1
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            succesion += 1
        else:
            succesion = 1
        result += str(succesion) + ' '

    print("Case #{}: {}".format(case, result))