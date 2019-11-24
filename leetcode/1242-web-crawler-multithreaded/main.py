from concurrent.futures import ThreadPoolExecutor

"""
    1st: BFS + ThreadPoolExecutor

    Time    O(N/10)?
    Space   O(N)
    260 ms, faster than 71.43%
"""


class Solution(object):

    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        hs = set()
        hs.add(startUrl)
        hostname = self.getHostname(startUrl)
        queue = [startUrl]
        while len(queue) > 0:
            queue2 = []
            with ThreadPoolExecutor(max_workers=10) as executor:
                l = list(executor.map(
                    lambda url: htmlParser.getUrls(url), queue)
                )
                for urls in l:
                    for newUrl in urls:
                        if newUrl in hs or self.getHostname(newUrl) != hostname:
                            continue
                        hs.add(newUrl)
                        queue2.append(newUrl)
            queue = queue2
        return hs

    def getHostname(self, s):
        temp = s[7:]
        i = 0
        while i < len(temp):
            if temp[i] == '/':
                break
            i += 1
        hostname = 'http://' + temp[:i]
        return hostname
