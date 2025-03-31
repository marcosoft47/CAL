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
        return (contador, pos)
    return pesqSeq(lista, valorProcurado, pos+1, contador)

# def genList(size: int, max: int):
#     lista = []
#     for _ in range(size):
#         lista.append(random.randint(0,max))
#     lista.sort()
#     print(lista)

# genList(100,1000)
lista = [1, 23, 39, 43, 57, 94, 103, 104, 109, 110, 118, 119, 129, 150, 152, 156, 157, 172, 180, 181, 188, 189, 197, 215, 216, 219, 220, 223, 247, 294, 311, 312, 317, 324, 331, 356, 360, 366, 389, 395, 396, 397, 415, 425, 437, 448, 450, 461, 482, 491, 495, 505, 512, 513, 548, 562, 566, 586, 588, 594, 596, 614, 618, 632, 640, 648, 665, 669, 713, 717, 720, 723, 729, 740, 743, 771, 780, 791, 815, 841, 842, 848, 881, 882, 883, 912, 917, 926, 928, 942, 947, 950, 961, 965, 968, 975, 976, 985, 994, 997]

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