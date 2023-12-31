/*
    https://leetcode.com/discuss/interview-question/413734/Bloomberg-or-Re-order-Array-Based-on-Dictionary

    Consider a vector of employees with a name and their title:
    [<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

    And a dictionary where the keys report to the values:
    {[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

    Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

    Sample output:
    [<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

    Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case.
*/
const reorderArray = (employees, order) => {

    const roleEmployeeMap = {}
    for (let [person, role] of employees) {
        if ((role in roleEmployeeMap) == false) {
            roleEmployeeMap[role] = []
        }
        roleEmployeeMap[role].push(person)
    }
    const graph = {}
    const indegrees = {}
    for (let [role, boss] of order) {
        if (role in graph === false) {
            graph[role] = []
            indegrees[role] = 0
        }
        if (boss in graph === false) {
            graph[boss] = []
            indegrees[boss] = 0
        }
        graph[boss].push(role)
        indegrees[role] += 1
    }

    const q = []
    for (let role in graph) {
        if (indegrees[role] == 0) {
            q.push(role)
        }
    }
    
    const res = []
    while (q.length > 0) {
        const role = q.shift()
        for (let person of roleEmployeeMap[role]) {
            res.push([person, role])
        }
        for (let boss of graph[role]) {
            indegrees[boss] -= 1
            if (indegrees[boss] == 0) {
                q.push(boss)
            }
        }
    }
    res.reverse()
    return res
}

let a, b

a = [['John', 'Manager'], ['Sally', 'CTO'], ['Sam', 'CEO'],
     ['Drax', 'Engineer'], ['Bob', 'CFO'], ['Daniel', 'Engineer']]
b = [['CTO', 'CEO'], ['Manager', 'CTO'], [
    'Engineer', 'Manager'], ['CFO', 'CEO']]
console.log(reorderArray(a, b))