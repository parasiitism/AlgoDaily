"""
    prefix sum + hashtable
    - similar to the problem "subarry zero sum", now we do "subarry zero prefiex XOR", another classic question
    - the reason why XOR work:
    
    e.g. [4,3,1,2,4]
    
    4 = 100
    3 = 011
    1 = 001
    2 = 010
    4 = 100
        ^^^
    
    All the bits will be XOR-ed out after operations

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ht = {0: 1}
        res = 0
        pfs_xor = 0
        for x in nums:
            pfs_xor ^= x
            if pfs_xor in ht:
                res += ht[pfs_xor]
            else:
                ht[pfs_xor] = 0
            ht[pfs_xor] += 1
        return res
