mcd = lambda x, y: x if y == 0 else mcd(y, x % y)

print(mcd(48, 18))
