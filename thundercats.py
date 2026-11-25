#Proyecto:Thundercats
#Integrantes:
# - Manuel Riascos Tovar
# - Ana Sofía Guerrero
# Idea: Dijkstra (uno a todos)

from heapq import heappush, heappop
INF=float('inf')

def dijkstra(G, nodoInicial, dist):
  #el nodo de inicio esta a distancia 0
  dist[nodoInicial]= 0
  pqueue= list() #cola de prioridad para elegir el nodo de menor distancia
  heappush(pqueue, (dist[nodoInicial],nodoInicial))

  while len(pqueue) != 0: #si quedan nodos
    du, u =heappop(pqueue) #la menor distancia sale
    #si no es la menor distancia
    if dist[u]== du:
      for v, duv in G[u]:
        if du+duv < dist[v]: #si mejora
          dist[v]= du+duv
          heappush(pqueue, (dist[v], v)) #nueva distancia para v

#Para ver si Lion-O puede llegar a una salida a velocidad que lleva Lion-O
def sipuedeEscapar(G, inicioLion, esSalida, distMutantes, velMutantes, velLion, logroEscapar):
  logroEscapar[0] = False #no ha escapado
  # si es 0 los mutantes estan ahi
  if distMutantes[inicioLion] > 0:
    distLion=[INF for _ in range(len(G))] #la distancia de Lion a cada nodo
    distLion[inicioLion]= 0
    pqueue = list() #cola de prioridad para el nodo mas cerca a Lion-O
    heappush(pqueue,(distLion[inicioLion], inicioLion))

    while len(pqueue) != 0 and not logroEscapar[0]: #si la cola esta vacia
      du,u = heappop(pqueue) #la de menor distancia
      if distLion[u] == du:
        tiempoLionU= (du * 0.1) /velLion #tiempo de Lion hasta u
        tiempoMutantesU= (distMutantes[u] * 0.1)/velMutantes#tiempo de los mutantes hasta u

        if esSalida[u]== 1 and tiempoLionU<tiempoMutantesU: #salida a la que llega antes que los mutantes
          logroEscapar[0] = True
        else:
          #los vecinos de u y la longitud
          for v, duv in G[u]:
            nuevaDist= du +duv #distancia de Lio a v y pasa por u
            tiempoLionV= (nuevaDist * 0.1) / velLion
            tiempoMutantesV = (distMutantes[v] * 0.1) / velMutantes

            #avanza si llega antes que los mutantes y si es menor q la distancia 
            if tiempoLionV <tiempoMutantesV and nuevaDist<distLion[v]:
              distLion[v]= nuevaDist #relajación mejor distancia a v
              heappush(pqueue, (distLion[v], v))
#Búsqueda binaria para la velocidad minima de Lion-O
def busquedaVelocidad(G, inicioLion, esSalida, distMutantes, velMutantes, velMin, velMax, eps, velMinima):
  if velMax-velMin > eps: #si estan lejos se sigue buscando
    velMedia= (velMin+velMax)/ 2.0 #la velocidad del medio
    logroEscapar=[False]
    #si Lion puede escapar a esa velocidad media 
    sipuedeEscapar(G, inicioLion, esSalida, distMutantes, velMutantes, velMedia, logroEscapar)
    
    if logroEscapar[0]:
      velMinima[0]= velMedia #si escapa se guarda la velocidad minima
      #si escapa con la velocidad media, entonces esta entre la velocidad minima y la media
      busquedaVelocidad(G, inicioLion, esSalida, distMutantes, velMutantes, velMin, velMedia, eps, velMinima)
    else:
      #si no escapó, entonces mira con una velocidad mas rápida entre velMedia y velMax
      busquedaVelocidad(G, inicioLion, esSalida, distMutantes, velMutantes, velMedia, velMax, eps, velMinima)

#Una prueba
def verPruebas(G, inicioLion, inicioMutantes, esSalida, velMutantes):
  #si empiezan en el mismo nodo, los mutantes atrapan a Lion-O de una
  if inicioLion==inicioMutantes:
    print("Mumm-Ra captures Lion-O!")
  else:
    
    distMutantes = [INF for _ in range(len(G))]#la distancia de los mutantes a cada nodo
    dijkstra(G, inicioMutantes, distMutantes)

    velMin=0.0 #velocidad mínima de Lion-O
    velMax = 1e9 #velocidad máxima de Lion-O

    #prueba con la velocidad más alta
    logroEscapar= [False]
    sipuedeEscapar(G, inicioLion, esSalida, distMutantes, velMutantes, velMax, logroEscapar)

    if not logroEscapar[0]:
      #ni con la velocidad más alta escapa
      print("Mumm-Ra captures Lion-O!")
    else:
      #sí escap busca la velocidad más baja con la que todavía escapa
      velMinima= [velMax]
      busquedaVelocidad(G, inicioLion, esSalida, distMutantes, velMutantes, velMin, velMax, 1e-7, velMinima)
      print(f"Lion-O can escape at a speed of {velMinima[0]:.6f} km/h!")  #:.6f imprime los 6 decimales 

def main():
  pruebas= int(stdin.readline())
  for _ in range(pruebas):
    #lee el primer caso de cada linea
    nodos, carreteras, numSalidas, velMutantes= map(int, stdin.readline().split())

    #En G[u] guarda los vecinos de u con la longitud 
    G= [[] for _ in range(nodos + 1)]

    for _ in range(carreteras): #las carreteras, agrega las aristas en los dos sentidos    
      nodo1, nodo2, longitud= map(int, stdin.readline().split()) #lee los dos extremos de la carretera y su longitud                                             
      G[nodo1].append((nodo2, longitud)) #desde el nodo1 se puede llegar al nodo2
      G[nodo2].append((nodo1, longitud)) #y desde el nodo2 se puede llegar al nodo1
