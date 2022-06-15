class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8:
            return False
        seen = {'special': 0, 'upper': 0, 'lower': 0, 'digit': 0}
        for i in range(n):
            c = password[i]
            if i > 0 and c == password[i-1]:
                return False
            if c in '!@#$%^&*()-+':
                seen['special'] += 1
            elif c.isupper():
                seen['upper'] += 1
            elif c.islower():
                seen['lower'] += 1
            elif c.isdigit():
                seen['digit'] += 1
        for key in seen:
            if seen[key] == 0:
                return False
        return True
