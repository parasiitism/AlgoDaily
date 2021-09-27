"""
    1st: BFS

    there are 6 possibilties
    - fill jug1
    - fill jug2
    - empty jug1
    - empty jug2
    - pour jug1 to jug2 <- the remain in jug1 is important
    - pour jug2 to jug1 <- the remain in jug2 is important

    Time    O(jug1 * jug2) <- the # of jug1 * jug2
    Space   O(jug1 * jug2)
    4752 ms, faster than 8.55%
"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False
        seen = set()
        q = []
        q.append([0, 0])

        while len(q) > 0:
            jug1, jug2 = q.pop(0)
            if jug1 == targetCapacity or jug2 == targetCapacity or jug1+jug2 == targetCapacity:
                return True

            key = (jug1, jug2)
            if key in seen:
                continue
            seen.add(key)

            q.append([jug1Capacity, jug2])  # fill jug1
            q.append([jug1, jug2Capacity])  # fill jug2
            q.append([0, jug2])             # empty jug1
            q.append([jug1, 0])             # empty jug2
            # pour jug1 to jug2 <- the remain in jug1 is important
            q.append([
                max(jug1+jug2-jug2Capacity, 0),
                min(jug1+jug2, jug2Capacity)
            ])
            # pour jug2 to jug1 <- the remain in jug2 is important
            q.append([
                min(jug1+jug2, jug1Capacity),
                max(jug1+jug2-jug2Capacity, 0)
            ])

        return False
