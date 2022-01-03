from collections import deque

def topoloy_sort(adjacency_list, indegree, nodeCount):
    q = deque()
    result = [] #  방문한 노드 정보 담기

    # 시작 노드(진입차수 = 0)를 q에 저장
    for idx in range(1, nodeCount + 1):
        if indegree[idx] == 0: #  시작노드라면
            q.append(idx) #  큐에 넣는다

    while q:
        now = q.popleft()
        result.append(now) #  popleft == 방문했다

        #  now의 인접노드를 확인
        for adjacent in adjacency_list[now]:
            indegree[adjacent] -= 1 #  인접노드로 연결된 간선 제거
            if indegree[adjacent] == 0: #  인접노드가 시작노드가 된다면
                q.append(adjacent) #  queue 에 넣는다


    return result


if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        
        lines = f.readlines()

        nodeCount, edgeCount = map(int, lines[0].strip().split())
        # 그래프 정보를 인접리스트에 저장
        adjacency_list = [[] for i in range(nodeCount + 1)]
        # indegree. 진입차수 정보
        indegree = [0 for i in range(nodeCount + 1)]

        for i in range(1, len(lines)):
            source, destination = list(map(int, lines[i].strip().split()))
            adjacency_list[source].append(destination) #  그래프 정보
            indegree[destination] += 1 #  sourdce --> destination 이니까 destination ++

        result = topoloy_sort(adjacency_list, indegree, nodeCount)
        print(result)

        