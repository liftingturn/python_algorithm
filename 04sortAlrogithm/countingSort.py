# 계수 정렬
# 특정 조건이 부합할 때만 사용할 수 있지만, 매우 빠르게 동작.
# 조건이란, 데이터의 크기범위가 제한, 정수형태로 표현할 수 있을 것
# 데이터의 개수가 N, 데이터 최대값이 K일 경우, 최악에도 O(N+K) 보장

def countingSort(array):
    count = [0]*(len(array)+1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i,end='')

# 데이터가 0과 999,999만 존재할 경우, 카운트 리스트가 쓸데없이 돌아감.
# 중복값이 다수인 리스트에 효과적