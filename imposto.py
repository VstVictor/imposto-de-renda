# Simulador de imposto de remda em Python

while True:

    # Apresentação

    print('\n\t\t\t Imposto de Renda \n\t')

    # Entrada

    sl_bruto = float(input('Informe o salário bruto: '))
    dp = int(input('Informe o número de dependentes: '))

    # Processamento

    desc_dp = 189.59 * dp
    sl_base = sl_bruto - desc_dp


    if sl_base < 1903.98:
        aliquota = 0.0
        fx_desc = 0.0
        imp_bruto = (sl_base * aliquota) - 0.0
    elif sl_base <= 2826.65:
        aliquota = 0.075
        fx_desc = 142.80
        imp_bruto = (sl_base * aliquota) - 142.80
    elif sl_base <= 3751.05:
        aliquota = 0.15
        fx_desc = 354.80
        imp_bruto = (sl_base * aliquota) - 354.80
    elif sl_base <= 4664.68:
        aliquota = 0.225
        fx_desc = 636.13
        imp_bruto = (sl_base * aliquota) - 636.13
    else:
        aliquota = 0.275
        fx_desc = 869.36
        imp_bruto = (sl_base * aliquota) - 869.36

    ir_devido = imp_bruto
    sl_liqui = sl_bruto - ir_devido
    aliquota_ef = ir_devido / sl_bruto

    print('\n\t -- Saída de Dados --\n')

    # Saída

    print('Salário bruto -- R${:.2f}'.format(sl_bruto))
    print('Número de dependentes -- {}'.format(dp))
    print('Salário base -- R${:.2f}'.format(sl_base))
    print('Alíquota -- {:.1f}%'.format(aliquota * 100))
    print('IR devido -- R${:.2f}'.format(ir_devido))
    print('Salário Líquido -- R${:.2f}'.format(sl_liqui))
    print('Alíquota Efetiva -- {:.2f}%'.format(aliquota_ef * 100))

    print('\n ---- Selecione a Opção ----\n\t')

    print('1. Calcular outro imposto de renda: ')
    print('2. Fechar: ')

    op = int(input(''))

    if op == 1:
        print('carregando...')
    elif op == 2:
        print('finalizado')
        break
    else:
        print('Opçao invalida')
        break