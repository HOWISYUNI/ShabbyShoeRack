'''
스택에 1부터 N까지 차례대로 넣었다가 뽑아 리스트에 넣습니다. 이때 모두 넣은 뒤 모두 뽑는 것이 아닌 넣는 과정과 뽑는 과정을 섞어서 진행할 수도 있습니다. 이때 만들어진 수열을 스택 수열이라고 합시다.

1부터 N까지의 수로 이루어진 리스트가 주어집니다. 이때 이 리스트가 스택수열인지 검사하는 함수를 만들어 봅시다.

예를 들어 [2, 1, 4, 3]은 스택 수열입니다. 1넣기 -> 2넣기 -> 2뽑기 -> 1뽑기 -> 3넣기 -> 4넣기 -> 4뽑기 ->3뽑기 의 과정을 거치면 만들어 질 수 있기 때문입니다.

그러나 [3, 1, 2, 4]는 스택 수열이 아닙니다. 위에 나온 스택수열을 만드는 방법으로는 어떻게 해도 만들 수 없기 때문입니다.
'''

from collections import deque

def isStackSequence(nums):
    
    q = deque(nums)
    stack = []
    
    for i in range(1, len(nums)+1) :

        # PUSH
        if not stack or stack[-1] < q[0]: # 스택 top < 큐 head -> 아직 stack이 더 쌓여야한다
            stack.append(i) # push
                
        # POP. 큐 head == 스택 top 이라면 계속 확인
        while q and stack and q[0] == stack[-1]:
            q.popleft()
            stack.pop() # pop


    return False if stack else True

def main():
    print(isStackSequence([2, 1, 4, 3])) # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4])) # False가 리턴되어야 합니다
    print(isStackSequence([4, 3, 6, 8, 7, 5, 2, 1])) # True
    print(isStackSequence([1,3,4,2]))

    
if __name__ == "__main__":
    main()