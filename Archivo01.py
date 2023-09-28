from tkinter import *

from Archivo02 import creaVentana2

class Ventana1(Tk):
    
#root = Tk() se sustituye por el Tk de la clase
    def __init__(self):
        super().__init__()  #define que esta es la ventana principal
        
        #root.geometry("300x100")
        self.geometry("300x100")
        
        #root.title("Cuadrados")
        self.title("Cuadrados")
        
        """
        boton_mostrar = Button(root, text="Cálculo del área")
        boton_mostrar.place(x=50,y=50)
                
        lblMensaje = Label(root, text ="Menú principal: Cuadrados")
        lblMensaje.place(x=40,y=20)
        """
        self.boton_mostrar = Button(self, text="Cálculo del área",command=self.mostrarVentana2)
        self.boton_mostrar.place(x=50,y=50)
                
        self.lblMensaje = Label(self, text ="Menú principal: Cuadrados")
        self.lblMensaje.place(x=40,y=20)
        
    def mostrarVentana2(self):
        self.withdraw()
        creaVentana2(self)
        


if __name__=="__main__":
    app=Ventana1()
    app.mainloop()
    
    #root.mainloop()
