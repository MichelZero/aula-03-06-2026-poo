# autor: Michel
# data 03/06/2026

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
