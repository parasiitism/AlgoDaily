"""
    questions to ask:
    - will there be charactors other than a-zA-Z in dictionary? yes
    - will there be duplicate words in the initial dictionary? yes
    - will there be already some duplicate abbreviated words in the initial dictionary?
    - be careful of the corner cases:
        - ["dog"], isUnique("dig") ? False
        - ["dog", "dog"], isUnique("dog") ? True
        - "dog", "dig"], isUnique("dog") ? False
"""


"""
    1st approach: hashtable
    - at init, for a new abbreviated word, save self.ht[s] = word as key:value
    - at init, for the duplicate abbreviated words, save None as value of its key, self.ht[s] = None
    - in isUnique, check if the abbreviated word exists in the hashtable

    Time    O(n)
    Space   O(n)
    108 ms, faster than 90.87% 
"""


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.ht = {}
        for word in dictionary:
            s = self.i18n(word)
            if s in self.ht:
                if self.ht[s] != word:
                    self.ht[s] = None
            else:
                self.ht[s] = word

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s = self.i18n(word)
        if s in self.ht:
            if self.ht[s] != word:
                return False
        return True

    def i18n(self, s):
        if len(s) < 3:
            return s
        head = s[0]
        tail = s[-1]
        cnt = len(s)-2
        return head + str(cnt) + tail


# Your ValidWordAbbr object will be instantiated and called as such:
d = ["deer", "door", "cake", "card"]
obj = ValidWordAbbr(d)
print(obj.isUnique("dear"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
print(obj.isUnique("door"))

print("---")

d = ["deer", "cake", "card"]
obj = ValidWordAbbr(d)
print(obj.isUnique("deer"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
print(obj.isUnique("door"))
