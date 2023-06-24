/*
    Event Emitter
    ⭐️ very fundamental JS concept
*/
class EventEmitter {
    constructor() {
        this.ht = {};
    }

    subscribe(event, cb) {

        if (event in this.ht === false) {
            this.ht[event] = new Set();
        }
        this.ht[event].add(cb)

        return {
            unsubscribe: () => {
                this.ht[event].delete(cb);
				if (this.ht[event].size === 0) {
					delete this.ht[event];
				}
            }
        };
    }

    emit(event, args = []) {
        if (event in this.ht === false) {
			console.log(`no callback are subscribed yet ${event}`);
			return [];
		}
        const res = []
		this.ht[event].forEach((cb) => {
		    const temp = cb(...args);
            res.push(temp)
		});
        return res
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */