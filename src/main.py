from src.pega_gastos import PegaGastos
from src.trata_gastos import CriaPlanilhaControle

if __name__ == '__main__':
    print("Iniciando o controle de gastos, um salto para sua vida financeira!\n")
    print('-='*30)
    pegar_gasto = PegaGastos
    valores = pegar_gasto.pega_gastos()
    print("A seguir ocorrerá a criação da planilha de controle\n")
    planilha = CriaPlanilhaControle
    planilha.cria_planilha(valores)
