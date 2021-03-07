#순차탐색 : 리스트 안에서 특정 데이터를 찾기 위해 앞에서부터 하나씩 확인
#이진탐색 : '정렬'되어있는 리스트에서 탐색범위를 '절반'씩 좁혀가며 탐색하는 방법 -> O(logN)

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2  #몫 연산자
    #중간점 값 기준 분기
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)



# 파이썬 라이브러리
# bisect_left|right(a,x) => 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 left|right쪽 인덱스 return

from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4

leftResult = (bisect_left(a,x)) #2
rightResult =(bisect_right(a,x)) #4