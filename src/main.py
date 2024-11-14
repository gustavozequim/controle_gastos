from src.settings import MENU_PRINCIPAL
from src.pega_gastos.pega_gastos import PegaGastos
from src.controle_planilha.trata_gastos import PlanilhaControle

if __name__ == '__main__':
    print("Iniciando o controle de gastos, um salto para sua vida financeira!\n")
    print('-='*30)
    continuar = True
    valores = None
    while continuar == True:
        for op in MENU_PRINCIPAL:
            print(op)
        print('-='*30)
        print("\nRecomendo começar configurando seus gastos\n")
        print('-='*30)
        opcao = int(input("Como vamos começar?: "))
        print('-='*30)
        pegar_gasto = PegaGastos
        if opcao == 0:
            valores = pegar_gasto.pega_gastos()
            continue
        if opcao == 1:
            pegar_gasto.configura_tipo_gastos()
            continue
        if opcao == 2:
            planilha = PlanilhaControle
            planilha.editar_planilha(valores)
        if opcao == 3:
            print("Ok! O APP será finalizado\nObrigado pela preferência")
            continuar = False

