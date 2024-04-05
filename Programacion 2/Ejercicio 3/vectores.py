#1.Declarar una lista vacía
lista_vacia = []

#2.Declarar una lista con más de 5 elementos
lista = ['a', 'b', 'c', 'd', 'e', 'f']

#3.Encuentre la longitud de las dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista = len(lista)

#4.Obtener el primer elemento, el elemento central y el último elemento de la lista.
primer_elemento = lista[0]
elemento_central = lista[len(lista)//2]
ultimo_elemento = lista[-1]

#5.crear una lista llamada Datos_personales que contenga (nombre, edad, altura, estado civil, dirección), y agrega datos utilizando la funcion append().
Datos_personales = []
Datos_personales.append('nombre')
Datos_personales.append('edad')
Datos_personales.append('altura')
Datos_personales.append('estado civil')
Datos_personales.append('dirección')

#6.Crea una lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7.Añadir una empresa a la lista it_companies utilizando la funcion insert().
it_companies.insert(0, 'EmpresaX')

#8.Comprobar si una determinada empresa existe en la lista it_companies.
empresa = 'EmpresaX'
if empresa in it_companies:
    print(f'{empresa} existe en la lista it_companies.')
else:
    print(f'{empresa} no existe en la lista it_companies.')

#9.Ordena la lista con el método sort()
it_companies.sort()

#10.Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()

#11.Elimine la primera empresa informática de la lista utilizando el metodo pop y delete.
it_companies.pop(0)
del it_companies[0]

#12.Eliminar todas las empresas de la lista it_companies
it_companies.clear()
