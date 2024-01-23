while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0 and nums[1] == 0:
        break

    try:
        print(f"연산 결과 : {nums[0] / nums[1]}")
    except ZeroDivisionError:
        print("Number Error")
