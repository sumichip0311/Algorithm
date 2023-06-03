import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data.sort(reverse=True)

sum = data[0]
for i in range(1, n):
    sum += data[i]/2

print('%g'%sum)