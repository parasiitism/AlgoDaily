# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import defaultdict

"""
    1st: BFS + hashtable
    - BFS to traverse all the urls
    - use a hashtable to avoid redundant calculation

    Time    O(n)
    Space   O(n)
    280 ms, faster than 5.88%
"""


class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        masterHostname, _ = self.getSplitUrl(startUrl)
        self.hs = set()
        q = [startUrl]
        while len(q) > 0:
            url = q.pop(0)
            hostname, _ = self.getSplitUrl(url)
            if hostname != masterHostname:
                continue
            if url in self.hs:
                continue
            self.hs.add(url)
            for child in htmlParser.getUrls(url):
                q.append(child)
        return self.hs

    def getSplitUrl(self, s):
        temp = s[7:]
        i = 0
        while i < len(temp):
            if temp[i] == '/':
                break
            i += 1
        hostname = 'http://' + temp[:i]
        path = temp[i:]
        return hostname, path
