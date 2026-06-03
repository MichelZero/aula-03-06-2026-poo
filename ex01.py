# autor: Michel
# data 03/06/2026

# A função recursiva para calcular o fatorial de 
# um número inteiro positivo é uma função que 
# chama a si mesma para resolver um problema menor até 
# atingir um caso base. 
# O fatorial de um número n (denotado como n!) é 
# o produto de todos os números inteiros positivos de 1 até n.

# 0! = 1 (definido como caso base)
# 1! = 1
# 2! = 2 * 1! = 2
# 3! = 3 * 2! = 3 * 2 * 1! = 6
# 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 24
# E assim por diante.

# 0! = 1
# 1! = 1
# 2! = 2 * 1! = 2
# 3! = 3 * 2! = 6
# 4! = 4 * 3! = 24
# 5! = 5 * 4! = 120


def  fatorial(n):
  if (n == 0):
    return 1
  else:
    return n * fatorial(n-1)
  
def  fat(n):
  if (n == 0) or (n ==1):
    return 1
  else:
    return n * fat(n-1)
  
##################################

valor = int(input("informe um valor: "))
print(f"{valor}! = {fat(valor)}")
