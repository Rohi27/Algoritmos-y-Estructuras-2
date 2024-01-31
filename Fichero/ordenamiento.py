import heapq



def quicksort_asc(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Selecciona el primer elemento como pivote
        # Divide el arreglo en dos sublistas: elementos menores o iguales al pivote y elementos mayores al pivote
        less = [x for x in arr[1:] if x[key] <= pivot[key]]
        greater = [x for x in arr[1:] if x[key] > pivot[key]]
        return quicksort_asc(greater, key) + [pivot] + quicksort_asc(less, key)  # Combina las sublistas y el pivote

def quicksort_desc(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Selecciona el primer elemento como pivote
        # Divide el arreglo en dos sublistas: elementos menores al pivote y elementos mayores o iguales al pivote
        less = [x for x in arr[1:] if x[key] < pivot[key]]
        greater = [x for x in arr[1:] if x[key] >= pivot[key]]
        return quicksort_desc(less, key) + [pivot] + quicksort_desc(greater, key)  # Combina las sublistas y el pivote
    
def mergesort_desc(arr, key):
    if len(arr) <= 1:
        return arr

    # Divide la lista en mitades
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Aplica recursivamente Mergesort a cada mitad
    left_half = mergesort_desc(left_half, key)
    right_half = mergesort_desc(right_half, key)

    # Combina las mitades ordenadas
    return merge_desc(left_half, right_half, key)

def merge_desc(left, right, key):
    result = []
    left_index, right_index = 0, 0

    # Combina las mitades ordenadas
    while left_index < len(left) and right_index < len(right):
        if left[left_index][key] < right[right_index][key]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Agrega los elementos restantes, si los hay
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def mergesort_asc(arr, key):
    if len(arr) <= 1:
        return arr

    # Divide la lista en mitades
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Aplica recursivamente Mergesort a cada mitad
    left_half = mergesort_asc(left_half, key)
    right_half = mergesort_asc(right_half, key)

    # Combina las mitades ordenadas
    return merge_asc(left_half, right_half, key)

def merge_asc(left, right, key):
    result = []
    left_index, right_index = 0, 0

    # Combina las mitades ordenadas
    while left_index < len(left) and right_index < len(right):
        if left[left_index][key] > right[right_index][key]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Agrega los elementos restantes, si los hay
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def heapsort(arr, key, start, end):
    heap = [(-item[key], item) for item in arr[start:end]]  # Crea un heap máximo utilizando la clave de ordenamiento
    heapq.heapify(heap)

    for i in range(start, end):
        arr[i] = heapq.heappop(heap)[1]  # Extrae los elementos del heap y los asigna a la lista original

        # En cada iteración, extraemos el elemento mínimo (el máximo en valor absoluto) del heap,
        # y lo asignamos a la posición correcta en la lista original.

def shellsort(arr, key):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Inserta el elemento en la posición correcta dentro de su sublista
            while j >= gap and arr[j - gap][key] < temp[key]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

            #  En cada iteración, se inserta el elemento en la posición correcta dentro de su sublista
            # utilizando la técnica de inserción Shell. El gap se va reduciendo hasta llegar a 1, lo que equivale a
            # realizar un algoritmo de inserción estándar.


def dict_menor_a_mayor(lista_diccionarios, clave_ordenamiento):
    # Utiliza el método sorted para ordenar la lista de diccionarios según la clave de ordenamiento
    lista_ordenada = sorted(lista_diccionarios, key=lambda x: x[clave_ordenamiento])

    return lista_ordenada

def dict_mayor_a_menor(lista_diccionarios, clave_ordenamiento):
    # Utiliza el método sorted para ordenar la lista de diccionarios según la clave de ordenamiento
    lista_ordenada = sorted(lista_diccionarios, key=lambda x: x[clave_ordenamiento], reverse=True)
    return lista_ordenada