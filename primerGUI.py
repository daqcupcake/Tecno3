import tkinter as tk

#variables
cont=0

root=tk.Tk()
root.title("El Primer GUI")
root.geometry("800x800")



def clickBtnPulsar():
    global cont
    nombre=txtEntrada.get()
    cont+=1
    if cont!=1:
        la2.config(text=f"{nombre} ha presionado el botón {cont} veces",bg="#325931")
    else:
        la2.config(text=f"{nombre} ha presionado el botón {cont} vez",bg="#325931")
    

#crear label (etiqueta)
la1=tk.Label(root,text="etiqueta 1")
la2=tk.Label(root,text="etiqueta 2")
btnPulsar=tk.Button(root,text="Pulsar",width="6",height="3",command=clickBtnPulsar)
txtEntrada=tk.Entry(root,width=50, font=("Arial",12))
txtEntrada.insert(0,"Ingrese su nombre")
#para pasar parametros: command= lamda: funcion("parametro")



#colocar a como caiga
#la1.pack()

#colocar en un grid
la1.grid(row=3,column=4)
la2.grid(row=1,column=1)
btnPulsar.grid(row=2,column=2)
txtEntrada.place(x=100,y=53)

#Loop para que se ejecute
root.mainloop()
