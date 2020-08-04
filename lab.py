from pyswip import Prolog
from laberinto import principal

def lectura_archivo(archivo):
	c = [line.splitlines() for line in (open(archivo, "r"))]
	c = [i[0].split() for i in c]
	return c

def start(mapa,cont):
	if mapa == []: return (-1,-1)
	if "i" in mapa[0]: return ([cont,mapa[0].index("i")])
	return start(mapa[1:],cont+1)


def buscando(x, y, lab):
  if lab[x][y] == 'f':
      camino.append(['f'])
      return True
  elif lab[x][y] == '|':  return False
  elif lab[x][y] == '-':  return False
  elif lab[x][y] == '--': return False
  elif lab[x][y] == 'o':  return False
  else: camino.append([lab[x][y]])
  lab[x][y] = 'o'

  if ((x < len(lab)-1 and buscando(x+1, y,lab)) or
  	(y > 0 and buscando(x, y-1,lab)) or
  	(x > 0 and buscando(x-1, y,lab)) or
  	(y < len(lab[0])-1 and buscando(x, y+1,lab))):
    return True
  return False

def encontrar(lista, lab):
  if(buscando(lista[0], lista[1], lab)): return True
  return False

def assert_intento(camino):
  for x in range(0 , len(camino) - 1):
    p.assertz("conecta("+camino[x][0]+","+camino[x+1][0]+")")

def solu(camino):
  s = []
  aux =[]

  for x in range(0 , len(camino)):
    for j in range(0 , len(camino[x]) ):
      if (camino[x][j] == 'o' or camino[x][j] == 'f'):

        aux = [str(x),str(j)]
        s.append(aux)

  return s

def solucion():
	solucion = []
	for r in p.query("camino([i],Sol)"):
		for j in r["Sol"]:
			solucion += [j]
		break
	solucion[-1] = 'i'
	solucion[0] = 'f'
	return solucion



p = Prolog()
p.consult('laberinto.pl')

lab = lectura_archivo("laberinto1.txt")  


dibujo = ''                     

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if (lab[i][j] == '|' or lab[i][j] ==  '--') : dibujo += '1'
        elif lab[i][j] == 'f': dibujo+= '3'
        else : dibujo += '0'
    dibujo += '\n'



camino = []
encontrar(start(lab,0),lab) 


while (['0'] in camino): camino.remove(['0']) 

assert_intento(list(camino))       

sol = solucion()[::-1] 

print(sol)

principal(dibujo,solu(list(lab))) 
