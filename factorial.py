from functools import reduce

factorialRecursivo = lambda n: 1 if n == 0 else n * factorialRecursivo(n - 1)
factorialIterativo = lambda n: 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

print(factorialRecursivo(5))
print(factorialIterativo(5))
