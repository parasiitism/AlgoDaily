"""
    1. split the string by space
    2. split the domain by .
    3. upsert the cnt to the list of top domains

    Time    O(n)
    Space   O(n)
    48 ms, faster than 99.74%
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnter = Counter()
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')
            cnt = int(cnt)
            parts = domain.split(".")
            subdomain = ''
            for j in range(len(parts)-1, -1, -1):
                p = parts[j]
                if len(subdomain) == 0:
                    subdomain = p
                else:
                    subdomain = p + '.' + subdomain
                cnter[subdomain] += cnt
        res = []
        for key in cnter:
            temp = str(cnter[key]) + " " + key
            res.append(temp)
        return res