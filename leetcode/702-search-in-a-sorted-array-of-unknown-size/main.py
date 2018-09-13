class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        head = reader.get(0)
        if head == target:
            return 0
        max_diff = target - head + 1
        tail = reader.get(max_diff)
        
        # searh for the right boundary, as long as the item, reader.get(right), is >= target
        right = max_diff
        while target > tail or tail == 2147483647:
            if tail == 2147483647:
                right = int(right/2)
                tail = reader.get(right)
            else:
                right = int(round(right*1.6))
                tail = reader.get(right)
                test = reader.get(right+1)
                if test == 2147483647:
                    break
                
        print("right", right, "tail", tail)
        # search for the target
        left = 0
        while left <= right:
            mean = int((left + right)/2)
            x = reader.get(mean)
            if target > x:
                left = mean + 1
            elif target < x:
                right = mean - 1
            else:
                return mean
        return -1