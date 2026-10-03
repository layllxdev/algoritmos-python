nomeVend=input()
salFix=float(input())
totalVend=float(input())
comissao=totalVend*0.15
salario=salFix+comissao
print("Total = R$ {:.2f}".format(salario))