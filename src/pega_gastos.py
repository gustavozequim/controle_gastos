class PegaGastos:
    def pega_valor_gastos():
        gasto = float(input("Valor do gasto: "))
        return gasto

    def pega_tipo_gastos():
        print("Insira o tipo de gasto")
        print(
        """
        [1] Mercado
        [2] Lazer
        [3] Contas
        """
        )
        tipo_gasto = int(input("Digite o tipo de gasto: "))