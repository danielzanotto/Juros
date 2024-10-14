print('Digite o numero que deseja calcular ')
print('\n1 para Juros ')
print('\n2 para Capital ')
print('\n3 para Tempo ')
print('\n4 para Taxa ')
print('\n5 para Montante ')
Selecione = 0
while Selecione == 0:
  Selecione = int(input('\n '))
if Selecione == 1:
  Capital = float(input('\n Digite o Capital: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Juros = Capital * Taxa *  Tempo
      #J = C* i * N
  print(f'O Juros será = {Juros}')
  
if Selecione == 2:
  Juros = float(input('\n Digite o Juros: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
   Capital = Juros / (Taxa * Tempo)
      #C = J / i * N
  print(f'O Capital será = {Capital}')

if Selecione == 3:

  Juros Simples

  Capital = Juros / (Taxa * Tempo)
       #C = J / (i * N)

  Taxa = Juros / (Taxa * Tempo)
       #C = J / (i * N)
   
  Tempo = Juros / (Capital * Taxa)
       #N = J / (C * i)

  Montante = Capital * (1 + Taxa * Tempo)
       #M = C * (1 + i * N)

  Capital = Montante / (1 + Taxa * Tempo)
       #C = M / (1 + i * N)

  Taxa = ((Montante / Juros)-1) / (Tempo)
       #i =((M / J)-1) / (N)

  Tempo = ((Montante / Juros)-1) / (Taxa)
       #N =((M / J)-1) / (N)

  Montante = Capital + Juros
       #M = C +J 

  Juros = Montante - Capital
       #J = M - C 

  Capital = Montante - Juros
       # C = M - J

C = Capital
J = Juros
I = Taxa #Valor unitario de % divide por 100
N = Tempo #Ano 360, Mês 30 
M = Montante

Juros Composto

Montante = Capital * (1 + Taxa) ^ Tempo
# M = C*(1+i)^N

Capital = Montante / (1+ Taxa) ^ Tempo
# C = M/(1+i)^N

Capital = Juros / ((1+ Taxa) ^ Tempo) -1
# C = J/((1+i)^N) -1

Juros = Capital * (((1+ Taxa) ^ Tempo)-1)
# J = C*[(1+i)^N]-1
#Juros = Capital * [((1+ Taxa) ^ Tempo)-1]

Taxa = ((((Juros / Capital) +1) ^ (1/ Tempo)) -1)
# i = [(((J / C)+1)^(1/N))-1]

Taxa = ((((Montante / Capital)^(1/ Tempo)) -1)
# i = [(((M / C)+1)^(1/N))-1]

        
