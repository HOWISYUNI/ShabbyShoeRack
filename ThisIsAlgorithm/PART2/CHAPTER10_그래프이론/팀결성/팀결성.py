def find_parent(parent, child):

    if parent[child] != child:
        parent[child] = find_parent(parent, parent[child])

    return parent[child]

def union(a, b, parent):
    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


if __name__ == "__main__":
    import os 
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()

        nodeCount, operationCoount = map(int, lines[0].strip().split())

        parent = [i for i in range(nodeCount + 1)] # 0번부터 nodeCount번 까지 사용한다.

        for i in range(1, operationCoount + 1):
            op, a, b = map(int,lines[i].strip().split())

            if op == 0:
                # 팀 합치기 연산 == union
                union(a, b, parent)
            elif op == 1:
                # 같은 팀 여부 확인 == find_parent
                a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
                if a_parent == b_parent:
                    print("YES")
                else:
                    print("NO")