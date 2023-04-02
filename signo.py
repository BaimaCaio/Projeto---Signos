import datetime
import func_bot

def ver_signo():
    voltar = 1
    while voltar !=0:
        #import func_bot
        data_nascimento = func_bot.nascimento()

        # Converte a string digitada pelo usuário em um objeto do tipo datetime
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m')
                
            if data_nascimento.day >= 21 and data_nascimento.month == 3 or data_nascimento.day <= 20 and data_nascimento.month == 4:
                signo = "Áries"
            elif data_nascimento.day >= 21 and data_nascimento.month == 4 or data_nascimento.day <= 20 and data_nascimento.month == 5:
                signo = "Touro"
            elif data_nascimento.day >= 21 and data_nascimento.month == 5 or data_nascimento.day <= 20 and data_nascimento.month == 6:
                signo = "Gêmeos"
            elif data_nascimento.day >= 21 and data_nascimento.month == 6 or data_nascimento.day <= 22 and data_nascimento.month == 7:
                signo = "Câncer"
            elif data_nascimento.day >= 23 and data_nascimento.month == 7 or data_nascimento.day <= 22 and data_nascimento.month == 8:
                signo = "Leão"
            elif data_nascimento.day >= 23 and data_nascimento.month == 8 or data_nascimento.day <= 22 and data_nascimento.month == 9:
                signo = "Virgem"
            elif data_nascimento.day >= 23 and data_nascimento.month == 9 or data_nascimento.day <= 22 and data_nascimento.month == 10:
                signo = "Libra"
            elif data_nascimento.day >= 23 and data_nascimento.month == 10 or data_nascimento.day <= 21 and data_nascimento.month == 11:
                signo = "Escorpião"
            elif data_nascimento.day >= 22 and data_nascimento.month == 11 or data_nascimento.day <= 21 and data_nascimento.month == 12:
                signo = "Sagitário"
            elif data_nascimento.day >= 22 and data_nascimento.month == 12 or data_nascimento.day <= 20 and data_nascimento.month == 1:
                signo = "Capricórnio"
            elif data_nascimento.day >= 21 and data_nascimento.month == 1 or data_nascimento.day <= 19 and data_nascimento.month == 2:
                signo = "Aquário"
            elif data_nascimento.day >= 20 and data_nascimento.month == 2 or data_nascimento.day <= 20 and data_nascimento.month == 3:
                signo = "Peixes"
            print(f'\nSeu signo é: {signo}\n')


        except:
            print('\nA data inserida é inválida. Verifique e tente novamente.')
        
        while True:
            outro = int(input('\n[1] Verificar outra data.\n'
                '[0] Retornar ao menu\n'))
            if outro == 1:
                print('')
                break
            elif outro == 0:
                print('')
                voltar = 0
                pass
            break
        
        