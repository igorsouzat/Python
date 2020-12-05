import time

def insertionSort(lista):
	for i in range(1, len(lista)):
		chave = lista[i]
		j = i - 1
		while j >= 0 and chave < lista[j]:
			lista[j+1] = lista[j]
			j -= 1
		lista[j+1] = chave
		

#EXECUTANDO
lista = list(range(0, 10000))
lista.reverse()
#print("Lista: ", lista)


#INICIO
inicio = time.time()
insertionSort(lista)
fim = time.time()
#print("\nLista organizada: ", lista)
print("\nTempo: ",fim - inicio)
