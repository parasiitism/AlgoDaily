"""
    1st: simple but tedius approach
    - the hardest part is to find the median
    - my way is to find the
        - mid for odd number of elements
        - midLeft, midRight for even number of elements
    - calculate the median separately for odd and even

    Time    O(n)
    Space   O(1)
    32 ms, faster than 62.05%
"""


class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        first, last = -1, -1
        total, cnt, maxCount, mode = 0, 0, 0, -1
        for i in range(len(count)):
            # min
            if count[i] > 0 and first == -1:
                first = i
            # max
            if count[i] > 0:
                last = i
            # average
            total += count[i] * i
            cnt += count[i]
            # mode
            if count[i] > maxCount:
                maxCount = count[i]
                mode = i

        mid, mid1, mid2 = None, None, None
        if cnt % 2 == 0:
            mid1, mid2 = cnt//2, cnt//2 + 1
        else:
            mid = cnt//2

        median = None
        median1 = None
        median2 = None
        currentCount = 0
        for i in range(len(count)):
            currentCount += count[i]
            if mid != None:
                if currentCount >= mid:
                    median = i
                    break
            else:
                if currentCount >= mid1 and median1 == None and currentCount >= mid2 and median2 == None:
                    median = i
                    break
                elif currentCount >= mid2 and median2 == None:
                    median2 = i
                elif currentCount >= mid1 and median1 == None:
                    median1 = i

            if median1 != None and median2 != None:
                median = (median1 + median2)/2.0
                break

        return [first, last, total*1.0/cnt, median, mode]
