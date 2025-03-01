es_primo = lambda n, d=2: True if n <= 2 else False if n % d == 0 else es_primo(n, d + 1) if d * d <= n else True

print(es_primo(7))  #Salida: True
print(es_primo(10))  #Salida: False
