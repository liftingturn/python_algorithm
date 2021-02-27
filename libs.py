#내장함수 : 기본 함수들

#itertools : 반복형태 유용 함수들. 순열/조합 알고리즘에서 사용
# 모든 경우의 수 고려할 시
# 순열 : 순서 상관있는 경우의 수 nPr  n + ... +n-r+1
# 조합 : 순서 상관없는 경우의 수 nCr  (n + ... +n-r+1)/r!

from itertools import permutations

data = ['a','b','c']
result = list(permutations(data,3))

from itertools import combinations
result = list(combinations(data,3))

#중복순열
from itertools import product
result = list(product(data,repeate=2)) #2개를 뽑는 모든 순열 (중복허용)

from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data,2))

#counter : Collections
from collections import Counter
counter = Counter(['a','b','a'])
counter['a'] = 2
dict(counter) 


#heapq : 우선순위 큐 기능

#bisect : 이진탐색기능

#collections : deque

#math 최대공약수 gcd 최소공배수 lcm
import math
math.gcd(a,b)
math.lcm(a,b)






result = sum([1,2,3,4])

min_result = min(3,5,1,2)
max_result = max(1,2,3,4)

result = eval("(3+5)*7")

sorted([1,3,2,4,5],reverse=True)
sorted([1,3,2,4,5],lambda x:x[2],reverse=True)