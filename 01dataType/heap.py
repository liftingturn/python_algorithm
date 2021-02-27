import heapq

#우선순위 큐 : 특정 기준에 따라 우선순위가 가장 높은 데이터를 가장 먼저 삭제할 때 유용한 자료구조.

# stack : 마지막에 들어간거 삭제할 때
# queue : 가장 먼저 들어간거 삭제할 때
# priority queue : 가장 우선순위가 높은 데이터

# 리스트 시간복잡도 삽입 : O(1), 삭제 : O(N)
# 힙 시간복잡도 삽입 : O(logN), 삭제 : O(logN)

#단순히 N개 데이터를 모두 넣었다 빼는 작업은 힙정렬과 동일. O(NlogN)

# heap(이하 힙)은 부모 노드가 자식 보다 작거나 같은 값을 갖는 이진트리
# 따라서 루트 노드가 pop됨

heap1 =[1,3,2,5,1,4]

heapq.heapify(heap1) # 해당 리스트를 heap 형태로 변환 mutate
print(heap1) #[1, 1, 1, 2, 2, 3, 4]

popValue = heapq.heappop(heap1)  # 루트 노트 value pop
print(popValue,heap1) #1 [1, 1, 3, 2, 2, 4]

heapq.heappush(heap1,100) # 해당 밸류 삽입 후 자동 정렬
print(heap1) #[1, 1, 3, 2, 2, 4, 100]

def heap_sort(nums):  # 일반 list sort의 경우 최악에 O(N^2)발생 방지를 위해 힙소트 사용
  heap = nums
  heapq.heapify(heap)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))