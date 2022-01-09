# divide and conquer를 이용한 풀이

import math

def convertTo1(num):
    div2result, div3result, minusResult = math.inf, math.inf, math.inf
    
    # base condition
    if num == 1:
        return 0
    
    # conquer
    if num%2 == 0:
        div2result = convertTo1(num//2)
    if num%3 == 0:
        div3result = convertTo1(num//3)
    else:
        minusResult = convertTo1(num-1)
        
    return min(div2result+1, div3result+1, minusResult+1)

# 2022.1.9 튜터 추천 풀이 추가
# 1부터 1로 만드는 최소 값을 리스트에 계속 저장하면서 num에 도달
def convertTo1(num):

    d = [num for _ in range(num + 1)]
    
    d[1] = 0
    
    for i in range(2, num + 1):
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        d[i] = min(d[i], d[i - 1] + 1)
    return d[num]

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
