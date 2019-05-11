"""
    I dont think it is a good question
    - bad leading zeros description
    - negative sign is present while it said "You may assume there is no extra space or special characters in the input string"

    Time    O(n) n: length of the string
    Space   O(1)
    16 ms, faster than 99.44%
"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        v4Items = IP.split('.')
        v6Items = IP.split(':')

        if len(v4Items) == 4 and len(v6Items) == 1 and self.checkv4(v4Items) == True:
            return "IPv4"

        if len(v6Items) == 8 and len(v4Items) == 1 and self.checkv6(v6Items) == True:
            return "IPv6"

        return "Neither"

    def checkv4(self, items):
        try:
            for item in items:
                x = int(item)
                if (x < 0
                        or 0 <= x <= 9 and len(item) != 1)\
                        or (10 <= x <= 99 and len(item) != 2)\
                        or (100 <= x <= 255 and len(item) != 3)\
                        or x > 255:
                    return False
            return True
        except:
            return False

    def checkv6(self, items):
        try:
            for item in items:
                x = int(item, 16)
                if x < 0 or x > 65535 or len(item) == 0 or len(item) > 4 or item[0] == '-':
                    return False
            return True
        except:
            return False


print(Solution().validIPAddress("172.16.254.1"))
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(Solution().validIPAddress("256.256.256.256"))

print(Solution().validIPAddress("2001:0db8:85a3:0000:0:8A2E:0070:7334"))
print(Solution().validIPAddress("2001:0db8:85a3:0:0000:8A2E:000a:7334"))
print(Solution().validIPAddress("02001:0db8:85a3:0:0:8A2E:0370.7334"))

print(Solution().validIPAddress("f001:db8:85a3:0:0:8A2E:0370:7334"))
# WTF
print(Solution().validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334"))
print(Solution().validIPAddress("15.16.-255.1"))
