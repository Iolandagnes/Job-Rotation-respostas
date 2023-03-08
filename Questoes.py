'''QUESTÃO 01'''

from itertools import count


indice, soma, k = 13, 0, 0
while k < indice:
    k += 1
    soma += k
print(f"O valor da soma é {soma}")

'''QUESTÃO 02'''

num = int(input("Informe o número desejado da Sequência de Fibonacci: "))
fib = [0]
ultimo = 1
penultimo = 1
if num == 0:
    print(f"A sequência é: {fib}")
elif num == 1:
    fib.append(1)
    print(f"A sequência é: {fib}")
else:
    fib.append(1)
    for i in range(1,num-1):
        termfinal = ultimo + penultimo
        penultimo = ultimo
        ultimo = termfinal
        fib.append(termfinal)
    print(f"A sequência é: {fib}")

'''QUESTÃO 03'''

#lETRA A
l1 = []
for i in range(1,10,2):
    l1.append(i)
print(f"Letra A: {l1}")
#LETRA B
l2 = [2]
i = 2
for count in range(0,6):
    i *= 2
    l2.append(i)
print(f"Letra B: {l2}")
#LETRA C
l3 = []
for count in range(0, 8):
    count **= 2
    l3.append(count)
print(f"Letra C: {l3}")
#LETRA D
l4 = [4]
for i in range(4, 12, 2):
    i **= 2
    l4.append(i)
print(f"Letra D: {l4}")
#LETRA E
l5 = [1, 1]
n = 7
for i in range(1,n):
        termfinal = ultimo + penultimo
        penultimo = ultimo
        ultimo = termfinal
        l5.append(termfinal)
print(f"Letra E: {l5}")
#LETRA F
l6 = [2, 10, 12, 16, 17, 18, 19, 200]
print(f"Letra F: {l6}")

'''QUESTÃO 04

Considerando as questões mencionadas pelo problema, podemos concluir que os dois estarão à mesma distância de Ribeirão Preto,
já que nesse momento se cruzarão na rodovia'''

'''QUESTÃO 05'''

'''t1, t2, t3, t4, t5, t6, t7 = 'E', 'S', 'T','Á', 'G', 'I', 'O'
print(t7, t6, t5, t4, t3, t2, t1)'''

palavra = input("Informe a palavra: ")
print(palavra[::-1])
