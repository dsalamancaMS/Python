
#list
lista_x = ["c", "d", "a", "b"]


#arregla la lista en orden, sobreescribe la lista
lista_x.sort()

#imprime los valores en indice impar, empieza en 1 y sigue de 2 en 2
print(lista_x[1::2])

lista_x.append("h")

#remueve solo la primera ocurrencia
lista_x.remove("a")


print(lista_x)

#consult if value is in list
print("e" in lista_x)

#comparador booleano
print(True is False)

#checks if elements on list are true
print(all([True,True]))
print(all([True,False]))

#checks if there is ANY true element
print(any([True,False]))

#None is Null
None



list_lista = [ "hola", "adios", lista_x]

list_lista[-1].append("soy nuevo")

print(list_lista)