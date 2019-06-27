import urllib
from urllib.parse import urlparse


def isMatched(a, b):
    a = a.lower()
    b = b.lower()
    x = urlparse(a)
    y = urlparse(b)

    # octet-by-octet
    for i in range(len(x)):
        if i == 1:
            # check domain
            hostA = x.hostname
            hostB = y.hostname
            if hostA != hostB:
                return False
            # check port
            portA = x.port
            if portA == 80:
                portA = None
            portB = y.port
            if portB == 80:
                portB = None
            if portA != portB:
                return False
        else:
            octA = x[i]
            octB = y[i]
            if checkEncoding(octA, octB) == False:
                return False
    return True


def checkEncoding(a, b):
    a = a.strip()
    b = b.strip()
    if a == b:
        return True
    a_ = urllib.parse.unquote(a).lower()
    b_ = urllib.parse.unquote(b).lower()
    if a == b_ or a_ == b:
        return True
    return False


s = "http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html"
links = s.split(';')
b = isMatched(links[0], links[1])
print(b)

s = "HTTPS://abc.com:8080/path/index*!^(~|>`^|<{`{>.html;HTTP://EXAMPLE.com:8081//index{~.html"
links = s.split(';')
b = isMatched(links[0], links[1])
print(b)
