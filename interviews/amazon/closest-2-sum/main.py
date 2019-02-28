"""
    Given 2 arrays of n flights, [id, travel distance], forwardRouteList and returnRouteList
    find the pair(s) in nums such that the sum is closest(<=) to a given number, target

    e.g.1
    maxTravelDist = 20
    forwardRouteList = [[1, 8], [2, 7], [3, 14]]
    returnRouteList = [[1, 5], [2, 10], [3, 14]]
    return [[3, 1]]

    e.g.2
    maxTravelDist = 20
    forwardRouteList = [[1, 8], [2, 15], [3, 9]]
    returnRouteList = [[1, 8], [2, 11], [3, 12]]
    return [[1, 3], [3, 2]]
  
    Questions to ask:
    - will there be 2 or more pairs have the same sum? yes
    - the result must contains 2 items? what if [1,2,10] and 10, should i just return 10?
    - will there be no result?
    - all numbers in nums > 0?
    - maxCap > 0?
"""


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    """
        1st approach
        - naive brute force
        Time    O(n^2)
        Space   O(n)
    """
    if maxTravelDist <= 0 or len(forwardRouteList) != len(returnRouteList):
        return []
    total = 0
    targetI = None
    targetJ = None
    res = []
    for forw in forwardRouteList:
        for retur in returnRouteList:
            curTotal = forw[1]+retur[1]
            if curTotal >= total and curTotal <= maxTravelDist:
                targetI = forw[0]
                targetJ = retur[0]
                total = curTotal
                if curTotal == maxTravelDist:
                    res.append([targetI, targetJ])
    if len(res) == 0:
        if targetI == None or targetJ == None:
            return []
        return [[targetI, targetJ]]
    return res


print(optimalUtilization(20,
                         [[1, 8], [2, 7], [3, 14]],
                         [[1, 5], [2, 10], [3, 14]]
                         ))

print(optimalUtilization(20,
                         [[1, 8], [2, 15], [3, 9]],
                         [[1, 8], [2, 11], [3, 12]]
                         ))


def optimalUtilization1(maxTravelDist, forwardRouteList, returnRouteList):
    """
        2nd approach
        - for each forward route, binary search through the return routes
        Time    O(nlogn)
        Space   O(n)
    """
    if maxTravelDist <= 0 or len(forwardRouteList) != len(returnRouteList):
        return []
    returnRouteList = sorted(returnRouteList)
    total = 0
    targetI = None
    targetJ = None
    res = []
    for forw in forwardRouteList:
        targetIdx = bsearch(returnRouteList, maxTravelDist-forw[1])
        if targetIdx < 0:
            continue
        target = returnRouteList[targetIdx]
        curTotal = forw[1]+target[1]
        if curTotal >= total and curTotal <= maxTravelDist:
            targetI = forw[0]
            targetJ = target[0]
            total = curTotal
            if curTotal == maxTravelDist:
                res.append([targetI, targetJ])
    if len(res) == 0:
        if targetI == None or targetJ == None:
            return []
        return [[targetI, targetJ]]
    return res


def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)/2
        if nums[mid][1] < target:
            left = mid + 1
        elif nums[mid][1] > target:
            right = mid - 1
        else:
            return mid
    return right


print(optimalUtilization1(20,
                          [[1, 8], [2, 7], [3, 14]],
                          [[1, 5], [2, 10], [3, 14]]
                          ))

print(optimalUtilization1(20,
                          [[1, 8], [2, 15], [3, 9]],
                          [[1, 8], [2, 11], [3, 12]]
                          ))
