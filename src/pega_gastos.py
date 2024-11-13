from src.settings import OPCOES_ACEITAS


class PegaGastos:
    
    def pega_gastos():
        tipos_de_gasto_padrao = ['[0] Mercado', '[1] Lazer', '[2] Contas']
        dict_gastos = {}
        continua = True
        lista_valor_gasto = []
        while continua == True:
            print("Insira o tipo de gasto")
            print('-='*30)
            print(f"{tipos_de_gasto_padrao[0]}\n{tipos_de_gasto_padrao[1]}\n{tipos_de_gasto_padrao[2]}")
            print('-='*30)
            tipo_gasto = int(input("Digite o tipo de gasto: "))
            print('-='*30)
            valor_gasto = str(input("Valor do gasto (se houve mais de um gasto com o mesmo \ntipo separe por virgulas os valores, ex: Mercado = 20, 40): "))
            print('-='*30)
            opcao = input("Deseja colocar mais algum gasto?[S/N]: ").upper()
            print('-='*30)
            tipo_gasto_inserido = tipos_de_gasto_padrao[tipo_gasto].removeprefix(f'[{tipo_gasto}] ')
            dict_gastos[tipo_gasto_inserido] = valor_gasto
            while opcao not in OPCOES_ACEITAS:
                print("Por favor digite S para inserir outro gasto, ou N para finalizar!")
                opcao = input("Deseja colocar mais algum gasto?[S/N]: ").upper()
                print('-='*30)
            if opcao == 'N':
                continua = False
        print('-='*30)
        print(f'Os seguintes gastos foram registrados:')
        for chave, valor in dict_gastos.items():
            print(f'{chave} = R${valor}')
        print('-='*30)
        return dict_gastos
