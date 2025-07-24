# rotate list

def jl(nums, k):
    k = k % len(nums) if nums else 0  # prevent IndexError
    m = []
    for i in range(k):
        m.append(nums.pop())
    r = m[::-1]
    z = r + nums
    return z



nums = [10, 20, 30, 40]
k = 2
print(jl(nums, k))