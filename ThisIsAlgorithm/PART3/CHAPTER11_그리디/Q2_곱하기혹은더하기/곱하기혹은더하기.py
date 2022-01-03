
def solution(number):
    result = 0

    for idx, singleNumber in enumerate(map(int, number)):
        if idx == 0:
            result = singleNumber
            continue

        result = max(result + singleNumber, result * singleNumber)

    return result

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode='r') as f:
        lines = f.readlines()
        number = lines[0].strip()
        print(solution(number))