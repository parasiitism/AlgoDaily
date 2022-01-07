"""
    1st: sort
    - amass the planet asap, then collide with the big ones to see if it will be destroyed

    Time    O(NlogN)
    Space   O(1)
    1263 ms, faster than 78.95%
"""


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False
        return True
