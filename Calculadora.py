import tkinter as tk

root=tk.Tk()
root.title("Calculadora")
root.geometry("800x800")

marco=tk.Frame(root,bg="red",bd=10)
#Define 
pantalla=tk.Entry(marco,width="30")

btn00=tk.Button(marco,text="0",width="5",height="2")
btn01=tk.Button(marco,text="1",width="5",height="2")
btn02=tk.Button(marco,text="2",width="5",height="2")
btn03=tk.Button(marco,text="3",width="5",height="2")
btn04=tk.Button(marco,text="4",width="5",height="2")
btn05=tk.Button(marco,text="5",width="5",height="2")
btn06=tk.Button(marco,text="6",width="5",height="2")
btn07=tk.Button(marco,text="7",width="5",height="2")
btn08=tk.Button(marco,text="8",width="5",height="2")
btn09=tk.Button(marco,text="9",width="5",height="2") 

btnDiv=tk.Button(marco,text="÷",width="5",height="2")
btnMul=tk.Button(marco,text="×",width="5",height="2")
btnRes=tk.Button(marco,text="-",width="5",height="2")
btnSum=tk.Button(marco,text="+",width="5",height="2")
btnDot=tk.Button(marco,text=".",width="5",height="2")
btnEq=tk.Button(marco,text="=",width="5",height="2")


#Colocar
marco.grid(row=5,column=5)

pantalla.grid(row=0,column=0,columnspan=4)

btn07.grid(row=1,column=0)
btn08.grid(row=1,column=1)
btn09.grid(row=1,column=2)

btnDiv.grid(row=1,column=3)


btn04.grid(row=2,column=0)
btn05.grid(row=2,column=1)
btn06.grid(row=2,column=2)

btnMul.grid(row=2,column=3)


btn01.grid(row=3,column=0)
btn02.grid(row=3,column=1)
btn03.grid(row=3,column=2)

btnRes.grid(row=3,column=3)


btn00.grid(row=4,column=0)

btnDot.grid(row=4,column=1)
btnEq.grid(row=4,column=2)
btnSum.grid(row=4,column=3)


#Loop para que se ejecute
root.mainloop()