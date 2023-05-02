/*
    An initial public ottering (IPO) reters to the process of ottering shares ot a private corporation to the public in a new stock issuance. Public share issuance allows a companv to raise capital trom public investors. IPO process
    can go through a tvpical auction, and an IPO price is not set betore the auction. Potential buvers are able to bid tor the shares thev want and the price thev are willing to pav. The bidders who were willing to pav the highest
    price are then allocated the shares available
    
    Before the auction ends, potentlal buyers can submit bids containing: user ld, number or shares, bidding price, timestamp.
    unce all the bias are submitted, the allotted placement Is assigned to the bidders trom the nighest bias down, until all ot the allotted snares are assigned. Ine auction assigns shares in multiple rounds until all snares are
    allocated or no more bids. In each round, It finds the bids with highest prices, assigns the shares, and removes the assigned bids:
    
    1. IT the bid (with the highest price) has only 1 bidders, the bidder gets shares he/she bids for (or get whatever left if the unallocated shares are less than the bid sha
    2. If the bids (with the highest orice) have multiole bidders, the bidders are assigned shares as follows:
    shares are distributed round robin stle to bidders in the same price group, with the bidders sorted by timestamp. Once a bidder gets the number ot shares they bid tor, they will be removed trom the above Iterative process and the
    process which then continues until all bidders are removed or the shares get exhausted, whichever comes first.
    
    Find out all bidders (user IDS) with no share allocation.
    
    Function Description
    Complete the function getResults in the editor below. The function must return a list of integers, each an ld for those bidders who receive no shares, sorted ascending.

    - The first line contains an integer, n, denoting the size or the array olas.
    - The next line contains an integer, 4, denoting the number of attributes for each bid.
    - Each line i of the n subsequent lines (where 0 si < n) contains four integers, u, sc, bp and ts denoting the user Id, number of shares, bid price and the timestamp of the j'bid.
    - The next line contains an integer, totalShares, denoting the total number of shares offered in the IPO

    e.g.
    
    Input
    3
    4
    1 2 5 6
    2 1 4 2
    3 5 4 6
    3

    Output: 3
*/
const f = (bids, k) => {
    let sortedBids = []
    const price_count = {}
    for (let i = 0; i < bids.length; i++) {
        const [userId, noOfShares, price, timestamp] = bids[i]
        sortedBids.push([price, timestamp, noOfShares, userId])
        
        if (price in price_count === false) {
            price_count[price] = 0
        }
        price_count[price] += 1
    }

    sortedBids.sort((a ,b) => {
        if (a[0] !== b[0]) {
            return b[0] - a[0]
        }
        return a[1] - b[1]
    })

    // reduce from highest price to lowest price (if every price is unique)
    while (k > 0 && sortedBids.length > 0) {
        const highestBid = sortedBids[0]
        const price = highestBid[0]
        if (price_count[price] > 1) {
            break
        }
        
        if (k >= highestBid[2]) {
            k -= highestBid[2]
            sortedBids.shift()
        } else {
            k = 0
            sortedBids.shift()
            // no more IPO stocks to allocate, the users from the remaining bids is the result
            if (sortedBids.length > 0) {
                const uniqueUsers = new Set(sortedBids.map(x => x[3]))
                return Array.from(uniqueUsers)
            }
        }
    }

    // round robin if k > 0
    while (k > 0 && sortedBids.length > 0) {
        let i = 0
        let total_asks = sortedBids[i][2]
        while (i+1 < sortedBids.length && sortedBids[i][0] === sortedBids[i+1][0]) {
            total_asks += sortedBids[i+1][2]
            i += 1
        }
        // console.log(i, total_asks, sortedBids)
        if (k >= total_asks) {
            k -= total_asks
            sortedBids = sortedBids.slice(i+1)
        } else if (k >= i+1) {
            // we don't have enough stocks, but everyone at least have 1 IPO stock
            return []
        } else {
            // we even don't have enough stocks for 1 round of rotation
            sortedBids = sortedBids.slice(i)
            k = 0
        }
    }
    const uniqueUsers = new Set(sortedBids.map(x => x[3]))
    return Array.from(uniqueUsers)
}

a = [
    [1,2,5,0],
    [2,1,4,2],
    [3,5,4,6]
]
console.log(f(a, 3)) // [3]

a = [
    [1,2,5,0],
    [2,1,4,2],
    [3,5,4,6],
    [4,5,4,7],
    [5,5,4,8],
]
console.log(f(a, 18)) // []

a = [
    [1,2,5,0],
    [2,1,4,2],
    [3,5,4,6],
    [4,5,4,7],
    [5,5,4,8],
]
console.log(f(a, 17)) // [] everyone get some stocks, just that userID 5 doesn't have the amount he ASKs

a = [
    [1,2,5,0],
    [2,1,4,2],
    [3,5,4,6],
    [4,5,4,7],
    [5,5,4,8],
    [6,5,3,9]
]
console.log(f(a, 18)) // [6]

a = [
    [1,2,5,0],
    [2,1,4,2],
    [3,5,4,6],
    [4,5,4,7],
    [5,5,4,8],
    [6,5,3,9],
    [7,5,3,10],
    [8,5,2,11],
]
console.log(f(a, 18)) // [6,7,8]