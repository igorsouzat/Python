import time

def mergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        left = lista[:meio]
        right = lista[meio:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k]=left[i]
                i=i+1
            else:
                lista[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            lista[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            lista[k]=right[j]
            j=j+1
            k=k+1


#EXECUTANDO
lista = list(range(0, 10000))
lista.reverse()
#print("Lista: ",lista)

#INICIO
inicio = time.time()
mergeSort(lista)
fim = time.time()
#print("\nLista organizada: ", lista)
print("\nTempo: ", fim - inicio)
