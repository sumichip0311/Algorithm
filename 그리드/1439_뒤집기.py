import sys

data = sys.stdin.readline().strip()
cnt = 0
tmp = '?'

for num in data:
    if num != tmp:
        tmp = num
        cnt += 1

print(cnt//2)