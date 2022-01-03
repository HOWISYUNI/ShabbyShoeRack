from itertools import combinations

def solution(coin_counts, coins):
    makable = [False for _ in range(sum(coins) + 1)]

    for count in range(1, coin_counts + 1):
        for comb in combinations(coins, count):
            makable[sum(comb)] = True

    for idx, is_makable in enumerate(makable):
        if idx != 0 and is_makable == False:
            return idx

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()
        coin_counts = int(lines[0].strip())
        coins = list(map(int, lines[1].strip().split()))
        print(solution(coin_counts, coins))