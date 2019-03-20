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
    if maxTravelDist <= 0 or len(forwardRouteList) == 0 or len(
            returnRouteList) == 0:
        return []
    returnRouteList = sorted(returnRouteList)
    res = []
    best = 0
    for forward in forwardRouteList:
        returnIdx = bsearch(returnRouteList, maxTravelDist - forward[1])
        if returnIdx < 0:
            continue
        backward = returnRouteList[returnIdx]
        dist = forward[1] + backward[1]
        if dist > best:
            # reset the intermediate result
            best = dist
            res = [[forward[0], backward[0]]]
        elif dist == best:
            res.append([forward[0], backward[0]])
    return res


def bsearch(routes, target):
    left = 0
    right = len(routes) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if routes[mid][1] < target:
            left = mid + 1
        elif routes[mid][1] > target:
            right = mid - 1
        else:
            return mid
    return right


print(
    optimalUtilization(20, [[1, 8], [2, 7], [3, 14]],
                       [[1, 5], [2, 10], [3, 14]]))

print(
    optimalUtilization(20, [[1, 8], [2, 15], [3, 9]],
                       [[1, 8], [2, 11], [3, 12]]))

# corner cases
print(
    optimalUtilization(-20, [[1, 8], [2, 7], [3, 14]],
                       [[1, 5], [2, 10], [3, 14]]))

print(optimalUtilization(20, [], [[1, 5], [2, 10], [3, 14]]))

print(optimalUtilization(20, [[1, 21], [2, 22], [3, 23]], [[1, 24], [2, 25], [3, 26]]))
