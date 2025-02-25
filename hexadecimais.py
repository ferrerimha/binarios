from binarios import Binario

class Hexadecimal:

  caracteres = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
  lista_para_converter = []

  def converte(entrada):
    entrada = entrada.lower()
    lista_para_converter = []
    count = 0
    resultado = []
    saida = []

    for caracter in entrada:
      lista_para_converter.append(caracter)

    if len(lista_para_converter) % 4 != 0:
      numero_de_conjuntos = int(len(lista_para_converter) / 4 + 1)
    else:
      numero_de_conjuntos = int(len(lista_para_converter) / 4)

    for i in range(numero_de_conjuntos):
      numero = Binario.converter("".join(map(str, lista_para_converter[0:4])))
      resultado.append(numero)
      del lista_para_converter[0:4]

    resultado = resultado[::-1]

    for numero in resultado:
      saida.append(Hexadecimal.caracteres[numero])
 
    saida = "".join(map(str, saida))

    return saida



  def desconverter(entrada):

    caracteres = Hexadecimal.caracteres
    convert_list = []
    binario = []
    exit = []
    entrada = entrada.lower()

    for caracter in entrada:
      convert_list.append(caracter)

    for caracter in convert_list:

      try:
        caracter = int (caracter)

        if caracter in caracteres:
          binario.append(Binario.desconverter(caracteres.index(caracter)))

      except:
        
        if caracter in caracteres:
          binario.append(Binario.desconverter(caracteres.index(caracter)))

        else:
          print ("Insira um hexadecimal valido:")
          quit()

    binario = ",".join (map (str, binario))
    binario = binario.split(",")

    for group in binario:

      while len(group) < 4:
        group = "0"+group
      
      exit.append(group)

    exit = int("".join (map (str, exit)))


    return exit
