#punto 1
perro={}

#punto 2
perro={'nombre':'caleb',
       'color':'marron',
       'raza':'labrador',
       'patas':'4',
       'edad':'3',
    }

#punto 3
estudiantes={'nombre':'kleiver',
             'apellido':'fajardo',
             'sexo':'masculino',
             'edad':'21',
             'estado civil':'soltero',
             'habilidades':['buen deportista','guapo'],
             'pais':'colombia',
             'direccion':['12345', '6789','2468']}

#punto 4
print(len(estudiantes))

#punto 5

print(estudiantes.get('habilidades'))
print(type(estudiantes['habilidades']))

#punto 6
habilidades1=input("ingrese habilidad: ")
estudiantes['habilidades'].append(habilidades1)

#punto 7
print(estudiantes.keys())

#punto 8
print(perro.values())
print(estudiantes.values())

#punto 9
print(estudiantes.items())

#punto 10
del estudiantes['estado civil']
print(estudiantes)

#punto 11
del estudiantes