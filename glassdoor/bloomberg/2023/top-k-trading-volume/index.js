/*
    You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you maintain if:

    - You have to tell top k products traded by volume at end of day.
    - You have to tell top k products traded by volume throughout the day.

    stream of input of
    {EURUSD, 100}
    {CHFEUR, 200}
    {EURUSD, 100}‍‌‌‍‌‍‌‍‍‌‌‌‍‌‌‌‍‌‌
    return the top k total amount
*/


// leetcode1244, there are a few solutions