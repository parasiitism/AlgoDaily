def f():
    n, m, a, b = map(int, input().split())

    if m * a <= b:
        return n * a

    m_ride_specials_count = (n//m) * b
    one_ride_count = min((n % m) * a, b)
    return m_ride_specials_count + one_ride_count


print(f())
