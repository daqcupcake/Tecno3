from tkinter import *


def creaVentana2(vent1):
    #root = Tk()
    ventana2=Toplevel(vent1)
    #root.geometry("400x100")
    ventana2.geometry("400x100")
    ventana2.title("Áreas")
    
    ventana2.lblArea = Label(ventana2,text ="")
    ventana2.lblArea.grid(row=0,column=2)
    
    def calculo_area():
        if ventana2.txtLado.get():
            lado=float(ventana2.txtLado.get())
            area=lado*lado
            ventana2.lblArea.config(text=f"El área del cuadrado es {area}")
        else:
           lblArea.config(text="Ingrese un valor") 
    
    ventana2.lblLado = Label(ventana2, text ="Medida del lado del cuadrado")
    ventana2.lblLado.grid(row=0,column=0)
    ventana2.txtLado = Entry(ventana2,width=10)
    ventana2.txtLado.grid(row=0,column=1)
            
    ventana2.boton_volver = Button(ventana2, text="Menú Principal",command=lambda:volverArchivo01(ventana2,vent1))
    ventana2.boton_volver.grid(row=1,column=0)
            
    ventana2.boton_calcular = Button(ventana2, text="Calcular", command=calculo_area)
    ventana2.boton_calcular.grid(row=1,column=1,pady=20)
    ventana2.protocol("WM_DELETE_WINDOW",lambda: volverArchivo01(ventana2, vent1))
    
    #root.mainloop()
    def volverArchivo01(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()


