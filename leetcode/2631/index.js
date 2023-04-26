/*
    hashtable
*/

/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const res = {}
    for (let x of this) {
      const key = fn(x)
      if (key in res === false) {
        res[key] = []
      }
      res[key].push(x)
    }
    return res
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */