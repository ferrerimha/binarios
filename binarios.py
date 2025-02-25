class Binario:

  def converter(entrada):
    entrada = entrada
    resultado = 0
    num_binario = []

    for num in entrada:
      num = int(num)
      if num != 0 and num != 1:
        print ("digite um numero binario, contendo apenas 0 e 1")
        continue

    for num in entrada[::-1]:
      num_int = int(num)
      num_binario.append(num_int)

    for i in range (len(num_binario)):
      if num_binario[i] == 1:
        expoente = num_binario[i] * 2**i
        resultado += expoente

    return resultado
  

  
  def desconverter(entrada):
    entrada = int (entrada)
    num_binario = []

    while entrada > 1:
      if entrada % 2 == 0:
        num_binario.append(0)
        entrada = entrada / 2

      else:
        entrada -= 1
        entrada = entrada / 2
        num_binario.append(1)

    if entrada == 1:
      num_binario.append(1)

    if entrada == 0:
      num_binario.append(0)

    saida = int("".join(map(str,num_binario[::-1])))

    return saida
