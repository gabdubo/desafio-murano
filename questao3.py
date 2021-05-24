def deposito(idade_atual, idade_retirada, quantia_desejada, taxa_juros):
  tempo = (idade_retirada - idade_atual)*12
  taxa_mensal = -1+(1+taxa_juros)**(1/12)
  valor_presente = quantia_desejada/(1+taxa_mensal)**tempo
  valor = (valor_presente*((1+taxa_mensal)**tempo)*taxa_mensal)/((-1+(1+taxa_mensal)**tempo))
  print( "O valor a ser depositado por mês é: R$" +str(round(valor,2)))
deposito(18, 50, 3000000, 0.035)


