IdadeDias=int(input())
anos=IdadeDias//365
resto=IdadeDias%365
meses=resto//30
DiasRestantes=resto%30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{DiasRestantes} dia(s)")