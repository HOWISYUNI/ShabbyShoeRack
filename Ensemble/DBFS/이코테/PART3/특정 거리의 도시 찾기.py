'''
풀이시간 : 30분
시간제한 : 2초
메모리제한 256MB

1 ~ N 의 노드
M개의 연결 도로
모든 도로의 거리 1
X에서 출발, 최단 거리 K로 도달할 수 있는 모든 노드 출력
'''
from collections import deque
import math

def solution(N, M, K, X, adjList):
    minLength = [math.inf for _ in range(N)]
    minLength[X-1] = 0 # 출발지
    visited = [False for _ in range(N)]
    q = deque()
    q.append(X-1)

    while q:
        curNode = q.popleft()
        visited[curNode] = True # 방문처리
        for adjNode in adjList[curNode]:
            if not visited[adjNode]:
                q.append(adjNode) # 다음 방문 대상 노드 추가. 여기서 append 해야 다양한 경로를 고려할 수 있다
                if minLength[curNode] + 1 < minLength[adjNode]: # 현재노드 + 1의 최단거리로 갈 수 있다면
                    minLength[adjNode] = minLength[curNode] + 1 # 직전 노드 + 1 = 방문 노드로의 최단 거리
                    # print(curNode+1, adjNode+1, minLength)

    return [i+1 for i, val in enumerate(minLength) if val == K]
    

if __name__ == "__main__":
    N, M, K, X = 4, 4, 2, 1
    adjList = [
        [1, 2],
        [2, 3],
        [],
        []
    ]
    print(solution(N, M, K, X, adjList))