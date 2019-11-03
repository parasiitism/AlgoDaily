class A0Paper():
    def canBuild(self, nums):
        total = 0
        for i in range(len(nums)):
            base = 0.5**i
            total += int(nums[i]) * base
            if total >= 1:
                return "Possible"
        return "Impossible"


s = A0Paper()

a = [0, 1, 2]
print(s.canBuild(a))
