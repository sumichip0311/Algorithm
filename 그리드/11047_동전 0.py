import sys
data = []
a, b = map(int, sys.stdin.readline().split())
count = 0
for _ in range(a):
    data.append(int(sys.stdin.readline().strip()))
    
for num in data[::-1]:
    count += b // num
    b = b % num
    
print(count)