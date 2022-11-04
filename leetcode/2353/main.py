from sortedcontainers import SortedList

"""
    Hashtable + Sorted container

    Time of changeRating    O(N)
    Space                   O(N)
    1098 ms, faster than 84.55%
"""


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine_map = {}
        self.cuisine_food_rating = defaultdict(SortedList)
        n = len(foods)
        for i in range(n):
            f = foods[i]
            c = cuisines[i]
            r = ratings[i]
            self.food_cuisine_map[f] = (c, r)
            self.cuisine_food_rating[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.food_cuisine_map[food]
        self.food_cuisine_map[food] = c, newRating
        self.cuisine_food_rating[c].remove((-r, food))
        self.cuisine_food_rating[c].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_rating[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
