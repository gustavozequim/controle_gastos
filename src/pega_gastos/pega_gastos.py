import os
from src.pega_gastos.edicao_de_tipos import EdicaoDoBanco
from src.settings import (OPCOES_ACEITAS_DE_GASTOS,
                          OPCOES_PARA_CONFIGURAR_GASTOS)


class PegaGastos:
    
    def pega_gastos():
        if os.path.exists('banco_tipos_de_gastos.txt'):
            with open('banco_tipos_de_gastos.txt', 'r') as arquivo:
                tipos_de_gasto_padrao = [linha.rstrip() for linha in arquivo]
        dict_gastos = {}
        indices = len(tipos_de_gasto_padrao)
        continua = True
        while continua == True:
            print("Insira o tipo de gasto")
            print('-='*30)
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
            print('-='*30)
            tipo_gasto = int(input("Digite o tipo de gasto: "))
            print('-='*30)
            valor_gasto = str(input("Valor do gasto (se houve mais de um gasto com o mesmo \ntipo separe por virgulas os valores, ex: Mercado = 20, 40): "))
            print('-='*30)
            opcao = input("Deseja colocar mais algum gasto?[S/N]: ").upper()
            print('-='*30)
            tipo_gasto_inserido = tipos_de_gasto_padrao[tipo_gasto].removeprefix(f'[{tipo_gasto}] ')
            dict_gastos[tipo_gasto_inserido] = valor_gasto
            while opcao not in OPCOES_ACEITAS_DE_GASTOS:
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
    
    def configura_tipo_gastos():
        print("Deseja configurar com os tipos de gasto?")
        opcao = str(
            input(
                "(Ao dizer não, será pego os tipos já cadastrados no banco.\nDo contrário, irá poder cadastrar e/ou editar os já cadastrados)[S/N]: "
            )
        ).upper()
        if opcao == "S":
            continuar = True
            while continuar == True:
                edicao = EdicaoDoBanco
                print("Perfeito! O que deseja fazer?")
                print('-='*30)
                print('-='*30)
                for config in OPCOES_PARA_CONFIGURAR_GASTOS:
                    print(f'{config}')
                tipo_config = int(input("Digite o número de sua escolha: "))
                if tipo_config == 0:
                    arquivo = edicao.edicao_de_tipos()
                    arquivo.close()
                    continue
                if tipo_config == 1:
                    print("Ok! Me diga agora o nome desse tipo de gasto:")
                    print("WIP: Aqui será feito o cadatro no banco de novos tipos de gasto")
                    continue
                if tipo_config == 2:
                    print("Selecione o tipo que deseja excluir:")
                    print("WIP: Banco de tipos salvos")
                    print("Tem certeza que deseja excluir esse tipo permanetemente?")
                    if 'S':
                        print("Tipo de gasto exluido com sucesso")
                    continue
                if tipo_config == 3:
                    print("Terminamos as edições por aqui!")
                    continuar = False
