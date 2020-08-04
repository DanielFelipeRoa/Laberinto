from turtle import TurtleScreen, RawTurtle, TK
from time import sleep

class Ventana():


    def __init__(self, titulo, alto, ancho):

        assert isinstance(titulo, str)
        assert isinstance(alto, int) and alto > 0
        assert isinstance(ancho, int) and ancho > 0

        self.root = TK.Tk()
        self.root.title(titulo)
        self.canvas = TK.Canvas(self.root, width=ancho, height=alto)
        self.canvas.pack()

        self.fondo_ventana = TurtleScreen(self.canvas)
        self.fondo_ventana.setworldcoordinates(0, alto, ancho, 0)

        self.canvas["bg"] = "gold"
        self.canvas.pack()

        self.pencil = RawTurtle(self.fondo_ventana)
        self.pencil.pencolor("white")

class Laberinto():

    Xdis = 10
    Ydis = 10

    Alto = 25
    Ancho= 25

    @staticmethod
    def deme_posicion(i, j):
        x = Laberinto.Xdis + j * (Laberinto.Ancho + 1)
        y = Laberinto.Ydis + i * (Laberinto.Alto  + 1)
        return (x, y)


    def __init__(self, area_dibujo, laberinto):

        lista = laberinto.split()
        lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
        lista = [[int(ch) for ch in x] for x in lista]

        self.laberinto = lista
        self.lienzo = area_dibujo

        self.dibuja_laberinto()

    def dibuja_laberinto(self):

        self.lienzo.fondo_ventana.tracer(False)
        self.lienzo.pencil.pencolor("white")

        for i in range(len(self.laberinto)):

            for j in range(len(self.laberinto[i])):

                if self.laberinto[i][j] == 1:
                    self.casilla("black", i, j)
                elif self.laberinto[i][j] == 3:
                    self.casilla("red", i, j)
                elif self.laberinto[i][j] == 0:
                    self.casilla("white", i, j)

        self.lienzo.fondo_ventana.tracer(True)

    def casilla(self, color, i, j):

        x, y = Laberinto.deme_posicion(i, j)

        self.lienzo.pencil.fillcolor(color)
        self.lienzo.pencil.pu()
        self.lienzo.pencil.setpos(x, y)
        self.lienzo.pencil.seth(0)
        self.lienzo.pencil.pd()
        self.lienzo.pencil.begin_fill()

        for i in range(2):
            self.lienzo.pencil.fd(Laberinto.Ancho+1)
            self.lienzo.pencil.left(90)
            self.lienzo.pencil.fd(Laberinto.Alto+1)
            self.lienzo.pencil.left(90)

        self.lienzo.pencil.end_fill()

    def dibujar(self, sol):


        sleep(1)
        self.lienzo.fondo_ventana.tracer(False)
        for i in range(len(sol)):
            x = int(sol[i][0])
            y = int(sol[i][1])
            sleep(0.05)
            self.casilla("darkgreen", x,y)
            self.lienzo.fondo_ventana.tracer(True)
        sleep(3)

def principal(dibujo, sol):
    ll = Laberinto(Ventana("Laberinto", 255, 235), dibujo)
    ll.dibujar(sol)