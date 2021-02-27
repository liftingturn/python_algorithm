#많은 수의 경우의 수를 탐색해야 하는 경우 사용.

#stack 자료형 사용

stack = []
stack.append(5)
stack.pop()

print(stack[::-1])

#queue ->

from collections import deque

queue = deque()

queue.append(5)
queue.popleft()

# 재귀
def factorial_recursive(n):
    if n<=1:
        return 1
    else:
        return n*factorial_recursive(n-1)

#최대공약수 계산 (유클리드 호제법)
from math import gcd
A= 65
B = 3
R = A % B 
if(R==0):
    # return B
else:
    # return gcd(B,R)

#DFS : depth-first search

#각 노드가 연결된 정보 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8], #1 번 노드 인접 노드들
    [1,7]  #2 번 노드 인접 노드들
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현 
visited =[False] * 9


def dfs(graph,v,visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

        

#bfs : breadth-first seach 너비우선탐색 -> 가까운 노드부터

from collections import deque

def bfs(graph,start,visited):
    #큐 구현 위해 deque 라이브러리사용
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        

