
# Dada una cadena pon los caracteres con índice par al principio y con índice
# impar después separador por un guion. Ejemplo "ABCDEF" debe dar "ACE-BDF"

c = "ABCDEF"

print('-'.join([c[::2],c[1::2]]))

# Primera letra a mayúscula y resto en minúsculas

c="HOLA"
#print(c.lower().replace(c[0],c[0].upper())) no funciona si la inicial de c ya es mayuscula

print(c[0].upper()+c[1:].lower())


# Cambiar espacios por _ y poner en minúsculas la extensión
# Suponer que la extensión tiene 3 caracteres

fichero = 'Foto de vacaciones.JPG'

print(fichero.replace(' ','_')[:-3]+fichero[-3:].lower())

# Combina join y split para que devuelva exactamente la misma cadena original

sep="-"

c="A-B-C-D-E-F"

list=c.split(sep)
print(sep.join(list))

# rodea la cadena c con > por la izquierda y < por la derecha hasta 
#  un total de 80 caracteres
c = "rellenar"

print(c.rjust(80-len(c),">").ljust(80,"<"))