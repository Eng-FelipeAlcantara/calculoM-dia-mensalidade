
nome = input('Digite o nome do estudante: ')
escola = input('Digite o nome da instituição de ensino: ')
qtde_estudantesfund1 = int(input('Digite a quantidade de estudantes do Fund 1: '))
valorMensalidadefund1 = float(input('Digite o valor da mensalidade do Fund 1: '))
qtde_estudantesfund2 = int(input('Digite a quantidade de estudantes do Fund 2: '))
valorMensalidadefund2 = float(input('Digite o valor da mensalidade do Fund 2: '))
qtde_estudantestotais = qtde_estudantesfund1 + qtde_estudantesfund2
totalArrecadadofund1 = qtde_estudantesfund1 * valorMensalidadefund1
totalArrecadadofund2 = qtde_estudantesfund2 * valorMensalidadefund2
mediaMensalidade = totalArrecadadofund1 +totalArrecadadofund2) / qtde_estudantestotais
print(nome, 'trabalha na empresa', escola)
print('Possui: ', qtde_estudantestotais, 'estudantes.')
print('A média da mensalidade é de: ', str(mediaMensalidade))
