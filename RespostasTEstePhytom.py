#  Codigo para fibonati em Phytom

fib1, fib2, times = input().split()
fib1 = int(fib1)
fib2 = int(fib2)
times = int(times)

for count in range (times-1):
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    
print (fib1)

# Frases ao contrario

num = int(input())

for n in range(num):
  broke = input().split()
  reverse = ""

  for m in range(len(broke)):
    reverse = broke[m]  + " " + reverse

  print(reverse)

# qual o nomero de tuplas de um numero que somados da a divisibilidade.


''' pelos meus testes e pelo que entendi do problema esse valor minimo de r vai dar na
maioria dos casos em infinito ou o tamanho em si do numero, pois não é para todos os
numeros primos que a regra de divisibilidade se aplica.
'''

'''
p = int(input())

lista = [x*p for x in range(10)]

teste = 1654646732548

teste2 = str(teste)
teste3 = teste2[3:5]

print(teste3)
print(int(teste3))
      

for r in range(1,  len(str(lista[-1]))    ):

    for num in lista:
        
        snum =  str(num)
        teste = 0
        
        for n in range(1 , len(snum) , r):
            if n+r > len(snum):
                teste = teste + int(snum[:-n])
            else:
                teste = teste + int(snum[-(n*r+1):-n])
            print (snum[-(n*r+1):-n])
   
'''

