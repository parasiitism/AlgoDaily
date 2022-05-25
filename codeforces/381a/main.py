def f():
    n = int(input())
    nums = [int(x) for x in input().split()]
    left, right = 0, n-1
    sereja, dima = 0, 0
    i = 0
    while left <= right:
        if nums[left] <= nums[right]:
            if i % 2 == 0:
                sereja += nums[right]
            else:
                dima += nums[right]
            right -= 1
        else:
            if i % 2 == 0:
                sereja += nums[left]
            else:
                dima += nums[left]
            left += 1
        i += 1
    print(str(sereja) + " " + str(dima))


f()
