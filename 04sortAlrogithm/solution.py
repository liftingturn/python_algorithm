# length N의 List A,B 존재. 모두 자연수
# A와 B의 원소 하나씩 서로 교체하는 바꿔치기 연산을 최대 K번 수행 가능.
# 목표는 배열 A의 모든 원소 합이 최대가 되도록
 
 #예시
 # N : 5, K:3, A:[1,2,5,4,3] , B:[5,5,6,6,5]
 # 핵심 아이디어 : 매번 A의 가장 작은 원소와 B의 가장 큰 원소를 교체

#두 배열의 원소가 최대 100,000개 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 함

n,k = map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break