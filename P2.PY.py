def positive_sum(nums):
    sum = 0
    for num in nums:
        if num > 0:
            sum = sum + num
    return sum

nums = [-1,2,14,0,0,1]
print positive_sum(nums)
