def linear_search(arr, x):
    """
    Realiza una búsqueda lineal para encontrar el elemento x en la lista arr.
    Devuelve el índice del elemento si se encuentra en la lista, o -1 si no se encuentra.
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

# Muestra un menú al usuario para que seleccione si quiere cargar un archivo o ingresar los números manualmente
print("¿Cómo desea ingresar los números?")
print("1. Cargar un archivo")
print("2. Ingresar los números manualmente")

option = int(input("Seleccione una opción (1 o 2): "))

# Si el usuario selecciona la opción 1, solicita al usuario el nombre del archivo a cargar y carga los números
if option == 1:
    filename = input("Ingrese el nombre del archivo de números: ")
    with open(filename, "r") as f:
        my_list = [int(x) for x in f.read().split()]

# Si el usuario selecciona la opción 2, solicita al usuario que ingrese los números manualmente
elif option == 2:
    my_list = [int(x) for x in input("Ingrese los números separados por comas: ").split(",")]

# Si el usuario ingresa una opción inválida, muestra un mensaje de error y sale del programa
else:
    print("Opción inválida.")
    exit()

# Solicita al usuario el número a buscar
search_for = int(input("Ingrese el número que desea buscar: "))

# Busca el número en la lista utilizando la función linear_search
result = linear_search(my_list, search_for)

# Imprime el resultado de la búsqueda
if result == -1:
    print(f"{search_for} no se encuentra en la lista")
else:
    print(f"{search_for} se encuentra en la posición {result}")

## Brandon Morales https://www.instagram.com/lewenn19/