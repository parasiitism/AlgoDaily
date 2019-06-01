import heapq

"""
    1st approach: pq + hashtable 
    - similar to lc1054

    1. count the occurence of characters
    2. put the characters into the maxheap
    3. pop the maxheap and construct the result
    4. if the pop item == res[-1], we save this to the buffer, and append the next item
    5. after we append the next item, we put the buffer back to the heap
    6. loop until there is no item in the heap
    7. if there is an item in the buffer, it means that we cannot constuct the reuslt
    8. else we just return the result

    Time    O(nlogn) becos heap for O(logn)
    Space   O(n)
    28 ms, faster than 41.51%
"""


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # counter
        pq = []
        ht = {}
        for c in S:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for key in ht:
            heapq.heappush(pq, (-ht[key], key))
        # construct result
        res = ""
        buffer = None
        while len(pq) > 0:
            ocur, pop = heapq.heappop(pq)
            if len(res) == 0:
                res += pop
                # we put back the character if occurence > 1
                if ocur < -1:
                    heapq.heappush(pq, (ocur+1, pop))
            else:
                if res[-1] != pop:
                    res += pop
                    # we put back the character if occurence > 1
                    if ocur < -1:
                        heapq.heappush(pq, (ocur+1, pop))
                    # remember to put the buffer back to the result
                    if buffer != None:
                        heapq.heappush(pq, buffer)
                        buffer = None
                else:
                    buffer = (ocur, pop)
        # if there is something in the buffer, we fail to reorganise the string
        if buffer != None:
            return ""
        return res


print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))

print(Solution().reorganizeString("aabc"))
print(Solution().reorganizeString("aaabc"))

print(Solution().reorganizeString("aabcc"))
print(Solution().reorganizeString("aaaabc"))

a = "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"
print(Solution().reorganizeString(a))

a = "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
print(Solution().reorganizeString(a))

print("-----")

"""
    1st approach: pq + hashtable but pop 2 at a time so dont need to use a buffer
    - similar to lc1054

    1. count the occurence of characters
    2. put the characters into the maxheap
    3. pop the maxheap and construct the result
    4. if the pop item == res[-1], we save this to the buffer, and append the next item
    5. after we append the next item, we put the buffer back to the heap
    6. loop until there is no item in the heap
    7. if there is an item in the buffer, it means that we cannot constuct the reuslt
    8. else we just return the result

    Time    O(nlogn) becos heap for O(logn)
    Space   O(n)
    16 ms, faster than 98.18%
"""


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # counter
        pq = []
        ht = {}
        for c in S:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for key in ht:
            heapq.heappush(pq, (-ht[key], key))
        # construct result by putting 2 items at a time
        res = ""
        while len(pq) > 0:
            ocurA, popA = heapq.heappop(pq)
            res += popA
            if len(pq) == 0:
                if abs(ocurA) > 1:
                    return ""
                break
            ocurB, popB = heapq.heappop(pq)
            res += popB
            # we put back the character if occurence > 1
            if abs(ocurA) > 1:
                heapq.heappush(pq, (ocurA+1, popA))
            if abs(ocurB) > 1:
                heapq.heappush(pq, (ocurB+1, popB))
        return res


print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))

print(Solution().reorganizeString("aabc"))
print(Solution().reorganizeString("aaabc"))

print(Solution().reorganizeString("aabcc"))
print(Solution().reorganizeString("aaaabc"))

a = "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"
print(Solution().reorganizeString(a))

a = "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
print(Solution().reorganizeString(a))
