import os
from itertools import product

def floydwarshall(min_distance_matrix, node_counts):

    # a -> b vs a -> junction -> b 를 1 ~ node_counts 순회하며 돈다

    # 3중 for 문
    # for junction in range(1, node_counts + 1):
    #     # juction을 제외한 나머지 노드로 경로 구성
    #     for source in range(1, node_counts + 1):
    #         for destination in range(1, node_counts + 1):
    #             if source != junction and destination != junction and source != destination:
    #                 direct = min_distance_matrix[source][destination]  # a -> b
    #                 detour = min_distance_matrix[source][junction] + min_distance_matrix[junction][destination]  # a -> junction -> b
    #                 if detour < direct:  # junction을 거쳐가는게 빠르다면
    #                     min_distance_matrix[source][destination] = detour

    # 3중 for문은 itertools의 product(데카르트 곱)을 사용하면 쉽게 구현할 수 있다.
    iteration_unit = list(range(1, node_counts + 1))
    for junction, source, destination in product(iteration_unit, iteration_unit, iteration_unit):
        if source != junction and destination != junction and source != destination:
            direct = min_distance_matrix[source][destination]  # a -> b
            detour = min_distance_matrix[source][junction] + min_distance_matrix[junction][destination]  # a -> junction -> b
            # floyd warshall 알고리즘 점화식 적용
            min_distance_matrix[source][destination] = min(direct, detour)



if __name__ == "__main__":
    # node_counts = int(input())
    # edge_counts = int(input())

    # min_distance_matrix = [[float('inf') for _ in range(node_counts + 1)] for _ in range(node_counts + 1)]
    # for i in range(edge_counts):
    #     source, destination, distance = map(int, input().split())
    #     min_distance_matrix[source][destination] = distance
    #     min_distance_matrix[i][i] = 0  

    
    # INIT
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode='r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        node_counts = int(lines[0])
        edge_counts = int(lines[1])

        min_distance_matrix = [[float('inf') for _ in range(node_counts + 1)] for _ in range(node_counts + 1)]
        for i in range(2, len(lines)):
            source, destination, distance = map(int, lines[i].strip().split())
            min_distance_matrix[source][destination] = distance
        
        for i in range(1, node_counts + 1):
            min_distance_matrix[i][i] = 0

    # floydwarshall 알고리즘 적용
    floydwarshall(min_distance_matrix, node_counts)
    
    # 결과 출력
    for i in range(1, node_counts + 1):
        for j in range(1, node_counts + 1):
            if j % 4 == 0:
                print(min_distance_matrix[i][j], end='\n')
                continue
            print(min_distance_matrix[i][j], end=' ')
