"""
    give u a list, every element in the list has <productId, productRating>
    , return the average rating of top 5 ratings for each product

    Questions to ask:
    - will there be less than 5 ratingss for a product? yes, if < 5, just calculate the average
    - no malformed rating? e.g. { "id1234": "" } <= rating is not number and empty
"""


class Product(object):
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating


def top5average(products):
    # sort the products by its rating such that the O(nlogn)
    products = sorted(products, key=lambda x: x.rating, reverse=True)
    # put the products ratings in a hashtable { id1 : [rating1, rating2...], ...}
    ht = {}
    for ele in products:
        key = ele.id
        val = ele.rating
        if key in ht:
            ht[key].append(val)
        else:
            ht[key] = [val]
    # calculate the average
    res = {}
    for k in ht:
        v = ht[k]
        if len(v) > 5:
            v = v[:5]
            avr = sum(v)/5.0
            res[k] = avr
        else:
            avr = sum(v)/float(len(v))
            res[k] = avr
    return res


# test
a = [
    Product(1, 9),
    Product(2, 2),
    Product(1, 10),
    Product(2, 1),
    Product(2, 3),
    Product(1, 9),
    Product(2, 1),
    Product(1, 10),
]

print(top5average(a))

a = [
    Product(1, 9),
    Product(2, 2),
    Product(1, 10),
    Product(2, 1),
    Product(2, 3),
    Product(1, 9),
    Product(2, 1),
    Product(1, 10),
    Product(1, 10),
    Product(1, 10),
]

print(top5average(a))
