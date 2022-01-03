from collections import deque

def init(food_times):
    dumb = [0]
    dumb.extend(food_times)
    q = deque(enumerate(dumb))
    q.popleft()
    
    return q

def solution_greedy(food_times, k):
    answer = 0
    q = init(food_times)
    passedTime = 0
    
    while q:
        idx, foodTime = q.popleft()
        
        if passedTime == k:
            answer = idx
            return answer
        
        else:
            passedTime += 1
            foodTime -= 1
            if foodTime != 0:
                q.append((idx, foodTime))
                
    answer = -1
    
    return answer

# def solution_efficient(food_times, k):

if __name__ == "__main__":
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode='r') as f:
        lines = f.readlines()
        food_times = list(map(int, lines[0].split()))
        k = int(lines[1])

        print(solution_greedy(food_times, k))
        # print(solution_efficient(food_times, k))