#Proyecto:Thundercats
#Integrantes:
# - Manuel Riascos Tovar
# - Ana Sofía Guerrero
# Idea: Dijkstra (uno a todos)

from heapq import heappush, heappop

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



