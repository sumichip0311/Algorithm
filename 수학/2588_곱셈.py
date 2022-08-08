import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()

for i in range(len(b), 0, -1):
    print(a * int(b[i-1]))

print(a * int(b))