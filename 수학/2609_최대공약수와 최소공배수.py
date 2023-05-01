import sys
import math

a, b = map(int, sys.stdin.readline().split())

def gcd2(a,b):
    while b > 0:
        a, b = b, a % b
    return a

print(math.gcd(a, b)) 
print(gcd2(a,b))
print(int((a * b) / math.gcd(a, b)))