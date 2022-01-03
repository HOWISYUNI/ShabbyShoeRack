def getPermutation(n, r) :
    '''
    n개의 알파벳 중에서 r개를 뽑아 나열한 결과를 리스트로 반환합니다.

    예를 들어, n = 4, r = 2 일 경우에는
    
    ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", dc"] 를 반환합니다.
    '''

    

    result = []

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]

    print('\n'.join(getPermutation(firstLine[0], firstLine[1])))

if __name__ == "__main__":
    main()
