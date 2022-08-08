import sys
n = int(sys.stdin.readline())

for i in range(1, 9 + 1):
    print("{} * {} = {}".format(n, i, n*i))