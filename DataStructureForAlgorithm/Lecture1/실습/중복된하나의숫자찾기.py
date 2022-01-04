import math

def findDuplicate(nums):
    nums.sort()
    former = math.inf
    
    for a in nums:
        if a == former:
            return a
        else:
            former = a

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()