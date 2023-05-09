import sys

data = int(sys.stdin.readline())
list = [300, 60 , 10]
reslut = []

for num in list:
    tmp = data // num
    reslut.append(str(tmp))
    data = data % num

if data != 0:
    print(-1)
else:
    print(' '.join(reslut))