/*
    Debug, 一个Java程序和一堆CSV 文件, 每个CSV是公司名称以及它的owner和每个owner所含有的share,
    owner可以是真的人. 也可以是其他公司, 程序是给定一个公司名称, 找出它背后的所有真人owner以及每个人所占的share比例
    
    这题一共有3个bug, 分散在不同公司的test case下 面试官会一个case一个case的问你, 一次找出一个bug就行, 仔细看code不难的
    
    Given
    - company the shares per entity (can either be a person or a company)
    - shares per entity
    Write a function to determine the shares a given owner(one person) has

    e.g.
    company_shares = {
        ABC: 12,
        calvin: 9,
        DEFGH: 50,
        emily: 29
    }
    entity_shares = {
        ABC: {
            A: 50,
            BC: 50
        },
        BC: {
            B: 10,
            C: 90
        },
        DEFGH: {
            DE: 20,
            FGH: 80 
        },
        DE: {
            D: 70,
            E: 30
        },
        FGH: {
            FG: 66,
            H: 34
        },
        FG: {
            F: 50,
            G: 50
        }
    }
*/

const list_share_per_owner = (company_shares, entity_shares) => {
    const cache = {}
    const res = {}
    const dfs = (entity, shares) => {
        cache[entity] = shares
        if (entity in entity_shares === false) {
            res[entity] = res[entity] ? res[entity] + shares : shares
        } else {
            const children = entity_shares[entity]
            for (let child in children) {
                const _shares = shares * children[child] / 100
                dfs(child, _shares)
            }
        }
    }

    for (let key in company_shares) {
        const shares = company_shares[key]
        dfs(key, shares)
    }

    return res
}
a = {
    ABC: 12,
    calvin: 9,
    DEFGH: 50,
    emily: 29
}
b = {
    ABC: {
        A: 50,
        BC: 50
    },
    BC: {
        B: 10,
        C: 90
    },
    DEFGH: {
        DE: 20,
        FGH: 80 
    },
    DE: {
        D: 70,
        E: 30
    },
    FGH: {
        FG: 66,
        H: 34
    },
    FG: {
        F: 50,
        G: 50
    }
}
console.log(list_share_per_owner(a, b))

/*
    the sum of the shares = 100 e.g. result = {
        A: 6,
        B: 0.6,
        C: 5.4,
        calvin: 9,
        D: 7,
        E: 3,
        F: 13.2,
        G: 13.2,
        H: 13.6,
        emily: 29
    }
*/