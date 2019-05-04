"""
    1st approach: hashtable + string splitting

    Time    O(nk) k: average number of characters of strings
    Space   O(n)
    112 ms, faster than 84.56%
"""


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        # split by space to get directory and files+content
        for path in paths:
            arr = path.split()
            directory = arr[0]
            fileContents = arr[1:]
            # split by ( to get file and content
            for fc in fileContents:
                left, right = fc.split('(')
                fpath = directory + '/' + left
                content = right
                # put the full path to its cooresponding key in the hashtable
                if content not in m:
                    m[content] = [fpath]
                else:
                    m[content].append(fpath)
        res = []
        # only put the paths where the content appear more than once
        for key in m:
            if len(m[key]) >= 2:
                res.append(m[key])
        return res
