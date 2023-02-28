from collections import *
"""
    The people who buy ads on our network don't have enough data about how ads are working for
    their business. They've asked us to find out which ads produce the most purchases on their website.

    Our client provided us with a list of user IDs of customers who bought something on a landing page
    after clicking one of their ads:

    # Each user completed 1 purchase.
    completed_purchase_user_ids = [
    "3123122444","234111110", "8321125440", "99911063"]

    And our ops team provided us with some raw log data from our ad server showing every time a
    user clicked on one of our ads:
    ad_clicks = [
    #"IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
    ]
        
    The client also sent over the IP addresses of all their users.
        
    all_user_ips = [
    #"User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
    ]
        
    Write a function to parse this data, determine how many times each ad was clicked,
    then return the ad text, that ad's number of clicks, and how many of those ad clicks
    were from users who made a purchase.


    Expected output:
    Bought Clicked Ad Text
    1 of 2  2017 Pet Mittens
    0 of 1  The Best Hollywood Coats
    3 of 3  Buy wool coats for your pets
"""
def f(completed_purchase_user_ids, ad_clicks, all_user_ips):
    ip2user = {}
    for s in all_user_ips:
        uid, ip = s.split(',')
        ip2user[ip] = uid
    
    purchaseds = set(completed_purchase_user_ids)
    ad2views = Counter()
    ad2purchase = Counter()
    for s in ad_clicks:
        ip, t, ad = s.split(',')
        ad2views[ad] += 1
        if ip in ip2user:
            user = ip2user[ip]
            if user in purchaseds:
                ad2purchase[ad] += 1
    res = []
    for ad in ad2views:
        views = ad2views[ad]
        purchases = ad2purchase[ad]
        s = str(purchases) + ' of ' + str(views) + ' ' + ad
        res.append(s)
    return res


a = ["3123122444","234111110", "8321125440", "99911063"]
b = [
    #"IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
c = [
    #"User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]
print(f(a, b, c))