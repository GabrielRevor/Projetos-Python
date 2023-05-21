import re 
import sys

entrada = input('CPF [Ex: 746.824.890-70]: ')
cpf_enviado = re.sub(
    r'[^~0-9]',
    '',
    entrada
) 

if len(entrada) == 0:
    print('Você não digitou nada')
    sys.exit()
else:
    entrada_e_sequencial = entrada == entrada[0] * len(entrada)


if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado[:9] 
contador_regressivo = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
    

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo
    contador_regressivo -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_calculo = nove_digitos + str(digito_1) + str(digito_2)

if cpf_enviado == cpf_gerado_calculo:
    print(f'Seu CPF é válido!')
else:
    print('CPF inválido.')


    

            