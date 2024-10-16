print('Digite o numero que deseja calcular ')
print('\n1 para Juros ')
print('\n2 para Capital usando Montante ')
print('\n3 para Capital usanado Juros ')
print('\n4 para Taxa usando Montante ')
print('\n5 para Taxa usando Juros ')
print('\n6 para Montante ')

Selecione = 0
while Selecione == 0:
  Selecione = int(input('\n '))
  
if Selecione == 1: # Juros
  Capital = float(input('\n Digite o Capital: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Juros = Capital * (((1+ Taxa) ** Tempo)-1)
      #J = C* i * N
  print(f'O Juros será = {Juros}')
  
if Selecione == 2: #Capital - Montante
  Montante = float(input('\n Digite o Montante: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Capital = Montante / (1+ Taxa) ** Tempo
      # C = M/(1+i)**N
  print(f'O Capital será = {Capital}')
  
if Selecione == 3: #Capital - Juros
  Juros = float(input('\n Digite o Juros: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Capital = Juros / ((1+ Taxa) ** Tempo) -1
      # C = J/((1+i)^N) -1
  print(f'O Capital será = {Capital}')

if Selecione == 4: #Taxa - Montante
  Montante = float(input('\n Digite o Montante: '))
  Capital = float(input('\n Digite o Capital: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Taxa = (((Montante / Capital)**(1/ Tempo)) -1)
        
  print(f'O Taxa será = {Taxa}')
          
if Selecione == 5: #Taxa - Juros
  Capital = float(input('\n Digite o Capital: '))
  Juros = float(input('\n Digite o Juros: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Taxa = ((((Juros / Capital) +1) ** (1/ Tempo)) -1)
  
  print(f'O Taxa será = {Taxa}')

if Selecione == 6:
  Capital = float(input('\n Digite o Capital: '))
  Taxa = float(input('\n Digite o Taxa ao mes: '))
  Tempo = float(input('\n Digite o Tempo em Meses: '))
  Montante = Capital * (1 + Taxa) ** Tempo
  # M = C*(1+i)^N
        
  print(f'O Montante será = {Montante}')
  

#C = Capital
#J = Juros
#I = Taxa #Valor unitario de % divide por 100
#N = Tempo #Ano 360, Mês 30 
#M = Montante

#Juros Composto

#Montante = Capital * (1 + Taxa) ** Tempo
# M = C*(1+i)^N

#Capital = Montante / (1+ Taxa) ** Tempo
# C = M/(1+i)^N

#Capital = Juros / ((1+ Taxa) ** Tempo) -1
# C = J/((1+i)^N) -1

#Juros = Capital * (((1+ Taxa) ** Tempo)-1)
# J = C*[(1+i)^N]-1
#Juros = Capital * [((1+ Taxa) ^ Tempo)-1]

#Taxa = ((((Montante / Capital)**(1/ Tempo)) -1)
# i = [(((M / C)+1)^(1/N))-1]

#Taxa = ((((Juros / Capital) +1) ** (1/ Tempo)) -1)
# i = [(((J / C)+1)^(1/N))-1]
