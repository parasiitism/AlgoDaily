"""
    1st: brute force with hashtable

    Time    O(S + xRI) x: the combinations of ingredients becoming recipes
    Space   O(S+R)
    1424 ms, faster than 6.25%
"""


from collections import *


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        suppliesSet = set(supplies)
        res = set()
        while True:
            cnt = 0
            for i in range(n):
                r = recipes[i]
                if r in res:
                    continue
                hasAll = True
                for ing in ingredients[i]:
                    if ing not in suppliesSet:
                        hasAll = False
                        break
                if hasAll:
                    res.add(r)
                    suppliesSet.add(r)
                    cnt += 1
            if cnt == 0:
                break
        return list(res)


"""
    2nd: topological ordering

    Time    O(V+E)
    Space   O(V)
    892 ms, faster than 18.75%
"""


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        indegrees = defaultdict(int)
        connections = defaultdict(list)
        for i in range(n):
            r = recipes[i]
            ings = ingredients[i]
            indegrees[r] = len(ings)
            for x in ings:
                connections[x].append(r)
        res = []
        q = deque(supplies)
        recipesSet = set(recipes)
        while len(q) > 0:
            node = q.popleft()
            if node in recipesSet:
                res.append(node)
            for child in connections[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
        return res
