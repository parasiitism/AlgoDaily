"""
    1st: stack + math
    
    Time    O(N)
    Space   O(N)
"""


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        res = n * [-1]
        for i in range(n-1, -1, -1):
            d, v = cars[i]
            while len(stack) > 0:
                j = stack[-1]
                # if the previous car runs faster, it is impossible for the current car to catch-up
                if cars[j][1] >= v:
                    stack.pop()
                    continue
                # if the collision time of current time is longer than the previous car collides with the others,
                # the collision between the current car and the previous car is not going to happen
                T = self.getTimeToCollide(cars[i], cars[j])
                if T >= res[j] and res[j] > 0:
                    stack.pop()
                else:
                    break

            # calculate the collision time
            if len(stack) > 0:
                j = stack[-1]
                res[i] = self.getTimeToCollide(cars[i], cars[j])

            # put the index in the stack
            stack.append(i)

        return res

    def getTimeToCollide(self, car1, car2):
        d1, v1 = car1
        d2, v2 = car2
        return (d1 - d2) / float(v2 - v1)  # t = dx / dv
