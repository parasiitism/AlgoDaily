
# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass

class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:

        roots = {x: x for x in range(n)}

        def union(i, j):
            parent = i
            while parent != roots[parent]:
                parent = roots[parent]
            roots[j] = parent

        for i in range(n):
            for j in range(i+1, n):
                if categoryHandler.haveSameCategory(i, j):
                    union(i, j)

        res = set()
        for key in roots:
            val = roots[key]
            res.add(val)

        return len(res)
