import tkinter as tk

root=tk.Tk()
root.title("Catculator")
root.geometry("300x400")


fondo = tk.PhotoImage(file="BaseCatCalc.png")
labelFondo = tk.Label(root,image=fondo)

#Define 
marco=tk.Frame(root,bg="#ffcfdc",bd=0,height=280,width=250)

pantalla=tk.Entry(marco,width="19",font=("Arial",20))



btn00=tk.Button(marco,text="0",width="5",height="2",bg="#ffccda")
btn01=tk.Button(marco,text="1",width="5",height="2",bg="#ffccda")
btn02=tk.Button(marco,text="2",width="5",height="2",bg="#ffccda")
btn03=tk.Button(marco,text="3",width="5",height="2",bg="#ffccda")
btn04=tk.Button(marco,text="4",width="5",height="2",bg="#ffccda")
btn05=tk.Button(marco,text="5",width="5",height="2",bg="#ffccda")
btn06=tk.Button(marco,text="6",width="5",height="2",bg="#ffccda")
btn07=tk.Button(marco,text="7",width="5",height="2",bg="#ffccda")
btn08=tk.Button(marco,text="8",width="5",height="2",bg="#ffccda")
btn09=tk.Button(marco,text="9",width="5",height="2",bg="#ffccda") 

btnDiv=tk.Button(marco,text="÷",width="5",height="2",bg="#ff80a2")
btnMul=tk.Button(marco,text="×",width="5",height="2",bg="#ff80a2")
btnRes=tk.Button(marco,text="-",width="5",height="2",bg="#ff80a2")
btnSum=tk.Button(marco,text="+",width="5",height="2",bg="#ff80a2")
btnDot=tk.Button(marco,text=".",width="5",height="2",bg="#ff80a2")
btnEq=tk.Button(marco,text="=",width="5",height="2",bg="#ff80a2")


#Colocar
labelFondo.place(x=0,y=0)
marco.place(x=25,y=85)

"""pantalla.grid(row=0,column=0,columnspan=4)

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
btnSum.grid(row=4,column=3) """

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