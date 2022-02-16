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

# 유의사항
## 시간초과
1. DBFS를 감싸는 for문이 많아질수록 로직이 복잡해져 시간초과날 수 있음. DBFS를 감싸는 반복문을 제거할 것.
    연구소문제 큐 만들 때 q(viruses)로 bfs 동작 전 for 문으로 q.append(v) 하는 동작을 제거할 수 있었음