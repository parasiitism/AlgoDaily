"""
    1st approach: sort + math, learned from others
    - for each car, if the time it takes to desitination (transit time) is less than the car in front of it, 
        it is going to catach up that car
    
    e.g. target = 12, position = [10,8,0,5,3,2], speed = [2,4,1,1,3,3]

    for car 10, (12-10)/2 = 1
    for car 8, (12-8)/4 = 1     <- it will catch up car10
    for car 5, (12-5)/1 = 7
    for car 3, (12-3)/3 = 3     <- it will catch up car5
    for car 2, (12-2)/3 = 3.33  <- it will catch up car5
    for car 1, (12-0)/1 = 12

    therefore there will be 3 fleets

    Time    O(nlogn)
    Space   O(n)
    168 ms, faster than 45.27%
"""


class Solution(object):
    def carFleet(self, target, position, speed):
        cars = []
        for i in range(len(position)):
            t = (target-position[i]) / float(speed[i])
            cars.append((position[i], t))
        cars.sort(key=lambda x: x[0])
        count = 0
        cur_max = 0
        for i in range(len(cars)-1, -1, -1):
            if cars[i][1] > cur_max:
                cur_max = cars[i][1]
                count += 1
        return count
