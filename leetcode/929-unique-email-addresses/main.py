"""
    questions to ask:
    - will there be no @?
    - will there be more than one @?
    - will there be no charactors before @?
    - will there be no charactors after @?
"""


class Solution(object):
    """
    - use split, replace and set
    Time  O(n)
    Space O(n)
    60ms beats 58.88%
    """

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            name, domain = email.split("@")
            first = name.split("+")[0].replace(".", "")
            if len(first) > 0 and len(domain) > 0:
                em = first+"@"+domain
                result.add(em)
        return len(result)


print(Solution().numUniqueEmails(
    [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
        "abc@ca.com",
        "@",
        "aaa@",
        "@ddd",
    ]))
