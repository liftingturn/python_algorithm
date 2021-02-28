#quick sort

#기준 데이터를 설정, 기준보다 큰 데이터와 작은데이터 자리를 옮기는 소팅 알고리즘
#일반적인 상황에서 가장 많이 사용됨
# 병합 정렬과 더불어, 대부분 프로그래밍 언어의 정렬라이브러리의 근간
# 가장 기본적인 퀵정렬은 첫번째 데이터를 기준데이터(Pivot) 으로 설정

list = [5,7,9,0,3,1,6,2,4,8] # pivot = 5
# 왼쪽에서부터 pivot보다 큰 데이터 선택 '7'
# 오른쪽(마지막인덱스)부터 pivot보다 작은 데이터 선택 '4' 
[5,4,9,0,3,1,6,2,7,8] #두 인덱스 교환 후
# 한번 더 ? 왼쪽에서부터 9, 오른쪽에서부터 2 발견, 교환
[5,4,2,0,3,1,6,9,7,8]
# 왼쪽에서부터 6, 오른쪽에서부터 1 발견, 서로 엇갈리는 상황에
# 6과 pivot을 교환,
# 이 때 pivot 기준으로 좌우로 크고 작음이 확실하게 나눠짐 : divide(분할완료)
[1,4,2,0,3,5,6,9,7,8]
#이후 pivot 기준 분할된 array 기준으로 동일 교환 반복 진행
[1,4,2,0,3],[5],[6,9,7,8]

#이상적인 경우 분할이 절반씩 일어난다면, 전체 연산 횟수 O(NlogN) 기대, 최악 O(N^2)
#이미 정렬된 리스트 대상으로 돌려보면 그런 결과가 발생

def quick_sort(array,start,end):
    if start >=end: #원소가 한개인 경우 종료
        return 
    pivot = start # 피벗은 첫 원소
    left = start +1
    right = end
    while(left<=right):
        #피벗보다 큰 데이터 찾을 때까지 반복
        while(left<end and array[left] <= array[pivot]):
            left+=1
        #피벗보다 작은 데이터 찾을떄까지 반복
        while(right>start and array[right]>=array[pivot]):
            right -=1
        if(left>right): #엇갈렸다면 작은데이터와 피벗을 교체 (divide)
            array[right],array[pivot] = array[pivot],array[right]
        else: #엇갈린거 아니면 left,right 교체
            array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽,오른쪽 각각 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

array = [5,7,9,0,3,1,6,2,4,8]
quick_sort(array,0,len(array)-1)


def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x>pivot]#분할된 오른쪽 부분

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

quick_sort(array)