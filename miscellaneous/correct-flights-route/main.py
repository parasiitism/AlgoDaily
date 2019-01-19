"""
Questions to ask:
- can i assume that the source and the destination are different place? yes
- is there any loop? probably not because it is hard to determind which go first
"""


def correctFlights(flights):
    """
    flights: ["SJC-LAX", "SFO-SJC", "LAX-MIA"]
    return: ["SFO-SJC", "SJC-LAX", "LAX-MIA"]
    Time    O(n^2)
    Space   O(n) result
    """
    result = []
    while len(flights) > 0:
        head = flights.pop(0)
        temp = [head]
        i = 0
        while i < len(flights):
            src, dst = temp[-1].split("-")
            x, y = flights[i].split("-")
            if dst == x:
                temp.append(flights[i])
                flights = flights[:i]+flights[i+1:]
            else:
                i += 1
        result = temp + result
    return result


def correctFlights(flights):
    """
    flights: ["SJC-LAX", "SFO-SJC", "LAX-MIA"]
    return: ["SFO-SJC", "SJC-LAX", "LAX-MIA"]
    Time    O(3n)
    Space   O(n) result
    19jan2019
    """
    if len(flights) == 0:
        return []

    forward = {}
    backwarod = {}

    for flight in flights:
        src, dst = flight.split("-")
        forward[src] = dst
        backwarod[dst] = src

    result = [flights[0]]

    while True:
        src, dst = result[-1].split("-")
        if dst in forward:
            result.append(dst+"-"+forward[dst])
        else:
            break

    while True:
        src, dst = result[0].split("-")
        if src in backwarod:
            result = [backwarod[src]+"-"+src] + result
        else:
            break

    return result


print(correctFlights(["SFO-SJC", "SJC-LAX", "LAX-MIA"]))
print(correctFlights(["SJC-LAX", "SFO-SJC", "LAX-MIA"]))
print(correctFlights(["A-B", "B-C", "C-D", "D-E", "E-F"]))
print(correctFlights(["D-E", "A-B", "E-F", "B-C", "C-D"]))
