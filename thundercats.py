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




