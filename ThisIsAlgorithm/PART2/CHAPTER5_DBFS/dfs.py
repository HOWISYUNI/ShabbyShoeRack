
def dfs(graph, node, visited, history):

    history.append(node)
    visited[node] = True

    # 방문하지 않은 인접 노드 구하기
    adjacents = graph[node]
    not_visited = [adjacent for adjacent in adjacents if adjacent not in visited]

    if not not_visited: # 방문하지 않은 노드가 없으면 리턴한다. 사실 밑에 for문을 다 돌면 이 조건은 필요없긴하다.
        return

    for node_num in graph[node]: # 말단노드가 연결되지 않은 경우는 여기서 체크한다.
        if not visited[node_num]: # 방문하지 않은 노드만 다시 들어가본다.
            dfs(graph, node_num, visited, history)


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
    dfs(graph, node=1, visited=visited, history=history)
    print(history)