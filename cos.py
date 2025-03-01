import math

cos_x = lambda x, n: sum([((-1)**k * (x**(2*k))) / math.factorial(2*k) for k in range(n)])

print(cos_x(math.pi/3, 10))  #Aproximación de cos(π/3) ≈ 0.5
