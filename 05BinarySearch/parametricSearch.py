#최적화 문제를 결정문제(Y|N)으로 바꾸어 해결하는 기법 => 이진탐색 적합

# first-fit 기억장치 배치 전략 원하는 내부 단편화 크기 있을 시, 적재 프로그램 용량 계산하기

n,m = list(map(int,input().split(' ')))  #빈공간 갯수 n, 내부단편화 크기 m

array = list(map(int,input().split())) # 빈 공간 크기 리스트

# 이진탐색 시작을 위한 시작,끝점 설정
start = 0
end = max(array)

result = 0
while(start<=end):
    total=0
    mid = (start+end)//2 #중간점
    for x in array:
        if x>mid:
            total+=x-mid
        if total<m:
            end=mid-1
        else:
            result=mid
            start=mid+1


#문제 2:
# N개 원소를 포함하고 있는 오름차순의 수열 (정렬되어있음)
# 수열에서 x가 등장하는 횟수 계산 ex) 수열 {1,1,2,2,2,2,3} , x=2 일 때, 값이 2인 원소가 4개이므로 4 출력
# 시간복잡도 O(logN)필수  -> 선형 탐색으로는 시간 초과(1~N). 정렬이 되어있으므로 이진탐색 수행 가능

#이진탐색으로 시작점과 끝점을 구해서 빼주면 됨
from bisect import bisect_left, bisect_right

def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index-left_index

count = count_by_range(array,x,x)
if(count==0):
    print(-1)
else:
    print(count)