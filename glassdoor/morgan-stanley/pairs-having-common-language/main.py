"""
    You are given a list of people and the languages spoken by each person

    e.g.
    A1--> English, Hindi, Spanish
    A2--> German, Hindi, Urdu
    ...
    An--> Tamil, Italian

    You have to calculate number of pairs of people who spoke at least one common language.
"""


def commonLanguagePairs(people, theirLangs):
    m = {}
    for i in range(len(people)):
        person = people[i]
        langs = theirLangs[i]
        for lang in langs:
            if lang not in m:
                m[lang] = [person]
            else:
                m[lang].append(person)
    pairs = set()
    for lang in m:
        arr = m[lang]
        if len(arr) < 2:
            continue
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                temp = (arr[i], arr[j])
                rev = (arr[j], arr[i])
                if temp not in pairs and rev not in pairs:
                    pairs.add(temp)
    return list(pairs)


a = ['Calvin', 'Peter', 'Paul', 'Anson', 'Bob', 'Lily']
b = [
    ['english', 'cantonese', 'mandarin'],
    ['english', 'spanish', 'mandarin'],
    ['german', 'hindi'],
    ['hindi', 'english'],
    ['german', 'cantonese'],
    ['japanese', 'english', 'mandarin'],
]
print(commonLanguagePairs(a, b))
