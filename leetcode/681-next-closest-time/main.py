"""
    2nd approach:
    - there are only 1440 slots, so generate them with timeslot string representation
    - translate the target time to slot index
    - interate through the slots from that index, and if the current timeslot is a combination of target, return it as the result
    - if no time found previously, we iterate the slots again from 0 to idx. And again if find a combination, return it

    Time    O(1440 + 1440*16) -> O(1)
    Space   O(n)
    64 ms, faster than 7.69%
"""


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        timeSlots = self.createSlots()
        # translate time to index
        idx = self.translateTimeToIndex(time)
        # look for the result from idx+1 to 1439
        for i in range(idx+1, len(timeSlots)):
            timeSlot = timeSlots[i]
            allFound = True
            for j in range(len(timeSlot)):
                if j != 2:
                    if timeSlot[j] not in time:
                        allFound = False
                        break
            if allFound:
                return timeSlot
        # look for the result from 0 to idx+1
        for i in range(idx+1):
            timeSlot = timeSlots[i]
            allFound = True
            for j in range(len(timeSlot)):
                if j != 2:
                    if timeSlot[j] not in time:
                        allFound = False
                        break
            if allFound:
                return timeSlot

    def createSlots(self):
        """
        create an array of timeslot strings
        [
            "00:00",
            "00:01",
            ...
            "23:59"
        ]
        """
        slots = []
        hour = 0
        minute = 0
        for i in range(1440):
            hourKey = str(hour)
            if hour < 10:
                hourKey = "0" + str(hour)
            minuteKey = str(minute)
            if minute < 10:
                minuteKey = "0" + str(minute)
            slots.append(hourKey+":"+minuteKey)
            minute += 1
            if minute > 59:
                hour += 1
                minute = 0
        return slots

    def translateTimeToIndex(self, time):
        """
        translate input time to index from 0 to 14439
        """
        a = time[:2]
        b = time[3:]
        hour = int(a)
        minute = int(b)
        return hour*60+minute


"""
19:39
22:22
15:11
13:10
21:01
00:00
00:10
00:00
08:00
09:00
11:11
11:21
"""

print(Solution().nextClosestTime("19:34"))
print(Solution().nextClosestTime("23:59"))
print(Solution().nextClosestTime("13:59"))
print(Solution().nextClosestTime("13:05"))
print(Solution().nextClosestTime("21:00"))
print(Solution().nextClosestTime("00:00"))
print(Solution().nextClosestTime("00:01"))
print(Solution().nextClosestTime("07:07"))
print(Solution().nextClosestTime("07:08"))
print(Solution().nextClosestTime("05:59"))
print(Solution().nextClosestTime("11:11"))
print(Solution().nextClosestTime("11:12"))
