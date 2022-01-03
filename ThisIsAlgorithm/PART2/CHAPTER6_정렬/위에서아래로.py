
if __name__ == '__main__':
    N = int(input().rstrip())
    num_list = [int(input().rstrip()) for _ in range(N)]

    num_list.sort(reverse=True)
    print(num_list)