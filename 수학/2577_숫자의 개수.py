import sys
from math import prod

data = [int(sys.stdin.readline().strip()) for i in range(3)]
value = str(prod(data))
memo = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for num in value:
    memo[num] += 1

for key, value in memo.items():
    print(value)