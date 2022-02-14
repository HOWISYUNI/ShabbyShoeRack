# BFS : 가까운 노드부터 탐색
## 자주 쓰는 경우
1. 최단거리 탐색
    - PART2 미로탈출
    - PART3 Q15 특정거리의 도시 찾기

## 기본 틀
'''python
q = deque()
q.append(node)

while q:
    curNode = q.popleft() # 현재 방문한 노드 
    visited[curNode] = True # 방문처리
    for adjNode in adjList[curNode]: # 현재 노드에 인접한 노드 찾기
        if not visited[adjNode]: # 인접 노드가 아직 방문하지 않은 노드라면
            q.append(adjNode) # 다음 방문 대상 처리. 다양한 경로를 고려할 수 있다. - PART3 Q15 특정거리의 도시 찾기
'''

# DFS : 가장 먼 노드부터 탐색