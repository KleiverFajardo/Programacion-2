import tkinter as tk
from tkinter import messagebox

def registrar():
    info = f"Nombre: {nombre.get()}\nApellido: {apellido.get()}\nEdad: {edad.get()}\nDirección: {direccion.get()}\nTeléfono: {telefono.get()}\nSexo: {var_sexo.get()}\nCiudad: {ciudad.get(ciudad.curselection())}"
    messagebox.showinfo("Información de Registro", info)

root = tk.Tk()

tk.Label(root, text="Nombre").grid(row=0)
nombre = tk.Entry(root)
nombre.grid(row=0, column=1)

tk.Label(root, text="Apellido").grid(row=1)
apellido = tk.Entry(root)
apellido.grid(row=1, column=1)

tk.Label(root, text="Edad").grid(row=2)
edad = tk.Entry(root)
edad.grid(row=2, column=1)

tk.Label(root, text="Dirección").grid(row=3)
direccion = tk.Entry(root)
direccion.grid(row=3, column=1)

tk.Label(root, text="Teléfono").grid(row=4)
telefono = tk.Entry(root)
telefono.grid(row=4, column=1)

tk.Label(root, text="Sexo").grid(row=5)
var_sexo = tk.StringVar()
rb_masculino = tk.Radiobutton(root, text="Masculino", variable=var_sexo, value="Masculino")
rb_masculino.grid(row=5, column=1)
rb_femenino = tk.Radiobutton(root, text="Femenino", variable=var_sexo, value="Femenino")
rb_femenino.grid(row=6, column=1)

tk.Label(root, text="Ciudad").grid(row=7)
ciudades = ["Cartagena", "Medellín", "Cali", "Barranquilla", "Bogota"]
ciudad = tk.Listbox(root)
for i in ciudades:
    ciudad.insert(tk.END, i)
ciudad.grid(row=7, column=1)

btn_registrar = tk.Button(root, text="Registrar", command=registrar)
btn_registrar.grid(row=8, column=1)

root.mainloop()
