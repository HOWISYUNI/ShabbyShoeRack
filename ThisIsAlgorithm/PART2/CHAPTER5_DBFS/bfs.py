from collections import deque

def bfs(graph, node, visited, history):
    '''
    BFS 기본구조
    1. while q
    2. cur_node = q.popleft()
    3. for linked_node in graph[cur_node] : 인접 노드 모두 순회 ( 다양한 방법으로 linked_node를 찾아낸다. floodfill처럼!)
    4. if not visited[linked_node]: q.append(linked_node), visited[linked_node] = True
    5. 4번 if 조건문에 원하는 조건 추가
    '''

    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        cur_node = q.popleft()
        history.append(cur_node)

        for linked in graph[cur_node]: # 현재 노드(cur_node)에서 다음 노드를 방문하는 부분
            if not visited[linked]:
                q.append(linked)
                visited[linked] = True # 이 부분이 방문했다! 를 뜻하는 부분임


if __name__ == "__main__":
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False for _ in range(len(graph))]
    history = []
    bfs(graph, node=1, visited=visited, history=history)
    print(history)