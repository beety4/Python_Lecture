def minus(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result -= nums[i]

    return result

    # 6, 3 ,2 ,1

    #return nums[0] - nums[1] if len(nums) > 2 else None

    # if len(nums) > 2:
    #     return nums[0] - nums[1]
    # else:
    #     return None