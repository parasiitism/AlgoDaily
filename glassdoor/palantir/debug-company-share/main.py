"""
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
"""


def calculate_shares_per_person(company_shares, entity_shares):

    cache = {}  # { entity: shares }
    res = {}    # { person: shares }

    def dfs(entity, shares):
        cache[entity] = shares

        if entity not in entity_shares:
            res[entity] = shares
            return

        children = entity_shares[entity]
        for key in children:
            _entity = key
            _shares = children[key]
            dfs(_entity, _shares * shares / 100)

    for entity in company_shares:
        shares = company_shares[entity]
        dfs(entity, shares)

    return res


company_shares = {
    'ABC': 12,
    'calvin': 9,
    'DEFGH': 50,
    'emily': 29
}
entity_shares = {
    'ABC': {
        'A': 50,
        'BC': 50
    },
    'BC': {
        'B': 10,
        'C': 90
    },
    'DEFGH': {
        'DE': 20,
        'FGH': 80
    },
    'DE': {
        'D': 70,
        'E': 30
    },
    'FGH': {
        'FG': 66,
        'H': 34
    },
    'FG': {
        'F': 50,
        'G': 50
    }
}
print(calculate_shares_per_person(company_shares, entity_shares))

"""
{
    'A': 6.0, 
    'B': 0.6, 
    'C': 5.4, 
    'calvin': 9, 
    'D': 7.0, 
    'E': 3.0, 
    'F': 13.2, 
    'G': 13.2, 
    'H': 13.6, 
    'emily': 29
}
"""
