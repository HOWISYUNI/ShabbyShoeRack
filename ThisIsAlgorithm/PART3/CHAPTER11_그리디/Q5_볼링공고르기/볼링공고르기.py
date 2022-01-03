def solution(ball_counts, ball_weights):

    count = 0

    for idx, standardWeight in enumerate(ball_weights):
        for counterpart in ball_weights[idx + 1:]:
            if standardWeight != counterpart:
                count += 1

    return count

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc2.txt'), mode='r') as f:
        lines = f.readlines()
        ball_counts, weight_limitation = map(int, lines[0].strip().split())
        ball_weights = list(map(int, lines[1].strip().split()))

        print(solution(ball_counts, ball_weights))
