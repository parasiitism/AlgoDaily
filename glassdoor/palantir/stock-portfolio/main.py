from heapq import *

"""
    Given a list of stocks price by date, return the profolio by date

    Date:   8/7     8/12    9/3     10/8
    GOOG    20              70
    META            50
    AMZN    10      20              90
    ------------------------------------
    res     30      90      140     210

    
    Input:
    [
        [('8/7', 20), ('9/3', 70)],
        [('8/12', 50)],
        [('8/7', 10), ('8/12', 20), ('10/8', 90)]
    ]
    
    Output:
    [('8/7', 30), ('8/12', 90), ('9/3', 140), ('10/8', 210)]

    Time    O(KlogN) K: total number of records, N: number of stocks
    Space   O(K)
"""
from collections import *


def date2int(s):
    mm, dd = s.split('/')
    return int(mm)*100 + int(dd)


def int2date(n):
    mm = n // 100
    dd = n % 100
    return str(mm) + '/' + str(dd)


def stock_portfolio_per_day(stocks_price_by_date):
    n = len(stocks_price_by_date)
    minheap = []
    for i in range(n):
        date_str, price = stocks_price_by_date[i][0]
        date = date2int(date_str)
        heappush(minheap, (date, i, 0))  # (date, i, j)

    stocks = Counter()
    res = []
    cur_date = None
    cur_total = 0
    while len(minheap) > 0:
        date, i, j = heappop(minheap)

        # 2nd approach
        if date != cur_date and cur_date != None:
            res.append((int2date(cur_date), cur_total))
        cur_date = date
        cur_total -= stocks[i]
        cur_total += stocks_price_by_date[i][j][1]
        stocks[i] = stocks_price_by_date[i][j][1]

        # 1st approach: O(N)
        # total = sum(stocks.values())
        # res[date_str] = total

        j += 1
        if j < len(stocks_price_by_date[i]):
            _date_str, _price = stocks_price_by_date[i][j]
            _date = date2int(_date_str)
            heappush(minheap, (_date, i, j))
    res.append((int2date(cur_date), cur_total))
    return res


a = [
    [('8/7', 20), ('9/3', 70)],
    [('8/12', 50)],
    [('8/7', 10), ('8/12', 20), ('10/8', 90)]
]

print(stock_portfolio_per_day(a))
