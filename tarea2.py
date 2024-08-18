import itertools

def generar_combinaciones(arr):
    total_combinaciones = 0 #T(n)=1

    # Generar combinaciones de todos los tamaños posibles
    for r in range(1, len(arr) + 1):  #T(n) = 2n
        combinaciones = list(itertools.combinations(arr, r))
        total_combinaciones += len(combinaciones)
        for combinacion in combinaciones: #T(n) = n
            print(combinacion) #T(n) = 1

    print(f"Total de combinaciones: {total_combinaciones}")  #T(n) = 1


# Ejemplo de uso
arreglo = [1, 2, 3 , 4]  #T(n) = 1
generar_combinaciones(arreglo)

# EN TOTAL 2n^2 + 3
