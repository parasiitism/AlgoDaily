/*
    1st:
    - primative types are not object, but we can transform them into Object for comparison
    - in JS, all classes are function
    https://www.digitalocean.com/community/tutorials/understanding-classes-in-javascript
*/
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj === null || obj === undefined || typeof classFunction !== 'function')
        return false;
    return Object(obj) instanceof classFunction;
};
/*
    2nd: null == undefined evaluates to true
*/
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj == null || typeof classFunction !== 'function')
        return false;
    return Object(obj) instanceof classFunction;
};