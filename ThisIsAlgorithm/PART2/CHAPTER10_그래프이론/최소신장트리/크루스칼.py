def find_parent(parent, child):

    if parent[child] != child:
        parent[child] = find_parent(parent, parent[child])

    return parent[child]

def union(a, b, parent):
    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
    parent[max(a_parent, b_parent)] = min(a_parent, b_parent)

def solution(edges, parent):
    result = 0

    for edge in edges:
        cost, node1, node2 = edge
        # cycle이 생기지 않아야한다.
        if find_parent(parent, node1) != find_parent(parent, node2):
            union(node1, node2, parent)
            result += cost

    return result

if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        edges = []
        max_val = 0
        lines = f.readlines()

        nodeCount, edgeCount = map(int, lines[0].strip().split())

        for i in range(1, len(lines)):
            node1, node2, cost = list(map(int, lines[i].strip().split()))
            edges.append((cost, node1, node2))
        # parent 초기화
        parent = [i for i in range(nodeCount + 1)]

        # edges 정렬. 크루스칼은 edges를 작은 숫자부터 넣어야한다.
        edges.sort()

        result = solution(edges, parent)
        print(result)