def nascimento():
    while True:
        dia = str(input('Digite o dia que você nasceu:\n'))
        if dia.isnumeric() and int(dia) >= 1 and int(dia) <= 31:
            if len(dia) == 1:
                dia = '0' + dia
            break
        else:
            print('\nO dia precisa ser numérico entre 1 e 31.\n')
            pass
    while True:    
        mes = str(input('Digite o mês que você nasceu:\n'))
        if mes.isnumeric() and int(mes) >=1 and int(mes) <= 12:
            if len(mes) == 1:
                mes = '0' + mes
            break
        else:
            print('\n O mês precisa ser numérico entre 1 e 12.')
        
    data_nascimento = f'{dia}/{mes}'
    return data_nascimento

def ano_nascimento():
    while True:
        ano = str(input('Digite o ano que você nasceu:\n'))
        if ano.isnumeric():
            return ano
        else:
            print('\nO ano precisa ser numérico.\n')
            pass

def hora_nascimento():
    while True:
        hora = str(input('Digite a hora em que você nasceu (entre 0 e 23):\n'))
        if hora.isnumeric() and int(hora) >= 0 and int(hora) <= 23:
            if len(hora) == 1:
                hora = '0' + hora
            break
        else:
            print('\nA hora precisa ser entre 0 e 23.\n')
            pass
    while True:
        minutos = str(input('Digite os minutos em que você nasceu (entre 0 e 59):\n'))
        if minutos.isnumeric() and int(minutos) >= 0 and int(minutos) <= 59:
            if len(minutos) == 1:
                minutos = '0' + minutos
            break
        else:
            print('\nOs minutos precisam ser entre 0 e 59.\n')
            pass
    
    hora_nascimento = f'{hora}:{minutos}'
    return hora_nascimento
