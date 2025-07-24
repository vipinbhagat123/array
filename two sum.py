# two sum

def kl(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]
    return -1
                
nums = [2, 7, 11, 15]
target = 9
print(kl(nums, target))

