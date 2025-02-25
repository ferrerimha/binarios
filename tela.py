import tkinter as tk
import binarios, hexadecimais

class Tela:

  def __init__(self, tamanho, title):
    self.tamanho = tamanho
    self.title = title

  
  def create_display(self):

    self.display = tk.Tk()
    self.display.title (self.title)
    self.display.geometry (self.tamanho)

    label = tk.Label (self.display, text= "Bem vindo ao conversor de binarios feito com python", font=("Arial", 14))
    label.pack(pady=60)

    self.inputs = tk.Entry(self.display, font=("arial", 12))
    self.inputs.pack()

    self.label_resultado = tk.Label(self.display, text="", pady=20, font=("Arial", 12))
    self.label_resultado.pack()

    button1 = tk.Button(self.display, text="binario para decimal",command= self.binarie)
    button1.pack(pady=5)

    button2 = tk.Button(self.display, text="Decimal para binario",command= self.decimal)
    button2.pack(pady=5)

    button3 = tk.Button(self.display, text="hexadecimal para binario",command= self.hexadecimal)
    button3.pack(pady=5)

    button4 = tk.Button(self.display, text="binario para hexadecimal",command= self.binarie2)
    button4.pack(pady=5)
  
    self.display.mainloop()



  def binarie(self):
    result = binarios.Binario.converter(self.inputs.get())
    self.label_resultado.config(text=f"Seu resultado é: {result}")
    print (result)

  def decimal(self):
    result = binarios.Binario.desconverter(self.inputs.get())
    self.label_resultado.config(text=f"Seu resultado é: {result}")
    print(result)

  def hexadecimal(self):
    result = hexadecimais.Hexadecimal.desconverter(self.inputs.get())
    self.label_resultado.config(text=f"Seu resultado é: {result}")
    print(result)

  def binarie2(self):
    result = hexadecimais.Hexadecimal.converte(self.inputs.get())
    self.label_resultado.config(text=f"Seu resultado é: {result}")
    print(result)


