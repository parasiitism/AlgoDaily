/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    const map = {}
    for (const s of cpdomains) {
        let [cnt, domain] = s.split(' ')
        let parts = domain.split('.')
        let subdomain = ''
        for (let j = parts.length-1; j >= 0; j--) {
            let p = parts[j]
            if (subdomain.length > 0) {
                subdomain = p + '.' + subdomain
            } else {
                subdomain = p
            }
            if (subdomain in map === false) {
                map[subdomain]  = 0
            }
            map[subdomain] += parseInt(cnt)
        }
    }
    const res = []
    for (const key in map) {
        const s = map[key] + " " + key
        res.push(s)
    }
    return res
};