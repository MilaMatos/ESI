import time
import os

while(True):
    print('---------------BEM VINDO---------------')
    print("Prosseguir - 1")
    print('Encerrar   - 2')
    print('---------------------------------------')
    opc = int(input('Opção: '))

    while opc != 1 and opc != 2:
        print('Valor inválido\n')
        opc = int(input('Opção: '))
    if opc == 1:
        dia = int(input('\nDia: '))
        while dia < 1 or dia > 31:
            print(" INVÁLIDO!\n")
            dia = int(input('\nDia: '))
        mes = int(input('Mes: '))
        while mes < 1 or mes > 12:
            print("INVÁLIDO!\n")
            mes = int(input('Mes: '))
        ano = int(input('Ano: '))
        while ano < 12 or ano > 23:
            print("INVÁLIDO!\n")
            ano = int(input('Ano: '))

        if ano == 21:
            if mes < 4 and mes > 0:
                print("\nInfantil 2")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\nNão pode matricular")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 20:
            if (mes < 4 and mes > 0):
                print("\nInfantil 3")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\nInfantil 2")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 19:
            if (mes < 4 and mes > 0):
                print("\nInfantil 4")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\nInfantil 3")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 18:
            if (mes < 4 and mes > 0):
                print("\nInfantil 5")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\nInfantil 4")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 17:
            if (mes < 4 and mes > 0):
                print("\n1º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\nInfantil 5")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 16:
            if (mes < 4 and mes > 0):
                print("\n2º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\n1º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 15:
            if (mes < 4 and mes > 0):
                print("\n3º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\n2º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 14:
            if (mes < 4 and mes > 0):
                print("\n4º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\n3º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 13:
            if (mes < 4 and mes > 0):
                print("\n5º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\n4º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue

        if ano == 12:
            if (mes < 4 and mes > 0):
                print("\n6º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
            elif (mes >= 4):
                print("\n5º ano")
                input("\n\n\nPressione ENTER para voltar ao menu")
                os.system("cls")
                continue
    if opc == 2:
        print('\n\nEncerrando...')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        os.system("cls")
        break
