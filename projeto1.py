import math
import subprocess
from datetime import datetime, timedelta
subprocess.run('cls', shell=True)

try:
    tipo_inventimento = str(input('Escolha o tipo de Investimento: '))
    capital = float(input('Digite o valor do capital inicial: '))
    taxa_juros = float(input('Digite a taxa de juros mensal (em %): ')) / 100
    meses = int(input('Digite o numero de meses: '))
    montante = capital * math.pow(1+taxa_juros, meses)
    input('\nAperte Enter para calcular o montante...')
except ValueError:
    print('Entrada invalida!\nInsira valores numéricos para o capital, taxa de juros e meses')
else:
    print('\nResumo do Investimento:')
    print(f'Tipo de Investimento: {tipo_inventimento}')
    print(f'Capital inicial: R$ {capital}')
    print(f'Taxa de Juros: {taxa_juros:.2f}%')
    print(f'Prazo: {meses} meses')
    print(f'Montante: R$ {montante:.2f}')
    print('\nDatas:')
    data = datetime.now()
    data_futura = data + timedelta(days=meses*30)
    print(f'Aplicação: {data.strftime("%d/%m/%Y")}')
    print(f'vencimento: {data_futura.strftime("%d/%m/%Y")}')

input('\nPressione Enter para sair...')


