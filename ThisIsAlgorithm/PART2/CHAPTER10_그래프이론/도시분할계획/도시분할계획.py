def find_parent(parent, child):

    if parent[child] != child:
        parent[child] = find_parent(parent, parent[child])

    return parent[child]

def union(a, b, parent):
    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
    parent[max(a_parent, b_parent)] = min(a_parent, b_parent)

def solution(edges):
    max_cost = 0
    total_cost = 0

    for a, b, cost in edges:
        if find_parent(parent, a) == find_parent(parent, b):
            # 사이클 발생
            continue
        else:
            union(a, b, parent)
            total_cost += cost #  전체 유지비
            max_cost = max(max_cost, cost)

    return total_cost - max_cost

if __name__ == "__main__":
    import os 
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()

        nodeCount, edgeCount = map(int, lines[0].strip().split())

        parent = [i for i in range(nodeCount + 1)] # 0번부터 nodeCount번 까지 사용한다.
        edges = []

        for i in range(1, nodeCount + 1):
            a, b, cost = map(int, lines[i].strip().split())
            edges.append((cost, a, b))

        edges.sort()

        # 최소 신장 트리
        result = solution(edges)
        print(result)