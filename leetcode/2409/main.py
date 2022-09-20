from datetime import datetime
from collections import namedtuple

"""
    1st: math
    - annoying implementation

    Time    O(1)
    Space   O(1)
    67 ms, faster than 14.29%
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_m1, alice_d1 = arriveAlice.split("-")
        alice_m2, alice_d2 = leaveAlice.split("-")

        bob_m1, bob_d1 = arriveBob.split("-")
        bob_m2, bob_d2 = leaveBob.split("-")

        Range = namedtuple('Range', ['start', 'end'])

        alice = Range(start=datetime(2022, int(alice_m1), int(alice_d1)),
                      end=datetime(2022, int(alice_m2), int(alice_d2)))
        bob = Range(start=datetime(2022, int(bob_m1), int(bob_d1)),
                    end=datetime(2022, int(bob_m2), int(bob_d2)))

        s = max(alice.start, bob.start)
        e = min(alice.end, bob.end)

        return max(0, (e - s).days + 1)
