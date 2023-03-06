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
    [('8/7', 30), ('8/12', 90), ('9/3', 140), ('10/8', 230)]
"""
def int2date(n):
    mm = n // 100
    dd = n % 100
    return str(mm) + '/' + str(dd)

def f(stocks_price_by_date):
    n = len(stocks_price_by_date)
    minheap = []
    for sid in range(n):
        price_by_date = stocks_price_by_date[sid]
        for date, price in price_by_date:
            mm, dd = date.split('/')
            mmdd = int(mm) * 100 + int(dd)
            heappush(minheap, (mmdd, sid, price))
    stock_prices = {i: 0 for i in range(n)}
    res = []
    current_date = None
    while len(minheap) > 0:
        date, sid, price = heappop(minheap)
        if current_date == None:
            current_date = date
        if date == current_date:
            stock_prices[sid] = price
        else:
            res.append([int2date(current_date), sum(stock_prices.values())])
            current_date = date
            stock_prices[sid] = price
    res.append([int2date(current_date), sum(stock_prices.values())])
    return res

a = [[('8/7', 20), ('9/3', 70)],
    [('8/12', 50)],
    [('8/7', 10), ('8/12', 20), ('10/8', 90)]]

print(f(a))


    