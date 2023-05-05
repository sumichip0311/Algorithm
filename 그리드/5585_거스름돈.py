import sys

data = int(sys.stdin.readline())
list = [500, 100, 50, 10, 5, 1]
cnt = 0
data = 1000 - data

for num in list:
    cnt += data // num
    data = data % num

print(cnt)