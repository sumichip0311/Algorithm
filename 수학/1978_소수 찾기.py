import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
value = 0
for num in data:
    count = 0
    if num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                count += 1
        if count == 1:
            value += 1    
            
print(value)