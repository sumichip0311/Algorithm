data = input().split('-') # '-'를 기준으로 split해서 data 리스트에 저장

list = [] # '_' 로 나눈 항들의 합을 저장할 리스트

for num in data:
    sum = 0
    tmp = num.split('+') # 덧셈을 위해 '+'를 기준으로 split
    for pnum in tmp:
        sum += int(pnum) # split한 리스트의 각 요소들을 int로 형변환 해주고 더함
    list.append(sum) # 각 항의 덧셈 연산한 값을 list에 저장

n = list[0] # 0번째 값으로 초기화 해줍니다

for i in range(1, len(list)): 
    n -= list[i] # 1부터 뺄셈을 진행합니다
print(n)