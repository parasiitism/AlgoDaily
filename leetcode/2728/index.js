/*
    Observation
    - the street is cicurlar, we don't know how many doors are there 
    - but if we open all doors
    - and then close all doors until we don't see any dooers opened, then we will know how many 
*/

/**
 * Definition for a street.
 * class Street {
 *     @param {number[]} doors
 *     constructor(doors);
 * 
 *     @return {void}
 *     openDoor();
 * 
 *     @return {void}
 *     closeDoor();
 * 
 *     @return {boolean}
 *     isDoorOpen();
 * 
 *     @return {void}
 *     moveRight();
 * 
 *     @return {void}
 *     moveLeft();
 * }
 */
/**
 * @param {Street} street
 * @param {number} k
 * @return {number}
 */
var houseCount = function(street, k) {
    for (let i=0; i<k; i++) {
        street.openDoor()
        street.moveRight()
    }
    let cnt = 0
    while (street.isDoorOpen()) {
        cnt += 1
        street.closeDoor()
        street.moveRight()
    }
    return cnt
};