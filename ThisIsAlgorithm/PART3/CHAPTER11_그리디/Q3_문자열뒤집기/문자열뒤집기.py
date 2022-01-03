def solution(string):
    turn_count = 0
    before = string[0]

    for now in string[1:]:
        if now != before:
            turn_count += 1

        beore = now

    return turn_count // 2

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc.txt'), mode='r') as f:
        lines = f.readlines()
        string = lines[0].strip()
        print(solution(string))