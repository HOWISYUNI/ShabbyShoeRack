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

def solution(N, M, graph):
    maxAisle = -math.inf
    viruses = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 2]
    aisles = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 0]
    walls = [(row, col) for row in range(len(graph)) for col in range(len(graph[row])) if graph[row][col] == 1]

    # 벽 세울 대상 선정
    candidates = list(combinations(aisles, 3))
    
    for p1, p2, p3 in candidates:
        tempGraph = copy.deepcopy(graph)
        # 벽을 3개 세우고
        tempGraph[p1[0]][p1[1]] = 1
        tempGraph[p2[0]][p2[1]] = 1
        tempGraph[p3[0]][p3[1]] = 1

    # graph에서 바이러스(2)의 주변 통로를 모두 바이러스(2)로 채움

    # graph의 통로 넓이 구하기
    # maxAisle = max(maxAisle, aisleSize)

    return maxAisle
