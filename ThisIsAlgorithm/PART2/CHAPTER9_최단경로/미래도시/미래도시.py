import os
from itertools import product

def floydwarshall(adjacency_list, company_counts):

    # INIT
    min_distance_matrix = [[float('inf') for _ in range(company_counts + 1)] for _ in range(company_counts + 1)]
    for i in range(1, company_counts + 1):
        min_distance_matrix[i][i] = 0
        for dest in adjacency_list[i]:
            min_distance_matrix[i][dest] = 1

    # floydwarshll
    iteration_unit = range(1, company_counts + 1)
    for junction, source, destination in product(iteration_unit, iteration_unit, iteration_unit):
        if source != junction and destination != junction and source != destination:
            direct = min_distance_matrix[source][destination]
            detour = min_distance_matrix[source][junction] + min_distance_matrix[junction][destination]
            # floydwarshall 알고리즘 점화식
            min_distance_matrix[source][destination] = min(direct, detour)


    return min_distance_matrix


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode = 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        company_counts, edge_counts = map(int, lines[0].split())
        
        adjacency_list = [set() for _ in range(company_counts + 1)]
        for i in range(1, edge_counts + 1):
            node1, node2 = map(int, lines[i].split())
            adjacency_list[node1].add(node2)
            adjacency_list[node2].add(node1)

        destination, junction = map(int, lines[edge_counts + 1].split())
        source = 1

    min_distance_matrix = floydwarshall(adjacency_list, company_counts)
    min_distance = min_distance_matrix[source][junction] + min_distance_matrix[junction][destination]
    if min_distance == float('inf'):
        print(-1)
    else:
        print(min_distance)