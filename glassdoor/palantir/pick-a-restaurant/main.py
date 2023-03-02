from collections import *
"""
    Two friends are getting together to have dinner at a restaurant. They can't figure out where to go so they decide to ask their friends for help.
    The two friends want to choose a restaurant such that:
    * Neither of them already likes it, and
    * It is liked by the most number of their mutual friends.
    
    Suppose you have data about who is friends with whom and what restaurants they've liked.
    
    friends = [
        [ "Ted", "Lily" ],
        [ "Ted", "Robin" ],
        [ "Lily", "Robin" ],
        [ "Ted", "Marshall" ],
        [ "Marshall", "Lily" ],
        [ "Calvin", "Marshall"],
        [ "Emily", "Marshall"],
    ]
    
    likes = [
        [ "Lily", "Restaurant_1", "Restaurant_17", "Restaurant_3" ],
        [ "Ted", "Restaurant_17", "Restaurant_1" ],
        [ "Robin", "Restaurant_5" ],
        [ "Marshall", "Restaurant_17", "Restaurant_5", "Restaurant_4" ],
        [ "Calvin", "Restaurant_17"],
        [ "Emily", "Restaurant_17"]
    ]
    
    In this example, Ted and Lily should go to Restaurant_5. Their mutual friends are Robin and Marshall. 
    One or both of Ted and Lily have already liked Restaurant_1, Restaurant_3, and Restaurant_17. 
    Robin and Marshall both like Restaurant_5, but only Marshall likes Restaurant_4.
    
    Write a function that given the friendship data, the likes data, and two names, will return the restaurant they should go to. 
    If there is more than one possible restaurant, return any one. If no such restaurant exists, return None (or an empty string).
    
    All test cases:
    restaurant_suggestion(friends_1, likes_1, "Ted", "Lily")      -> Restaurant_5
    restaurant_suggestion(friends_2, likes_2, "Ted", "Ranjit")    -> None
    restaurant_suggestion(friends_2, likes_2, "Lily", "Marshall") -> None
    restaurant_suggestion(friends_2, likes_3, "Ted", "Marshall")  -> Restaurant_4 or Restaurant_5
    
    Complexity variables:
    N = the number of people
    M = the number of restaurants
"""
def f(friends, likes, person1, person2):
    # can be pre-compute
    G = defaultdict(set)
    for a, b in friends:
        G[a].add(b)
        G[b].add(a)
    M = defaultdict(set)
    for arr in likes:
        name = arr[0]
        rests = arr[1:]
        for r in rests:
            M[r].add(name)
    
    # person1&2 related
    mutuals = set()
    for f in G[person1]:
        if f != person2 and f in G[person2]:
            mutuals.add(f)
    for f in G[person2]:
        if f != person1 and f in G[person1]:
            mutuals.add(f)
    rests_by_popularity = Counter()
    res = []
    max_popularity = 0
    for r in M:
        names = M[r]
        if person1 in names or person2 in names:
            continue
        for n in names:
            if n in mutuals:
                rests_by_popularity[r] += 1
                if rests_by_popularity[r] > max_popularity:
                    res = [r]
                    max_popularity = rests_by_popularity[r]
                elif rests_by_popularity[r] == max_popularity:
                    res.append(r)
    return res

friends = [
    [ "Ted", "Lily" ],
    [ "Ted", "Robin" ],
    [ "Lily", "Robin" ],
    [ "Ted", "Marshall" ],
    [ "Marshall", "Lily" ],
    [ "Calvin", "Marshall"],
    [ "Emily", "Marshall"],
]
likes = [
    [ "Lily", "Restaurant_1", "Restaurant_17", "Restaurant_3" ],
    [ "Ted", "Restaurant_17", "Restaurant_1" ],
    [ "Robin", "Restaurant_5" ],
    [ "Marshall", "Restaurant_17", "Restaurant_5", "Restaurant_4" ],
    [ "Calvin", "Restaurant_17"],
        [ "Emily", "Restaurant_17"]
]

print(f(friends, likes, "Ted", "Lily"))
print(f(friends, likes, "Ted", "Ranjit"))
print(f(friends, likes, "Lily", "Marshall"))
print(f(friends, likes, "Calvin", "Emily"))