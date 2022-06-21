import statistics
qtdConjunto = int(input("Qual o tamanho do conjunto: "))
temperaturas = []

for  i in range(1,qtdConjunto+1) :
 valores = int(input('Insira o ' + str(i) +'º valor:'))
 temperaturas.append(valores)


media = int(sum(temperaturas)/len(temperaturas))

mediana = statistics.median(temperaturas)

print("Temperaturas antes da ordem:" + str(temperaturas) )

print("Temperaturas ordenadas" + str(sorted(temperaturas)) + ' K')

print('Mediana - ' + str(mediana)+' K')

print('Media - '+ str((media)) + ' K')
