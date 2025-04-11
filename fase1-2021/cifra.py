# Desafio: Cifra da Nlogônia
# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/

p = input()

cifra = ''


alfabeto = "abcdefghijklmnopqrstuvxz"

for c in p:
    if c not in "aeiou":
        pos_c = pos_letra[c]

        pos_a = pos_c - 1
        pos_p = pos_c + 1
        for _