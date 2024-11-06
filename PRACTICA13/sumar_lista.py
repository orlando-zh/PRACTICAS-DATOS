def sum_lista (lista):
    if len(lista) == 0:
        return 0
    else:
        return lista [0] + sum_lista(lista[1:])
    

print(sum_lista([1, 2, 3, 4, 5]))
