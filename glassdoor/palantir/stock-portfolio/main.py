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
    [[('8/7', 20), ('9/3', 70)],[('8/12', 50)],[('8/7', 10), ('8/12', 20), ('10/8', 90)]]
    
    Output:
    [('8/7', 30), ('8/12', 90), ('9/3', 140), ('10/8', 230)]
"""
def f(stocks_price_by_date):
    n = len(stocks_price_by_date)
    minheap = []
    for ticker in range(n):
        price_by_date = stocks_price_by_date[ticker]
        for date, price in price_by_date:
            mm, dd = date.split('/')
            mmd = int(m) * 100 + int(d)
            heappush(minheap, (mmdd, ticker, price))
    tickers_price = {i: 0 for i in range(n)}
    res = []
    current_date = None
    while len(minheap) > 0:
        date, ticker, price = heappop(minheap)
        if current_date == None:
            current_date = date
        if date == current_date:
            tickers_price[ticker] = price
        else:
            # print(tickers_price)
            res.append(sum(tickers_price.values()))
            current_date = date
            tickers_price[ticker] = price
    # print(tickers_price)
    res.append(sum(tickers_price.values()))
    return res

a = [[('8/7', 20), ('9/3', 70)],
    [('8/12', 50)],
    [('8/7', 10), ('8/12', 20), ('10/8', 90)]]

print(f(a))


    