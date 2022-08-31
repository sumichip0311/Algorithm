import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
reslut = []
tmp = 0
data = sorted(data)
print(data)

for num in data:
    tmp += num
    reslut.append(tmp)
    
print(sum(reslut))