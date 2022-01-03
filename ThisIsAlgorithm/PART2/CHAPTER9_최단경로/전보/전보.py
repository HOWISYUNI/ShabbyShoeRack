import heapq

def dijkstra(adjacency_list, source, city_counts):
    min_distance_list = [float('inf') for _ in range(city_counts + 1)]
    min_distance_list[source] = 0

    hq = [(0, source)]
    heapq.heapify(hq)  # 기존 리스트를 힙큐로 사용할땐 명시적으로 heapify 해주는게 좋다.

    while hq:
        cost_to_junction, junction = heapq.heappop(hq)

        # cost_to_junction이 junction으로의 최소 거리가 아니라면 건너뛴다.
        if cost_to_junction > min_distance_list[junction]:
            continue

        # junction에 연결된 노드의 최단거리를 수정한다.
        # source --- (junction) -- destination  VS  source -- destination
        for destination, cost in adjacency_list[junction]:
            if min_distance_list[destination] > cost_to_junction + min_distance_list[junction]: # destination으로 가는데, junction을 통해 가는게 빠르다면
                min_distance_list[destination] = cost_to_junction + cost # 최단거리를 갱신한다.
                heapq.heappush(hq, (min_distance_list[destination], destination))  # (갱신된 거리, 목적지) 로 힙큐에 넣어준다.

    return min_distance_list

if __name__ == "__main__":

    # init
    with open('tc1.txt', mode='r') as f:
        lines = f.readlines()
        city_counts, edge_count, source = map(int, lines[0].strip().split())
        # dijkstra는 junction에 연결된 노드들의 최단거리를 갱신하므로, 인접 노드를 빠르게 파악하기 위해 인접 리스트를 만드는게 좋다.
        adjacency_list = [[] for _ in range(city_counts + 1)]

        # map
        for i in range(1, edge_count + 1):
            src, dest, cost = map(int, lines[i].strip().split())
            adjacency_list[src].append((dest, cost))

    min_distance_list = dijkstra(adjacency_list, source, city_counts)

    # min_distance_list에 inf가 있으므로 이를 0으로 바꿔준 후 max를 찾아야한다.
    min_distance_list = [0 if distance == float('inf') else distance for distance in min_distance_list]
    print(max(min_distance_list))


