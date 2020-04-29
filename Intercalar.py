listaA = [0]*10
listaB = [0]*10

listaR = [0]*20

for i in  range(10):
    print( "digite um numero")
    listaA[i] = int(input())

for i in range(10):
    print( "digite um numero")
    listaB[i] = int(input())

proximolivre = 0

for i in range (10):
    listaR[proximolivre] = listaA[i]
    proximolivre = proximolivre + 1
    listaR[proximolivre] = listaB[i]
    proximolivre = proximolivre + 1

print(listaA)
print(listaB)
print(listaR)
