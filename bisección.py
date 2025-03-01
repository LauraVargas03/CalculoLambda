biseccion = lambda f, a, b, tol: (lambda m: m if abs(f(m)) < tol else biseccion(f, a, m, tol) if f(a) * f(m) < 0 else biseccion(f, m, b, tol))((a + b) / 2)

f = lambda x: x**2 - 2  # Función f(x) = x² - 2, buscamos la raíz en [1, 2]
print(biseccion(f, 1, 2, 0.0001))  # Aproximación de √2
