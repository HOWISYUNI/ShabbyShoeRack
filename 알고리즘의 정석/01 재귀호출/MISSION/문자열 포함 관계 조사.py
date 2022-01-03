import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''

    # base condition
    if len(A) == 0:
        return "Yes"

    # recursive
    target = A[0]

    if target in B:
        return strContain(A[1:], B)
    else:
        return "No"


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    A = list(set(input()))
    B = list(set(input()))

    print(strContain(A, B))

if __name__ == "__main__":
    main()
