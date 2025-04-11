n = int(input())

lista = []
somatorio = 0

for _ in range(n):
    valor = int(input())


    if valor != 0:
        lista.append(valor)

        somatorio += valor
        
    else:
        somatorio -= lista.pop()

print(somatorio)