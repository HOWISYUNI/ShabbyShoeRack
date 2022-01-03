def find_parent(parent, child):

    if parent[child] != child: #  루트 노드가 아닐 경우
        parent[child] = find_parent(parent, parent[child])  # parent 찾으러 가는 경로의 모든 노드를 하나의 parent로 갱신한다.

    return parent[child]

def union(a, b, parent):

    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)  #  부모를 찾아서
    parent[max(a_parent, b_parent)] = min(a_parent, b_parent) # 부모테이블을 갱신한다.

def solution(unions, parent, nodeCount):

    # 1. union 연산. 화살표 연결까지만 함
    for a, b in unions:
        union(a, b, parent)

    # 2. find_parent로 최종적으로 모든 노드 압축연산
    for node in range(1, nodeCount + 1):
        find_parent(parent, node)

    return parent


if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode='r') as f:

        unions = []
        max_val = 0
        lines = f.readlines()

        nodeCount, edgeCount = map(int, lines[0].strip().split())

        for i in range(1, len(lines)):
            line = list(map(int, lines[i].strip().split()))
            unions.append(line)

        # parent 초기화
        parent = [i for i in range(nodeCount + 1)]

        parent = solution(unions, parent, nodeCount)
        
    
    # 출력
    print('각 원소가 속한 집합 : ', end=' ')
    for idx, item in enumerate(parent):
        if idx != 0:
            print(item, end=' ')

    print()

    print('부모 테이블 : ', end=' ')
    for idx, item in enumerate(parent):
        if idx != 0:
            print(item, end=' ')

    print()