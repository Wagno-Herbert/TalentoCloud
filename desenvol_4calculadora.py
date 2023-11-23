# TalentoCloud 
def calculadora(n1, n2, operacao):
  if (operacao == "soma"):
    resp = n1 + n2
  elif (operacao == "subtração"):
    resp = n1 - n2
  elif (operacao == "multiplicação"):
    resp = n1 * n2
  elif (operacao == "divisão"):
    resp = n1/n2
  else:
    resp = 0
  return resp
