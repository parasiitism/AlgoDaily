"""
Questions to ask:
- can i assume that the source and the destination are different place? yes
- is there any loop? probably not because it is hard to determind which go first
"""


def correctFlights(flights):
    """
    flights: ["SJC-LAX", "SFO-SJC", "LAX-MIA"]
    return: ["SFO-SJC", "SJC-LAX", "LAX-MIA"]
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


print(correctFlights(["SFO-SJC", "SJC-SFO"]))
print(correctFlights(["SFO-SJC", "SJC-LAX", "LAX-MIA"]))
print(correctFlights(["SJC-LAX", "SFO-SJC", "LAX-MIA"]))
print(correctFlights(["A-B", "B-C", "C-D", "D-E", "E-F"]))
print(correctFlights(["D-E", "A-B", "E-F", "B-C", "C-D"]))
