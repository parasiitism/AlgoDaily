class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # count occurence
        setA, setB = set(), set()
        for num in nums1:
            setA.add(num)
        for num in nums2:
            setB.add(num)
        # declare hastables for iteration
        largerSet = setA
        smallerSet = setB
        if len(largerSet) < len(smallerSet):
            smallerSet, largerSet = largerSet, smallerSet
        # # find the duplicates
        res = []
        for key in largerSet:
            if key in smallerSet:
                res.append(key)
        return res
