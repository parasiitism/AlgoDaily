def firstMissingPositive(nums):
    """
    sort
    Time    O(nlogn+n)
    Space   O(n)
    """
    if len(nums) == 0:
        return 1

    # if duplicate
    nums = list(set(nums))

    nums = sorted(nums)

    # dont use heap becos it just gurantee the first item is smallest
    # but the rest of the items are not necessarily sorted
    # heapq.heapify(nums)

    # if negative
    for o in nums:
        if o < 1:
            nums = nums[1:]

    j = 0
    for i in range(1, len(nums)+1):
        if nums[j] != i:
            return i
        j += 1
    return j+1

def firstMissingPositive1(nums):
    """
    hashtable
    Time    O(2n)
    Space   O(n+1)
    
    """
    seen = [False]*(len(nums)+1)
    for num in nums:
        # to avoid negative and out of bound
        if num > 0 and num < len(seen):
            seen[num] = True
    for i in range(1, len(seen)):
        if seen[i] == False:
            return i
    # it means all numbers are continuous, so just return the number of seen
    return len(seen)