'''
풀이시간 : 40분
시간제한 : 2초
메모리제한 512MB

N x M 그래프
빈칸, 벽, 바이러스 = 0, 1, 2
바이러스는 상하좌우로 퍼짐 = DBFS
벽 3개를 꼭 세워서 바이러스 퍼진 후 통로의 최대 넓이 구하기
'''
import math, copy
from itertools import combinations
from collections import deque

def solution(N, M, graph):
    maxAisle = -math.inf
    viruses = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 2]
    aisles = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 0]
    # walls = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 1]

    # 상하좌우 순서
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    # 벽 세울 대상 선정
    candidates = list(combinations(aisles, 3))
    
    for p1, p2, p3 in candidates:
        tempGraph = copy.deepcopy(graph)
        # 벽을 3개 세우고
        tempGraph[p1[0]][p1[1]] = 1
        tempGraph[p2[0]][p2[1]] = 1
        tempGraph[p3[0]][p3[1]] = 1

        q = deque(viruses) # bfs 큐 선언
        visited = [[False for _ in range(M)] for _ in range(N)]
        # 바이러스 전염 : BFS. graph에서 바이러스(2)의 주변 통로를 모두 바이러스(2)로 채움
        while q:
            x, y = q.popleft() # 현재 노드 좌표
            tempGraph[x][y] = 2 # 현재 노드 바이러스 감염 처리
            visited[x][y] = True # 방문처리
            # 상하좌우 방문
            for dx, dy in zip(dxs, dys):
                nx = x+dx
                ny = y+dy
                if isValid(nx, ny, N, M) and not visited[nx][ny] and tempGraph[nx][ny] == 0:  # 유효하고 안가봤고 통로라면
                    q.append((nx, ny)) # 다음 방문 대상 처리

        # graph의 통로 넓이 구하기
        aisleSize = 0
        for x in range(N):
            for y in range(M):
                if tempGraph[x][y] == 0:
                    aisleSize += 1
        
        # 최대 통로 넓이(maxAisle) 갱신
        maxAisle = max(maxAisle, aisleSize)
    
    return maxAisle

def isValid(nx, ny, N, M):
    return 0 <= nx < N and 0 <= ny < M

if __name__ == "__main__":
    # case 1
    N, M = 7, 7
    graph = [
        [2,0,0,0,1,1,0],
        [0,0,1,0,1,2,0],
        [0,1,1,0,1,0,0],
        [0,1,0,0,0,0,0],
        [0,0,0,0,0,1,1],
        [0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0]
    ]

    # # case 2
    N, M = 4, 6
    graph = [
        [0,0,0,0,0,0],
        [1,0,0,0,0,2],
        [1,1,1,0,0,2],
        [0,0,0,0,0,2]
    ]

    # # case 3
    # N, M = 8, 8
    # graph = [
    #     [2,0,0,0,0,0,0,2],
    #     [2,0,0,0,0,0,0,2],
    #     [2,0,0,0,0,0,0,2],
    #     [2,0,0,0,0,0,0,2],
    #     [2,0,0,0,0,0,0,2],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    # ]

    print(solution(N, M ,graph))