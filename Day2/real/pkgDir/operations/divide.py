def divide(nums):
    if nums[1] != 0:
        return nums[0] / nums[1]
    else:
        return None
    #
    # try:
    #     return nums[0] / nums[1]
    # except ZeroDivisionError:
    #     return None