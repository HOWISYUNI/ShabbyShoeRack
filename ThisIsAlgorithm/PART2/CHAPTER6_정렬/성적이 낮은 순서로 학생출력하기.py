
if __name__ == '__main__':
    N = int(input().rstrip())
    grade_dict = {}

    for _ in range(N):
        name, score = input().split()
        grade_dict[name] = score

    answer = sorted(grade_dict.items(), key= lambda item:item[1])

    for name, score in answer:
        print(name, end=' ')

