def solution(frontiers_counts, frighten_levels):
    result_set = []
    is_first = True

    for level in frighten_levels:
        if is_first:
            filling_list = []
            filling_list.append(level)
            is_first = False
            continue

        if filling_list and max(filling_list) > len(filling_list):
            filling_list.append(level)

            if max(filling_list) == len(filling_list):
                result_set.append(filling_list)
                is_first = True

    return result_set

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()
        frontiers_counts = map(int, lines[0].strip())
        frighten_levels = list(map(int, lines[1].strip().split()))

    result = solution(frontiers_counts, frighten_levels)
    print(len(result))