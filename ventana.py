from tkinter import*
from lexen import prosesarLexico
from sintax import prosesarSintax

def iniciarInterfase():
    raiz = Tk()

    miFrame=Frame(raiz, width=100, height=100)
    miFrame.pack()


    label= Label(miFrame , text="Input:")
    label.grid(row=0 , column=0 , columnspan = 4, sticky="w" , padx=10, pady=5)
    label.config(fg="black" , justify="left" , width=0 , font=('Arial', 15))

    cuadro = Text(miFrame)
    cuadro.grid(row=1 , column=0 , columnspan = 4, sticky="w" , padx=10 , pady=10)
    cuadro.config(fg="blue" , width=100, height=18)
    
    scrollVert=Scrollbar(miFrame, command=cuadro.yview)
    scrollVert.grid(row=1, column=4, columnspan = 4 , sticky="nsew")
    cuadro.config(yscrollcommand=scrollVert.set)
    


    label2= Label(miFrame , text="Output:")
    label2.grid(row=2 , column=0 , columnspan = 4,  sticky="w" , padx=10 , pady=10)
    label2.config(fg="black" , justify="left" , width=0 , font=('Arial', 15))

    output = Text(miFrame)
    output.grid(row=3 , column=0 , columnspan = 4 , sticky="w" , padx=10 , pady=5)
    output.config(fg="blue" , width=100, height=15)
 
    scrollVert2=Scrollbar(miFrame, command=output.yview)
    scrollVert2.grid(row=3, column=4, columnspan = 4 , sticky="nsew")
    output.config(yscrollcommand=scrollVert2.set)
    
    output.config(state= DISABLED)

    def getLexen():
        output.config(state= NORMAL)
        borrar(output)

        data1 = ""
        data1 = cuadro.get("1.0", "end")
        
        output.insert("end", prosesarLexico(data1))
        output.config(state= DISABLED)
    

    def getSintax():
        output.config(state= NORMAL)
        borrar(output)

        data2 = ""
        data2 = cuadro.get("1.0", "end")
        
        output.insert("end", prosesarSintax(data2))
        output.config(state= DISABLED)

    
    def borrar(textbox):
        textbox.delete("1.0", "end")
    
    def boorarTodo():
        output.config(state= NORMAL)
        borrar(output)
        borrar(cuadro)
        output.config(state= DISABLED)

    botonLex = Button(miFrame , text = "Analisis Lexico" , command=getLexen)
    botonLex.grid(row=4 , column=0 ,sticky="w" , padx=10 , pady=10 )
    botonLex.config(width=15 ,fg="green",bg="white", font=("Arial",14),relief="groove",bd=4)
    
    botonYacc = Button(miFrame , text = "Analisis Sintactico \n y  Semantico" , command=getSintax)
    botonYacc.grid(row=4 , column=1 ,sticky="w" , padx=10 , pady=10 )
    botonYacc.config(width=15 ,fg="green",bg="white", font=("Arial",14),relief="groove",bd=4)

    botonRestart = Button(miFrame , text = "Reiniciar" , command=boorarTodo)
    botonRestart.grid(row=4 , column=2 ,sticky="w" , padx=10 , pady=10 )
    botonRestart.config(width=15 ,fg="red",bg="white", font=("Arial",14),relief="groove",bd=4)
   



    raiz.mainloop()


iniciarInterfase()