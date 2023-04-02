import horoscopo
import signo
import mapa_astral

encerrar = 99
while encerrar != 0:
    comando = input('Digite o número que corresponde a sua '
                        'opção e clique enter:\n'
                        '[1] Descobrir meu signo\n'
                        '[2] Meu mapa astral\n'
                        '[3] Ver meu horóscopo\n'
                        '[0] Encerrar\n')
    if int(comando) == 1:
        signo.ver_signo()
        encerrar = 1
    elif int(comando) == 2:
        mapa_astral.ver_mapa_astral()
        encerrar = 1
    elif int(comando) == 3:
        horoscopo.ver_horoscopo()
        encerrar = 1
    elif int(comando) == 0:
        print('\nAté logo. Gratiluz!')
        encerrar = 0
    else:
        print('\nSelecione uma das opções do menu.\n')
    