from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


class Alumno:
    
    def registrarAlumno(self):
        alumnos = [self.email.get(), self.cel.get()]
        self.TrvAlumnos.insert('',0,text=self.nombre.get(),values=alumnos)
        # alumnos = [self.email.get()]
        # self.TrvAlumnos.insert('',0,text=self.nombre.get(),values=alumnos)
    
    def __init__(self,window):
        self.wind = window
        self.wind.title('CRUD DE ALUMNOS')
        self.wind.geometry('420x390')
        self.wind.configure(bg='#49A')
        
        #frame
        frame = LabelFrame(self.wind,text='Registro de nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=3,pady=10)
        
        ######## CAMPO NOMBRE ##########
        #LABEL NOMBRE
        lbNombre = Label(frame,text='Nombre : ')
        lbNombre.grid(row=1,column=0)        
        #text nombre
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)
        
        ######## CAMPO EMAIL ##########
        #LABEL EMAIL
        lbEmail = Label(frame,text='Email : ')
        lbEmail.grid(row=2,column=0)
        #text EMAIL
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        
        ######## CAMPO CELULAR ##########
        #LABEL CELULAR 
        lbCel = Label(frame,text='Celular : ')
        lbCel.grid(row=3,column=0)
        #text CELULAR 
        self.cel = Entry(frame)
        self.cel.grid(row=3,column=1)
        
        ######### BOTON NUEVO ALUMNO ######
        btnNuevoAlumno = Button(frame,text='Registrar',command=self.registrarAlumno)
        btnNuevoAlumno.grid(row=5,columnspan=2,sticky=W +E)
        
        ##### TRERVIEW ##########
        self.TrvAlumnos = Treeview(height=10,columns=('#0','#1','#2'))
        self.TrvAlumnos.grid(row=6,column=0,columnspan=2,padx=10)
        self.TrvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.TrvAlumnos.heading('#1',text='Email',anchor=CENTER)
        self.TrvAlumnos.heading('#2',text='Celular',anchor=CENTER)

window = Tk()
app = Alumno(window)
window.mainloop()