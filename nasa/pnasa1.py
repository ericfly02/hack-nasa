import time
import threading
from pyfiglet import Figlet
from tqdm.auto import tqdm


#Introducir contraseña para acceder al sistema de la nasa
answer = input("Estas apunto de entrar en los sistemas de la nasa, estas seguro  [si / no]?")

if answer == "si":

   answer = input ("CONTRASEÑA, aqui tienes una pista (∫2x dx)")
   if answer == "x^2+c":

   	answer == input ('a cuanto equivale sin(2x)? ')
   	if answer == "cos^2x-sin^2x":
   	
   		print('CREDENCIALES OBTENIDAS CORRECTAMENTE')
   	
   	

   else:
   	print("pruebalo otra vez")

   


if answer == 'no':
   time.sleep(0)



#BANNER

custom_fig = Figlet(font='starwars')
print(custom_fig.renderText('HACKING  NASA'))


for i in tqdm(range(10000000)):
   print("Thespeedy02", end='\r')


   def hacked():
     for i in range(1):
        time.sleep(0.001)
        print('CREDENCIALES OBTENIDAS CORRECTAMENTE')

 


custom_fig = Figlet(font='starwars')
print(custom_fig.renderText('by The Speedy02'))


t101 = threading.Thread(target=hacked)


t101.start()