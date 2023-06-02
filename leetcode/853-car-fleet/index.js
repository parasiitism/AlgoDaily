/*
    1st approach: sort + mono-increase stack, learned from others
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
*/
var carFleet = function(target, position, speed) {
    const n = position.length
    const cars = []
    for (let i = 0; i < n; i++) {
        const t = (target - position[i]) / speed[i]
        cars.push([t, position[i]])
    }
    cars.sort((a, b) => b[1] - a[1])
    const S = []
    for (let [t, _pos] of cars) {
        if (S.length == 0 || t > S[S.length-1]) {
            S.push(t)
        }
    }
    return S.length
};