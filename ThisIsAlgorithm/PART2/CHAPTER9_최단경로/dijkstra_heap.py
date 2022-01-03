import heapq

"""
최단 거리 알고리즘은, 시작점으로부터 나머지 점까지의 최단거리를 구하는 알고리즘이다.
목표는 언제나 시작점으로부터의 최단거리를 기록한다는 것임을 잊지말아야한다.
다익스트라 알고리즘은 현재 시점에서 매 턴마다 시작점으로부터의 최소거리 노드를 찾아, 최소거리 테이블을 갱신한다.
최소거리 테이블의 최소거리 노드(a)를 찾는 이유는, a를 거쳐서 a 이외의 다른 노드로 더 짧은 거리로 갈 수도 있기 때문이다. 
뿐만 아니라 더이상 a 까지의 최소 거리를 찾을 수 없음을 보장한다. 이후 a까지의 거리는 현재 최소거리에 최소 1을 더해서 찾은 거리이기 때문이다. 

예를들어, 시작 노드 a에 b와 c가 각각 2와 3의 거리로 연결돼있다고 하자. 나머지 노드는 나름의 방식으로 연결돼있다.
a -> b 거리가 2, a -> c 거리가 3이므로 다음 반복문의 최소거리 노드는 b 가 선택되고, b에 연결된 노드들의 a로 부터의 최소거리가 갱신될 수도 있다.
또한, a에 연결된 노드의 최솟값이 2임을 알게되므로 어떠한 방식으로 돌아오든 b로 가기위해선 2보다 무조건 크다.

이 최소 거리 노드를 찾는 방식에 있어 simple 다익스트라와 heap 다익스트라의 차이가 있다.  

simple 다익스트라는 매 반복마다 방문하지 않았으면서 최소거리테이블의 최소거리 노드(v)를 확인해(방문처리), 다음 턴의 노드(v*)를 통해서는 v로 최단거리로는 갈 수 없음과 v까지의 최소거리는 구했음을 보장한다. 
heap 다익스트라는 매 반복마다 갱신되는 값이 해당 노드의 최솟값임을 이용하고, 갱신된 값을 최소힙에 넣는다. 
힙에서 pop된 원소(a) 이후의 모든 거리는 a까지의 거리보다 무조건 크다. 이는 a로 최소 거리로 갈 수 없음과 동시에 이후 모든 거리는 a까지의 거리보다 작음을 보장한다. 

simple 다익스트라는 최소 거리 리스트 + visited 리스트를 활용한다.
heap 다익스트라는 최소 거리 리스트 + 힙큐(최소 거리 노드만을 찾기위한 용도) 를 활용한다.

1. 현재 노드로 부터 연결된 노드를 찾는다.
2. 연결된 노드 중 최소 거리 리스트를 갱신시킨 노드가 존재한다면 힙에 넣는다.
3. 최소 힙의 원소가 존재하지 않을 때 까지 1~2를 반복한다.
"""

def dijkstra_heap(adjacency_list, start_node):
    min_distance_list = [float('inf') for _ in range(len(adjacency_list))]
    min_distance_list[start_node] = 0
    # 힙큐는 오로지 최소 거리 노드만을 찾기 위한 용도
    hq = [(0, start_node)]
    heapq.heapify(hq)  # 힙큐는 명시적으로 heapify하는게 좋다.

    while hq:
        cost_to_junction, junction = heapq.heappop(hq)  # 고려할 source node를 받아온다.

        # 만약 이미 최솟값인 노드라면 다음 노드를 고려하지 않는다. 어차피 가봤자 지금 최솟값보다 항상 큰 거리가 나오니까.
        if cost_to_junction > min_distance_list[junction]:
            continue

        # junction을 거쳐 최소 거리를 갱신할 수 있는지 확인해보자. 새로운 최소거리를 찾아보자
        # 즉, source -- (junction) -- destination  VS  source -- destination  을 비교하는 싸움이다.
        for destination, cost_to_destination in adjacency_list[junction]:
            if min_distance_list[destination] > cost_to_junction + cost_to_destination:  # 새로운 최소 거리가 갱신된다면
                min_distance_list[destination] = cost_to_junction + cost_to_destination  # 갱신된 최소거리를 기억하고
                heapq.heappush(hq, (min_distance_list[destination], destination))  # (거리, 노드번호) 로 hq에 넣는다.

    return min_distance_list


if __name__ == "__main__":
    # node_counts, edge_counts = map(int, input().split())
    # starting_point = int(input())
    # adjacency_list = [[] for _ in range(node_counts + 1)]
    # for _ in range(edge_counts):
    #     source, destination, cost = map(int, input().split())
    #     adjacency_list[source].append((destination, cost))

    start_node = 1
    adjacency_list = [
        [],
        [(2, 2), (3, 5), (4, 1)],
        [(3, 3), (4, 2)],
        [(2, 3), (6, 5)],
        [(3, 3), (5, 1)],
        [(3, 1), (6, 2)],
        []
    ]

    result = dijkstra_heap(adjacency_list=adjacency_list, start_node=start_node)

    for i in range(1, len(result)):
        print(result[i])