'''
어떤 수가 입력으로 들어오면 몇번의 연산을 통해 숫자를 1로 가장 빨리 만들 수 있을지 계산하는 함수를 작성해 봅시다.

할 수 있는 연산은 다음과 같으며 어느 연산을 먼저 수행하는지에 대한 순서는 없습니다.

3의 배수라면 3으로 나눕니다.

2의 배수라면 2로 나눕니다.

1을 뺍니다.

예를 들어 10이 입력되었다면, 10 -> 5 -> 4 -> 2 -> 1의 4번의 과정을 거쳐 1로 만들 수 있습니다.

하지만 10 -> 9 -> 3 -> 1의 방법으로 3번의 과정을 거쳐 더 빠르게 1로 만들 수 있습니다.

또한 이것이 가장 빠른 방법입니다.

이와 같이 숫자가 입력되면 가장 빠르게 1로 만드는 연산의 횟수를 출력하는 프로그램을 작성해 봅시다.
'''

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
