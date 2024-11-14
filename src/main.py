from src.settings import MENU_PRINCIPAL
from src.pega_gastos.pega_gastos import PegaGastos
from src.criacao_planilha.trata_gastos import CriaPlanilhaControle

if __name__ == '__main__':
    print("Iniciando o controle de gastos, um salto para sua vida financeira!\n")
    print('-='*30)
    continuar = True
    while continuar == True:
        for op in MENU_PRINCIPAL:
            print(op)
        print('-='*30)
        print("\nRecomendo começar configurando seus gastos\n")
        print('-='*30)
        opcao = int(input("Como vamos começar?: "))
        pegar_gasto = PegaGastos
        if opcao == 0:
            valores = pegar_gasto.pega_gastos()
            continue
        if opcao == 1:
            pegar_gasto.configura_tipo_gastos()
            continue
        if opcao == 2:
            planilha = CriaPlanilhaControle
            planilha.cria_planilha(valores)
        if opcao == 3:
            print("Ok! O APP será finalizado\nObrigado pela preferência")
            continuar = False
