if __name__ == '__main__':
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A는 내림차순, B는 오름차순으로 정렬
    A.sort()
    B.sort(reverse=True)

    # K번 바꿔치기
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]

    print(sum(A))