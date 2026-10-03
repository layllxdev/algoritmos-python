# Questão 1
num=[]
valor=float(input())
while valor!=-1:
    num.append(valor)
    valor=float(input())
print(len(num))
print(num)
print(sum(num))

# Questão 2
n=[]
for i in range(10):
    num1=int(input())
    n.append(num1)
print(n)
print(min(n))
print(n.index(min(n)))

# Questão 3
prioridade=[]
normal=[]
for i in range(30):
    nome=input()
    tipo=input()

    if tipo=="sim":
        prioridade.append(nome)
    else:
        normal.append(nome)
i=0
j=0
while i<len(prioridade) or j<len(normal):

    if i<len(prioridade):
        print(prioridade[i],"Prioridade")
        i+=1
    if j<len(normal):
        print(normal[j],"Normal")
        j+=1
    if j<len(normal):
        print(normal[j],"Normal")
        j+=1

# Prova
#1
num=[]
numero=float(input())
while numero!=-1:
    num.append(numero)
    numero=float(input())
print(len(num))
print(num)
print(sum(num))

#2
num=[]
for i in range(10):
    lista=float(input())
    num.append(lista)
print(num)
print(min(num))
print(num.index(min(num)))