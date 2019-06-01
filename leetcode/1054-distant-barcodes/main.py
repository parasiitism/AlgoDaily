import heapq

"""
    1st approach: heap + hashtable
    - similar to lc767

    1. count the occurence of characters
    2. put the characters into the maxheap
    3. pop the maxheap and construct the result
    4. if the pop item == res[-1], we save this to the buffer, and append the next item
    5. after we append the next item, we put the buffer back to the heap
    6. loop until there is no item in the heap
    7. if there is an item in the buffer, it means that we cannot constuct the reuslt
    8. else we just return the result

    Time    O(nlogn)
    Space   O(n)
    592 ms, faster than 25.00%
"""


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        pq = []
        ht = {}
        for c in barcodes:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for key in ht:
            heapq.heappush(pq, (-ht[key], key))
        # construct result
        res = []
        buffer = None
        while len(pq) > 0:
            ocur, pop = heapq.heappop(pq)
            if len(res) == 0:
                res.append(pop)
                # we put back the character if occurence > 1
                if abs(ocur) > 1:
                    heapq.heappush(pq, (ocur+1, pop))
            else:
                if res[-1] != pop:
                    res.append(pop)
                    # we put back the character if occurence > 1
                    if abs(ocur) > 1:
                        heapq.heappush(pq, (ocur+1, pop))
                    # remember to put the buffer back to the result
                    if buffer != None:
                        heapq.heappush(pq, buffer)
                        buffer = None
                else:
                    buffer = (ocur, pop)
        # if there is something in the buffer, we fail to reorganise the string
        if buffer != None:
            return []
        return res


print(Solution().rearrangeBarcodes([1, 3, 3, 3, 4, 5]))
print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2]))
print(Solution().rearrangeBarcodes([1, 1, 2, 2, 2]))
print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
print(Solution().rearrangeBarcodes([1, 2, 2, 3, 3, 3, 4, 5]))

print("-----")

"""
    2nd approach: heap + hashtable but pop 2 at a time so dont need to use a buffer
    - similar to lc767

    1. count the occurence of characters
    2. put the characters into the maxheap
    3. pop the maxheap and construct the result
    4. if the pop item == res[-1], we save this to the buffer, and append the next item
    5. after we append the next item, we put the buffer back to the heap
    6. loop until there is no item in the heap
    7. if there is an item in the buffer, it means that we cannot constuct the reuslt
    8. else we just return the result

    Time    O(nlogn)
    Space   O(n)
    552 ms, faster than 42.33%
"""


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        pq = []
        ht = {}
        for c in barcodes:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for key in ht:
            heapq.heappush(pq, (-ht[key], key))
        # construct result by putting 2 items at a time
        res = []
        while len(pq) > 0:
            ocurA, popA = heapq.heappop(pq)
            res.append(popA)
            if len(pq) == 0:
                break
            ocurB, popB = heapq.heappop(pq)
            res.append(popB)
            # we put back the character if occurence > 1
            if abs(ocurA) > 1:
                heapq.heappush(pq, (ocurA+1, popA))
            if abs(ocurB) > 1:
                heapq.heappush(pq, (ocurB+1, popB))
        return res


print(Solution().rearrangeBarcodes([1, 3, 3, 3, 4, 5]))
print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2]))
print(Solution().rearrangeBarcodes([1, 1, 2, 2, 2]))
print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
print(Solution().rearrangeBarcodes([1, 2, 2, 3, 3, 3, 4, 5]))

print("-----")
