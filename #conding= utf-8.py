#conding= utf-8 

# Este es un comentario que no se ejecuta 
print("Hola ciudad de Sabaneta") #Aquí hay otro comentario que no se ejecuta
#caracteres:
#simbolos:. = # & $
#cifras: 0 1 2 3 4 5 6 7 8 9
#letras: a b c d e f g h i

print(3.14159)

 #variables: son definiciones de datos que se pueden cambiar
#declarar una variable: Es asignarle el nombre y un valor
#La asisgnación se hace utilizando el símbolo =
#La asignación no es conmutativa. Primero va el nombre y luego el valor
una_frase = "Hola ciudad de Medellín"
numero_pi = 3.14159
p = 3.14159

otrafrase = 'Aqui vivi en nombre que se le da a un dato'

#concatenamos varias frases en una sola instrución
print(una_frase+ '\n' +otrafrase)


print('El valor de pi es: ' '\n' + str(numero_pi))

frase3 = 'Esta es la tecera frase'

un_numero = 3
print(un_numero)
print(type(un_numero))

#Aqui reutilizamos la variable un_numero para generar una nueva variable
##El tipo, asignandole un valor de tipo flotante
un_numero = 8.654
print(un_numero)
print(type(un_numero))


#Operadores matematicos
suma = 3 + 8
resta= 15 - 7 
multiplicacion= 12 / 2
division_entera = 12 // 5
raiz_cuadrada = 5 ** 0.5
raiz_cubica = 27** (1/3)


print( 'El resultado de la suma es: ' + str(suma))
print(type(suma))
print( 'El resultado de la resta es: ' + str(resta))
print(type(resta))
print( 'El resultado de la multiplicacion es: ' + str(multiplicacion))
print(type(multiplicacion))
print( 'El resultado de la division entera es: ' + str(division_entera))
print(type(division_entera))
print('El resultado de la raiz cuadrada es: ' + str(raiz_cuadrada))
print(type(raiz_cuadrada))
print('El resultado de la raiz cubica es: ' + str(raiz_cubica))
print(type(raiz_cubica))


operacion_muy_larga = (2+3) * 5 / 2
print(operacion_muy_larga)


nombre= input( 'cual es tu nombre' )
print('Hola' + nombre)
