import tkinter as tk

root=tk.Tk()
root.title("Catculator")
root.geometry("300x400")


fondo = tk.PhotoImage(file="BaseCatCalc.png")
labelFondo = tk.Label(root,image=fondo)

#Define 
marco=tk.Frame(root,bg="#ffcfdc",bd=0,height=280,width=250)

pantalla=tk.Entry(marco,width="19",font=("Arial",20))

#variables globales
num1=None
num2=None
operacion=None
reset=False
#funciones botones

    

def clickNum (num): #recibe un numero 

    
    
    global reset
    
    if reset:
            pantalla.delete(0,tk.END) #o "end" en lugar de END
            reset=False
    pantalla.insert(tk.END, str(num))

def clickOp (op):
    global num1,num2,operacion
    
    if pantalla.get():
        if num1 is None:
                num1=float(pantalla.get())
        
        else:
            num2=float(pantalla.get())
            num1=hacerCalculo()
            num2=None
        
    
        
    operacion=op
    pantalla.delete(0,tk.END)

def hacerCalculo():
    global num1,num2, reset
    if operacion=="+":
        resultado=num1+num2
        
    elif operacion=="-":
        resultado=num1-num2
    
    elif operacion=="x":
        resultado=num1*num2
        
    elif operacion=="/":
        if num2!=0:
            resultado=num1/num2
        else:
            resultado="error"
    else:
        pass           

    return resultado

def clickIgual():
    global num2, reset
    num2=float(pantalla.get())
    pantalla.delete(0,tk.END)
    resultado=None
   
    
    if operacion=="+":
        resultado=num1+num2
        
    elif operacion=="-":
        resultado=num1-num2
    
    elif operacion=="x":
        resultado=num1*num2
        
    elif operacion=="/":
        if num2!=0:
            resultado=num1/num2
        else:
            resultado="error"
    else:
        pass
    
    pantalla.insert(0,str(resultado))
    reset=True
    
btn00=tk.Button(marco,text="0",width="5",height="2",bg="#ffccda",command=lambda:clickNum(0))
btn01=tk.Button(marco,text="1",width="5",height="2",bg="#ffccda",command=lambda:clickNum(1))
btn02=tk.Button(marco,text="2",width="5",height="2",bg="#ffccda",command=lambda:clickNum(2))
btn03=tk.Button(marco,text="3",width="5",height="2",bg="#ffccda",command=lambda:clickNum(3))
btn04=tk.Button(marco,text="4",width="5",height="2",bg="#ffccda",command=lambda:clickNum(4))
btn05=tk.Button(marco,text="5",width="5",height="2",bg="#ffccda",command=lambda:clickNum(5))
btn06=tk.Button(marco,text="6",width="5",height="2",bg="#ffccda",command=lambda:clickNum(6))
btn07=tk.Button(marco,text="7",width="5",height="2",bg="#ffccda",command=lambda:clickNum(7))
btn08=tk.Button(marco,text="8",width="5",height="2",bg="#ffccda",command=lambda:clickNum(8))
btn09=tk.Button(marco,text="9",width="5",height="2",bg="#ffccda",command=lambda:clickNum(9)) 

btnDiv=tk.Button(marco,text="÷",width="5",height="2",bg="#ff80a2",command=lambda:clickOp("/"))
btnMul=tk.Button(marco,text="×",width="5",height="2",bg="#ff80a2",command=lambda:clickOp("x"))
btnRes=tk.Button(marco,text="-",width="5",height="2",bg="#ff80a2",command=lambda:clickOp("-"))
btnSum=tk.Button(marco,text="+",width="5",height="2",bg="#ff80a2",command=lambda:clickOp("+"))
btnDot=tk.Button(marco,text=".",width="5",height="2",bg="#ff80a2",command=lambda:clickNum("."))
btnEq=tk.Button(marco,text="=",width="5",height="2",bg="#ff80a2",command=clickIgual)


#Colocar

labelFondo.place(x=0,y=0)
marco.place(x=25,y=85)


pantalla.place(x=0,y=10)

btn07.place(x=10,y=60)
btn08.place(x=70,y=60)
btn09.place(x=130,y=60)

btnDiv.place(x=190,y=60)


btn04.place(x=10,y=110)
btn05.place(x=70,y=110)
btn06.place(x=130,y=110)

btnMul.place(x=190,y=110)


btn01.place(x=10,y=160)
btn02.place(x=70,y=160)
btn03.place(x=130,y=160)

btnRes.place(x=190,y=160)


btn00.place(x=10,y=210)

btnDot.place(x=70,y=210)
btnEq.place(x=130,y=210)
btnSum.place(x=190,y=210)


#Loop para que se ejecute
root.mainloop()