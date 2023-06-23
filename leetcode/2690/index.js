/*
    JS proxy
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy
    - https://blog.techbridge.cc/2018/05/27/js-proxy-reflect/
*/

/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    return new Proxy({}, {
        get(_target, prop, _receiver) {
            return () => prop;
        }
    })
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */