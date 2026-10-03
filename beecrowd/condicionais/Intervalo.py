valor=float(input())
int1=[0,25]
int2=[25,50]
int3=[50,75]
int4=[75,100]
if 0<=valor<=25:
    print("Intervalo [0,25]")
elif 25<valor<=50:
    print("Intervalo [25,50]")
elif 50<valor<=75:
    print("Intervalo [50,75]")
elif 75<valor<=100:
    print("Intervalo [75,100]")
else:
    print("Fora de Intervalo")