# import random
import csv
def pesquisaBinaria(lista: list, valorProcurado: int) -> tuple[int,int]:
    return pesqBin(lista, valorProcurado, 0, len(lista)-1, 0)

def pesqBin(lista: list, valorProcurado: int, piso: int, teto: int, contador: int) -> tuple[int,int]:
    contador += 1

    if piso > teto:
        print('Valor não existe na lista')
        return (-1,-1)
    pos = (piso+teto)//2
    if lista[pos]==valorProcurado:
        return (contador,pos)
    if lista[pos]>valorProcurado:
        return pesqBin(lista,valorProcurado,piso,pos-1, contador)
    return pesqBin(lista,valorProcurado,pos+1,teto, contador)

def pesquisaSequencial(lista: list, valorProcurado: int) -> tuple[int,int]:
    return pesqSeq(lista,valorProcurado,0,0)

def pesqSeq(lista: list, valorProcurado: int, pos: int, contador: int)-> tuple[int,int]:
    contador += 1
    if len(lista) < pos:
        print('Valor não existe na lista')
        return (-1,-1)
    if lista[pos] == valorProcurado:
        return (contador, contador-1)
    return pesqSeq(lista, valorProcurado, pos+1, contador)

# def genList(size: int, max: int):
#     lista = []
#     for _ in range(size):
#         lista.append(random.randint(0,max))
#     lista.sort()
#     print(lista)

# genList(50,1000)
lista = [8, 63, 116, 132, 159, 183, 223, 237, 259, 319, 321, 324, 345, 354, 361, 367, 376,
         377, 396, 405, 474, 526, 527, 539, 562, 564, 596, 640, 663, 665, 677, 704, 729, 754,
         754, 758, 785, 788, 790, 800, 836, 844, 856, 902, 902, 914, 932, 937, 949, 966]

somaBin = 0
somaSeq = 0
piorS = piorPosS = melhorS = melhorPosS = piorB = piorPosB = melhorB = melhorPosB = 0
contador = pos = 0
with open("resultadosSequencial.csv",'w') as fs, open("resultadosBinario.csv", 'w') as fb:
    writerS = csv.writer(fs)
    writerS.writerow(['Media', 'Melhor Caso', 'Posicao Melhor', 'Pior Caso', 'Posicao Pior'])
    writerB = csv.writer(fb)
    writerB.writerow(['Media', 'Melhor Caso', 'Posicao Melhor', 'Pior Caso', 'Posicao Pior'])
    for i in range(1, len(lista)+1):
        for j in lista[0:i]:
            contador, pos = pesquisaBinaria(lista[0:i],j)
            somaBin += contador
            if contador > piorB or piorB == 0:
                piorB = contador
                piorPosB = pos
            if contador <  melhorB or melhorB == 0:
                melhorB = contador
                melhorPosB = pos

            contador, pos = pesquisaSequencial(lista[0:i],j)
            somaSeq += contador
            if contador > piorS or piorS == 0:
                piorS = contador
                piorPosS = pos
            if contador <  melhorS or melhorS == 0:
                melhorS = contador
                melhorPosS = pos
        
        medBin = somaBin / (i)
        medSeq = somaSeq / (i)
        writerS.writerow([medSeq,melhorS,melhorPosS,piorS,piorPosS])
        writerB.writerow([medBin,melhorB,melhorPosB,piorB,piorPosB])
        somaBin = somaSeq = piorB = melhorB = piorS = melhorS = 0