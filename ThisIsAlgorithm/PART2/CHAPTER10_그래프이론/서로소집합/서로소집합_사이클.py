def find_parent(parent, child):

    if parent[child] != child:
        parent[child] = find_parent(parent, parent[child]) #  루트를 찾아가는 경로의 모든 노드를 같은 parent로 갱신

    return parent[child]

def union(a, b, parent):

    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)  # 루트 노드를 찾아서
    parent[max(a_parent, b_parent)] = min(a_parent, b_parent) #  부모 테이블을 갱신한다.

def solution(unions, parent, nodeCount):

    # 1. union
    for a, b in unions:
        a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
        if a_parent == b_parent:  # cycle
            print("사이클이 발생했습니다.")
            return
        else:
            union(a, b, parent)

    # 2. 압축연산
    for node in range(1, nodeCount + 1):
        find_parent(parent, node)


if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc_cycle.txt'), mode='r') as f:

        unions = []
        max_val = 0
        lines = f.readlines()

        nodeCount, edgeCount = map(int, lines[0].strip().split())

        for i in range(1, len(lines)):
            line = list(map(int, lines[i].strip().split()))
            unions.append(line)

        # parent 초기화
        parent = [i for i in range(nodeCount + 1)]

        solution(unions, parent, nodeCount)