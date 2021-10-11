# Muñoz Gonzalez Job Alejandro
# ICO G-52
# para la clase de investigacion de opereciones
from fractions import Fraction as Frac
# =============================================================================
# Este programa solo resuelve los tableaus que tengan solucion inicial
# no crea un tableau inicial en base a un modelo, por lo cual hay que darle
# el numero de filas y el numero de columnas de la matriz, tambien se debe de
# nombrar a las columnas
#
# ACTUALIZACIONES A FUTURO
# 1. Que el programa saque las variables no basicas y las variables basicas
#    Por tableau
# 2. Mejorar el formato en que se muestran los tableaus
# 3. Crear un Tableau inicial dandole al programa solamente las ecuaciones
# 4. Crear un Tableau inicial para aquellos problemas que no tengan solucion
#    inicial
# =============================================================================


# crea una lista de nombres de las columnas
def NombrarColumnas(columnas):
    tabla = []
    for i in range(columnas):
        nombre = input("Nombra a la columna "+str(i+1)+": ")
        tabla.append(nombre)
    return(tabla)


# crea el tableau inicial
def CrearTableauInicial(filas, columnas):
    tableau = []
    for i in range(filas):
        tabla = []
        for j in range(columnas):
            tabla.append(
                Frac(input("Valor en la fila "+str(i+1)+" columna "+str(j+1)+": ")))
        tableau.append(tabla)
    return(tableau)


# definiremos si el tableau insertado es optimo
# si regresa un True significa que el tableu no es optimo
# si regresa False el tableu es optimo
def VerificarTableau(tableau, columnas, tipo):
    # condicion para maximizacion
    if tipo == 0:
        for i in range(columnas-1):
            if tableau[0][i] < 0:
                return True
        return False

    # condicion para minimizacion
    else:
        for i in range(columnas-1):
            if tableau[0][i] > 0:
                return True
        return False


# esta funcion regresa la posicion en la que se encuentra el numero mas negativo
# o mas positivo segun sea el caso
def LocalizarPosicionFilaZ(tableau, columnas, tipo):
    filaOrdenada = []
    # condicion para maximizacion
    if tipo == 0:
        for i in range(columnas-1):
            if tableau[0][i] <= 0:
                filaOrdenada.append(tableau[0][i])

        filaOrdenada.sort()
        for i in range(columnas-1):
            if filaOrdenada[0] == tableau[0][i]:
                return i
    # condicion para minimizacion
    else:
        for i in range(columnas-1):
            if tableau[0][i] >= 0:
                filaOrdenada.append(tableau[0][i])

        filaOrdenada.sort()
        for i in range(columnas-1):
            if filaOrdenada[-1] == tableau[0][i]:
                return i


# Devuelve un tableau actualizado el cual tendra ya la fila pivote en el
def Ratio(tableau, numeroColumna, filas):
    listaDivisiones = []
    listaRatio = []
    try:
        for i in range(1, filas):
            listaDivisiones.append(tableau[i][-1]/tableau[i][numeroColumna])
    except ZeroDivisionError:
        # En caso de division entre 0 se insertara un -1 para que no cuente para el ratio
        listaDivisiones.append(-1)
    for i in range(len(listaDivisiones)):
        if listaDivisiones[i] >= 0:
            listaRatio.append(listaDivisiones[i])
    listaRatio.sort()
    for i in range(len(listaDivisiones)):
        if listaRatio[0] == listaDivisiones[i]:
            return i+1


# Devuelve el numero de la fila donde se encuentra la fila pivote
def CrearPivote(fila, columna, numColumnas, tableau):
    numDivisor = tableau[fila][columna]
    for i in range(numColumnas):
        tableau[fila][i] = tableau[fila][i]/numDivisor
    return tableau


# Actualiza el tableau ingresado dandole el tableau, el numero de filas,
# el numero de columnas, el numero de la fila pivote y el numero de la columna
# que se volveran 0
def ActualizarTableau(tableau, numFilas, numColumnas, fila, columna):
    listaDivisores = []
    for i in range(numFilas):
        listaDivisores.append(tableau[i][columna]*-1)

    for i in range(numFilas):
        if i != fila:
            for j in range(numColumnas):
                tableau[i][j] = (
                    (tableau[fila][j]*listaDivisores[i])+tableau[i][j])
    return tableau


# Solo muestra el Tableu en un formato especifico, CUIDADO todo funciona al rededor
# de la longitud de la lista de nombres
def MostrarTableau(tableau, nombres):
    x = len(nombres)

    for i in range(x):
        print('-'*10, end="")
    print('-'*(x+1))

    print('|', end="")
    for i in range(x):
        print('{0:>10}|'.format(nombres[i]), end="")
    print('')

    for i in range(x):
        print('-'*10, end="")
    print('-'*(x+1))

    for i in range(len(tableau)):
        print('|', end="")
        for j in range(x):
            if j == x-1:
                print('{0:>10}|'.format(str(tableau[i][j])))
            else:
                print('{0:>10}|'.format(str(tableau[i][j])), end="")

    for i in range(x):
        print('-'*10, end="")
    print('-'*(x+1))


def NuevoTableau(tableau, filas, columnas, tipo):
    numeroColumna = LocalizarPosicionFilaZ(tableau, columnas, tipo)
    numeroFila = Ratio(tableau, numeroColumna, filas)
    tableau = CrearPivote(numeroFila, numeroColumna, columnas, tableau)
    tableau = ActualizarTableau(
        tableau, filas, columnas, numeroFila, numeroColumna)
    return tableau


def main():
    tipoProblema = int(
        input("De que tipo es el problema? Maximizacion = 0, Minimizacion = 1: "))
    numFilas = int(input("Ingresa el numero de filas del tableau: "))
    numColumnas = int(input("Ingresa el numero de columnas del tableau: "))
    tableau = CrearTableauInicial(numFilas, numColumnas)
    listaNombres = NombrarColumnas(numColumnas)
    # tableau = [[Frac(-10), Frac(-15), Frac(-20), Frac(0), Frac(0), Frac(0)], [Frac(2), Frac(4),
    #             Frac(6), Frac(1), Frac(0), Frac(24)], [Frac(3), Frac(9), Frac(6), Frac(0), Frac(1), Frac(30)]]
    # listaNombres = ["X1", "X2", "X3", "h1", "h2", "Solucion"]
    noOptimo = True
    contador = 1
    print('')
    print("TABLEAU INICIAL")
    MostrarTableau(tableau, listaNombres)
    noOptimo = VerificarTableau(tableau, numColumnas, tipoProblema)
    if noOptimo:
        print("El TABLEAU INICIAL NO ES OPTIMO")
        while noOptimo:
            print('')
            print("TABLEAU NUMERO "+str(contador))
            MostrarTableau(tableau, listaNombres)
            noOptimo = VerificarTableau(tableau, numColumnas, tipoProblema)
            if noOptimo:
                tableau = NuevoTableau(
                    tableau, numFilas, numColumnas, tipoProblema)
                print("El TABLEAU ACTUAL NO ES OPTIMO")
                contador += 1
                continue
            else:
                print("EL TABLEAU ACTUAL ES OPTIMO")
                break
    else:
        print("El TABLEAU INICIAL ES OPTIMO")
    print("fin del programa")


if __name__ == "__main__":
    main()