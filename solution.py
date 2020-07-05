import numpy as np

tablero = np.zeros((8,8))

posicion = [0,1]

"""registros

  registros[i][0] = num movimientos
  registros[i][1] = num mov
  registros[i][2] = pos x
  registros[i][3] = pos y

"""
registros = np.array([[1,0,posicion[0],posicion[1]]])


tablero[posicion[0],posicion[1]] = 1
  

def mov1(posicion):
    nueva_ = []
    nueva_.append(posicion[0] + 2)
    nueva_.append(posicion[1] + 1)
    return nueva_
  

def mov2(posicion):
    nueva_ = []
    nueva_.append(posicion[0] + 2)
    nueva_.append(posicion[1] - 1)
    return nueva_
  

def mov3(posicion):
    nueva_ = []
    nueva_.append(posicion[0] - 1)
    nueva_.append(posicion[1] + 2)
    return nueva_
  

def mov4(posicion):
    nueva_ = []
    nueva_.append(posicion[0] + 1)
    nueva_.append(posicion[1] + 2)
    return nueva_
  

def mov5(posicion):
    nueva_ = []
    nueva_.append(posicion[0] - 1)
    nueva_.append(posicion[1] - 2)
    return nueva_
  

def mov6(posicion):
    nueva_ = []
    nueva_.append(posicion[0] + 1)
    nueva_.append(posicion[1] - 2)
    return nueva_
  

def mov7(posicion):
    nueva_ = []
    nueva_.append(posicion[0] - 2)
    nueva_.append(posicion[1] - 1)
    return nueva_
  

def mov8(posicion):
    nueva_ = []
    nueva_.append(posicion[0] - 2)
    nueva_.append(posicion[1] + 1)
    return nueva_

def actualizar_tablero(tablero,posicion,num):
    tablero[posicion[0]][posicion[1]] = num
    return tablero


movimientos = [mov1,mov2,mov3,mov4,mov5,mov6,mov7,mov8]


while(1):
    #cada itineración hace un movimiento ya sea hacer otro o retroceder.
    ultimo = int( registros.size/4 -1)

    if (registros[ultimo][1] < 8):

        #calculo la nueva posicion
        nueva_posicion = movimientos[registros[ultimo][1]](posicion)

        if(nueva_posicion[0] < 0 or nueva_posicion[1] < 0 or nueva_posicion[0] > 7 or nueva_posicion[1] > 7):
            registros[ultimo][1] += 1
        elif(tablero[nueva_posicion[0]][nueva_posicion[1]] != 0):
            registros[ultimo][1] += 1
        else:
            tablero = actualizar_tablero(tablero,nueva_posicion,ultimo+2)
            nuevo = np.array([[ultimo+2,0,nueva_posicion[0],nueva_posicion[1]]])
            registros = np.append(registros, nuevo, axis=0)

            posicion[0] = nueva_posicion[0]
            posicion[1] = nueva_posicion[1]
      
    else:
        tablero = actualizar_tablero(tablero,posicion,0)
        registros = np.delete(registros, ultimo, 0)
        registros[ultimo-1][1] += 1
        posicion[0] = registros[ultimo-1][2]
        posicion[1] = registros[ultimo-1][3]
    
    if(len(registros) == 64):
        break

#Se rellena la solución en el tablero
print(tablero)


