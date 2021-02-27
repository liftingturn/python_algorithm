# 현재 상황에서 당장 좋은것만 고르는 방법
# 정당성 분석이 중요. 당장 가장 좋은것만 골라도 최적의 해를 구할 수 있는지

n = 1260
count= 0

array = [500,100,50,10]

n,k = input().split()

# 그리디

n,k = map(int,(input().split()))

count = 0

while n>1:
    if n%k == 0:
        n = n/k
    else: 
        n -= 1
    count +=1
print(count)


n = int(input())
array = map(int,input().split())
array.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹 포함된 포험가 수

for fear in array: #공포도를 낮은 것 부터 하나씩 확인
    count += 1 #현재 그룹에 해당 모험가 포함
    if count >= fear: # 현재 포함된 모험가수가 현재 공포도 이상이면 그룹 fix
        result += 1 #그룹 수 증가
        count = 0 #현재 그룹 비워주기
print(result) 

#구현 유형 : 풀이를 떠올리는건 쉽지만 소스코드로 옮기기 어려움
# 알고리즘 간단 but 코드가 길어지는 형태
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 적절한 라이브러리를 찾아야 하는 문제

# 알고리즘에서 2차원 공간은 matrix 의 의미로 사용됨

# 상하좌우 : 시뮬레이션 유형 - 명령에 따라 차례대로 이동하는 형태

n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ["L","R","U","D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx,ny
