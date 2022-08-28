import sys

n = int(sys.stdin.readline())
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    avg = sum(data[1:]) / data[0]
    cnt = 0
    for num in data[1:]:
        if num > avg:
            cnt += 1
    rate = cnt / data[0] * 100
    print(f"{rate:.3f}%")