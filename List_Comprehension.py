print([x for x in range(2, 1000) if any(x % y != 0 for y in range(2, x))])
# print([x for x in range(2, 1000) for y in range(2, x) if x % x == 0 and x % 1 == 0 and x % y != 0])
