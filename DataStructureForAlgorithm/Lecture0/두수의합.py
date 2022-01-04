# push 용 수정

def twoSum(nums, target):
    
    for start in range(len(nums)-1):
        for end in range(start, len(nums)):
            if nums[start]+nums[end] == target:
                return nums[start], nums[end]
                
    else:
        return -1

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12))

if __name__ == "__main__":
    main()
