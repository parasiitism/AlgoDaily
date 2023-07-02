type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (receiving) => {
            if (val === receiving) {
                return true
            }
            throw new Error('Not Equal')
        },
        notToBe: (receiving) => {
            if (val !== receiving) {
                return true
            }
            throw new Error('Equal')
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */