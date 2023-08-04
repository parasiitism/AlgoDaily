"""
    stack + hashtable
    - very similar to lc135, additionally:
        - sort the original posstions for displaying the result in the later stage
        - sort the robots by positions
        - just added some logic to decrement the health upon collision


    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        position_map = {}
        A = []
        for i in range(n):
            p = positions[i]
            h = healths[i]
            d = directions[i]
            A.append([p, h, d])
            position_map[p] = i
        A.sort(key=lambda x: x[0])
        # print(A)
        S = []
        for i in range(n):
            x = A[i]
            if x[2] == 'R':
                S.append(x)
            else:
                while len(S) > 0 and S[-1][2] == 'R' and S[-1][1] < x[1]:
                    S.pop()
                    x[1] -= 1
                if len(S) > 0 and S[-1][2] == 'R' and S[-1][1] == x[1]:
                    S.pop()
                elif len(S) == 0:
                    S.append(x)
                elif S[-1][2] == 'L':
                    S.append(x)
                elif S[-1][2] == 'R' and S[-1][1] > x[1]:
                    S[-1][1] -= 1
        # print(S)
        S.sort(key=lambda x: position_map[x[0]])
        return [h for _p, h, _d in S]
