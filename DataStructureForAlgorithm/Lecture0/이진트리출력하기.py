from collections import deque
import math

#====이 문제를 풀기 위해 필요한 클래스와 함수들입니다. 따로 수정 할 필요는 없습니다.
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def listToCompleteBinaryTree(lst):
    def helper(index):
        if index >= len(lst):
            return None
        node = Node(lst[index])
        node.left = helper(index * 2 + 1)
        node.right = helper(index * 2 + 2)
        return node
    return helper(0)
#=================================================================================
def printTree(node):
    all_lines = []
    
    q = deque()
    
    q.append(node)
    
    tempLine = []
    i = 0
    
    while q:
        n = q.popleft()
    
        tempLine.append(n.val)
        
        if len(tempLine) == 2**i: # 2의 거듭제곱개가 됐을 때
            all_lines.append(tempLine) # all_lines에 붙이구
            tempLine = [] # 빈 tempLine을 만든다
            i += 1
        
        if n.left : q.append(n.left)
        if n.right : q.append(n.right)
        
        
    
    return all_lines


def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    