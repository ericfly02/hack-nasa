#! /bin/python3

#Print string
print('strings and things')
print("""Hello this is a multi-line string!""")
print('this is '+' a string')


print ('\n')  #new line


# MATH
print('Math time:')
print(50 +50) #suma
print(50 - 50) #resta
print(50 * 50) #multiplicar
print (50 / 50) #dividir
print (50 + 50 - 50 * 50 / 50) #Compuesta
print (50 ** 2) #exponentes
print (50 % 6) #modulo
print (50 // 50) #number without left over



#VARIABLES & METHODS
print('Fun with variables and methods:')
quote = 'A Eric le gustan las montayas'
print(len(quote)) #longitud
print(quote.upper()) #Mayuscula
print(quote.lower()) #Minuscula
print(quote.title()) #Titulo


nombre = 'Eric'
edad = 18 #int int(18)
gpa = 8 #float float(8)

print(int(edad))
print(int(1))


print(' Mi nombre es ' + nombre + ' I tengo ' + str(edad) + ' anyos ')

print ('\n')  #new line

edad += 1
print(edad)

cumple = 1
edad += cumple
print(edad)

print ('\n')  #new line

#FUNCTIONS
print('Ahora unas funciones:')
def quien_soy():
       nombre = 'eric'
       edad = 18
       print('Mi nombre es' + nombre + 'I tengo' + str(edad) + 'anyos')

quien_soy()
 
 
 
 #adding in parameters
 
 		#def add_one_hundred(num) :
 			#print(num + 100)
 
 		#add_one_hundred(100)
 
 #add in multiple parameters
 
def add (x,y): 
 	print(x + y)
 
add(7,7)
add(9,9)
 
 #Using Return
			#def multiply(x,y):
 				#return x * y
 	
 	
				#print(multiply)
  
			#def square_toot(x):
  				#return x ** .5
  	
				#print(square_root(64)
	
	
print ('\n')  #new line

#Boolean expressions (True or False)

print('Boolean Expressions')

bool1 = True
bool2 = 3*3 == 9
bool3 = False 
bool4 = 3*3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = 'True'
print(type(bool5))

#Relational and Boolian Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print (greater_than, less_than_equal_to, greater_than_equal_to, less_than)

test_and = (7 > 5) and (8 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = True

print(test_and)



print ('\n')  #new line

#Conditional Statements
print('conditional Statements:')
def cocacola(money):

	if money >= 2:
		return 'Tienes una cocacola!'

	else:
		return 'No tienes cocacola!'


print (cocacola(0))
print (cocacola(1))


def lapiz(dinero):
	if dinero >= 2:
		return 'key'

	else :
		return 'nop'

print (lapiz(1))
print (lapiz(34))


print ('\n')  #new line

def alcohol(edad, dinero):
	if (edad >= 18) and (dinero >= 5):
		return 'Tienes Fiesta esta noche guapeton'

	elif (edad >= 21) and (dinero <= 5):
		return 'Necesitas mas money guapeton'

	elif (edad <= 21) and (dinero >= 5):
		return 'bien provado chaval'

	else:
		return 'eres pobre y no tienes la edad guapeton'


print (alcohol(21,5))
print (alcohol(21,4))
print (alcohol(20,4))



print ('\n')  #new line

#Lists
print('Lists have brackets:')

peliculas = ('1970', 'El lobo de wall street', 'Una mariposa', 'el hoyo')

print (peliculas[0])
print (peliculas[1])
print (peliculas[2])
print (peliculas[3])


print (peliculas[0:2]) #Toda la lista del 0 hasta el 2

print (peliculas[1:])  #Toda la lista apartir del 1

print (peliculas[:1])  #Toda la lista del 0 hasta el 1

print (peliculas[-1])  #pelicula anterior a la 1

print (len(peliculas))  #Numero de peliculas en la lista

#peliculas.append ['la fabrica de chocolate']
#print(peliculas)

#peliculas.pop()
#print(peliculas)

#peliculas.pop(1)
#print(peliculas)

peliculas = ['1970', 'El lobo de wall street', 'Una mariposa', 'el hoyo'] 

persona = ['jake', 'Pol', 'juan', 'Marc']
combinado = zip(peliculas, persona)
print(list(combinado))


print ('\n')  #new line



#Tuples
print('Tuples tienen parentesis i no se pueden cambiar')
grades = ('A', 'B', 'C', 'D', 'F')
print(grades[1])


print ('\n')  #new line


#Looping
print('For loops - start to finish of iterate')
vegetales = ['espinacas', 'cogombre', 'ensalada']
for x in vegetales:
	print (x)

print ('while loops - Solo se ejecuta cuando sea verdad:')
i = 1
while i < 10:
	print(i)
	i += 1          #Mientras sea verdad, habra alguna cosa

	





































