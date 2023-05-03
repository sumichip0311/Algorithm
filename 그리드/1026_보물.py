import sys

n = sys.stdin.readline().split()
data1 = list(map(int,sys.stdin.readline().split())) # int형 list로 받아오기
data2 = list(map(int,sys.stdin.readline().split()))
max = 0

data1.sort() # 오름차순 정렬
data2.sort(reverse=True) #내림차순 정렬

for i in range(0, len(data1)): # list길이 만큼 계산
    max += int(data1[i]) * int(data2[i])

print(max)