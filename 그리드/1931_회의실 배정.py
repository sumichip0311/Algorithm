import sys

n = int(sys.stdin.readline())
data = []
count = 0
tmp = 0
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
    
#data.sort(key= lambda x: x[0])
data.sort(key= lambda x: x[1])

for num in data:
    if tmp <= num[0]:
        count += 1
        tmp = num[1]

print(count)
    