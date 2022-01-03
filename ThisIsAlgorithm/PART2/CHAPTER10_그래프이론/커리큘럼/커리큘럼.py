from collections import deque
import copy
def topology_sort(adjacencyList, indegree, timeList, nodeCount):
    q = deque()
    result = copy.deepcopy(timeList)

    # 현재 진입차수가 0인 노드 찾기
    for idx, degree in enumerate(indegree):
        if idx == 0:
            continue

        if degree == 0:
            q.append(idx)
            result[idx] = timeList[idx] #  원래 root 노드인 노드의 result 초기화

    # 위상 정렬
    while q:
        now = q.popleft()
        for next_node in adjacencyList[now]:
            result[next_node] = max(result[next_node], result[now] + timeList[next_node]) #  최대만 갱신한다.
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

    return result

if __name__ == "__main__":
    import os 
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()

        nodeCount = int(lines[0].strip())
        adjacencyList = [[] for i in range(nodeCount + 1)]
        indegree = [0 for i in range(nodeCount + 1)]
        timeList = [0 for i in range(nodeCount + 1)]

        for child in range(1, nodeCount + 1):
            line = list(map(int, lines[child].strip().split()))
            timeList[child] = line[0]
            for parent in line[1:-1]:
                adjacencyList[parent].append(child)
                indegree[child] += 1

        result = topology_sort(adjacencyList, indegree, timeList, nodeCount)
        print(result)
                