import requests
import matplotlib.pyplot as plt
from PIL  import Image
from urllib.request import urlopen
import json
"""Libreria requeridas"""


#####
'''Busqueda de pokemon por numero'''
def numero_pokemon(num):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    peticion = requests.get(url + str(num))
    respuesta = json.loads(peticion.content)
    #print(respuesta['name'])
    return respuesta['name']


pokemon = input('Ingresa nombre o numero de pokemon: ')

while not pokemon.isalpha:
    pokemone =numero_pokemon(pokemon)
    pokemon == pokemone
    """Coneste ciclo revisamos el dato ingresado, si se ingreso una cadena, brinca al siguiente
    bloque, si se ingresa un numero se inicia una funcion en la que compara el numero con el 
     erchivo .jason y poder obtener el nombre del pokemon y poder brincar al siguiente bloque """    

url = 'https://pokeapi.co/api/v2/pokemon/'+ pokemon
respuesta = requests.get(url, timeout=10)
"""Se obtiene informacion de la URL"""


if respuesta.status_code != 200:
    print('Pokemon no encontrado')
    exit()# se termina programa
"""Si se obtiene un status.code 200 se continua con el programa de lo contrario terminara el programa"""

datos = respuesta.json()
"""Se genera archivo json"""

numero =  datos[ 'id' ]
nombre = datos[ 'name' ]
tamano = datos[ 'height' ]
Experiencia =  datos[ 'base_experience' ]
peso =  datos[ 'weight' ]
movimientos = datos['moves']
"""Aqui se recolectan los datos generales del pokemon y se almacenan en una variable por dato."""

moves=[]
for i in range(int(len(movimientos))):#con el siclo for enlistaremos los atackes que pikachu puede aprender
    """el for espera indices o claves numericas, por eso se conviete a entero y en diccionario 
    serian de texto  y se puede obtener un erro al iterar """
    movimiento = movimientos[i]['move']['name'] #se referencia en dos corchetes 'move', seguido de 'name' ya qeu es la secuencia de acceder  a la informacion segun la estructura de la API
    moves.append(movimiento)
    #print(f'{i + 1}. {movimiento}')
"""Este ciclo for es para obtener cada un ode lo movimientos de pokemon y almacenarlos en la lista 'moves'"""

with open('pokedex.txt', 'a') as pokedex: #a = append sirve para agregar informacion al final del archivo
     pokedex.write(f'Link de la imagen frontal del {nombre}: {url}')
     pokedex.write(f'\n La informacion general del {nombre} es la siguiente: ')
     pokedex.write(f'\n{datos}')
"""Se genera un archivo de texto y se almacenan los datos generales del pokemon y URL de la imagen frontal"""    

try: 
    url_image = datos['sprites']['front_default'] #para obtener el dato exacto se define los niveles de identacion de donde se iran obteniendo los datos, por eso dos corchetes, primero sprites  y despues front_default segun el caso
    imagen = Image.open(urlopen(url_image))

    #print(url_image)Esta URL debera guardarse en texto
except:
    print('No tiene imagen')
    #exit()
"""Se guarda URL de la imagen frontal del pokemon y con la libreria PIL estraemos la imagen"""

print(f'numero: {numero}')
print(f'nombre: {nombre}')
print(f'peso: {peso}')
print(f'tamano: {tamano}')
for i in range(len(moves)):#con el siclo for enlistaremos los atackes que pikachu puede aprender
    """el for espera indices o claves numericas, por eso se conviete a entero y en diccionario serian de texto
      y se puede obtener un erro al iterar """
    print(f'{i + 1}. {moves[i]}')
"""Se imprimen todos los datos obtenidos del pokemon antes de generar la grafica con la imagen a mostrar"""


  
plt.title(f'{nombre}  (no.{numero})')# se nombra al pokemon en la imagen
plt.xticks([]) # se eliminan los numeros en la imagen
plt.yticks([])
imgplot = plt.imshow(imagen)# se agrega la variable que guardo la url de la imagen
plt.show()
"""Se define los parametros para mostrar la imagen con la libteria 'matplotlib.pyplot' como titulo  imagen 
 y se eliminan los numeros que normalmente se muestran el los ejes 'x' y 'y'"""

    
    



