import sys

n = sys.stdin.readline().strip()
if len(n) == 1:
        n = n + '0'
value = int(n)
count = 0

while True:
    tmp = int(n[-2]) + int(n[-1])
    tmp = str(tmp)
    n = n[-1] + tmp[-1]
    count += 1
    if int(n) == value:
        break
print(count)