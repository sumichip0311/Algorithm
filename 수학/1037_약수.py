import sys

n = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
    
print(min(data) * max(data))