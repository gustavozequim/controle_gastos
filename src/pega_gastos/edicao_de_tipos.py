class EdicaoDoBanco:

    def edicao_de_tipos():
        with open('banco_tipos_de_gastos.txt', 'r+') as arquivo:
            tipos_de_gasto_padrao = [linha.rstrip() for linha in arquivo]
            indices = len(tipos_de_gasto_padrao)
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
            op_edicao = int(input("Diga qual opção deseja editar: "))
            novo_tipo = str(input("Ótimo!O que será posto no lugar?: "))
            tipos_de_gasto_padrao[op_edicao] = novo_tipo
            print("Os tipos ficaram assim:")
            arquivo.truncate(0)  # Apaga o conteúdo do arquivo até a última linha
            arquivo.seek(0)  # Vai para a última linha
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
                arquivo.write(f'{tipos_de_gasto_padrao[indice]}\n')
        return arquivo
    
    def deletar_tipo():
        with open('banco_tipos_de_gastos.txt', 'r+') as arquivo:
            tipos_de_gasto_padrao = [linha.rstrip() for linha in arquivo]
            indices = len(tipos_de_gasto_padrao)
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
            op_edicao = int(input("Diga qual opção deseja deletar: "))
            op = str(input("Tem certeza que deseja excluir esse tipo permanetemente?[S/N]: ")).upper()
            if op == 'S':
                tipos_de_gasto_padrao.remove(tipos_de_gasto_padrao[op_edicao])
                print("Tipo de gasto exluido com sucesso")
            else:
                print("Sem problemas! O banco se manteve")
                return arquivo
            indices = len(tipos_de_gasto_padrao)
            print("Os tipos ficaram assim:")
            arquivo.truncate(0)  # Apaga o conteúdo do arquivo até a última linha
            arquivo.seek(0)  # Vai para a última linha
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
                arquivo.write(f'{tipos_de_gasto_padrao[indice]}\n')
        return arquivo
    
    def criacao_de_tipo():
        with open('banco_tipos_de_gastos.txt', 'r+') as arquivo:
            tipos_de_gasto_padrao = [linha.rstrip() for linha in arquivo]
            indices = len(tipos_de_gasto_padrao)
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
            novo_tipo = str(input("Ok! Me diga agora o nome desse tipo de gasto:"))
            tipos_de_gasto_padrao.append(novo_tipo)
            print("Tipo de gasto exluido com sucesso")
            print("Sem problemas! O banco se manteve")
            indices = len(tipos_de_gasto_padrao)
            print("Os tipos ficaram assim:")
            arquivo.truncate(0)  # Apaga o conteúdo do arquivo até a última linha
            arquivo.seek(0)  # Vai para a última linha
            for indice in range(indices):
                print(f"[{indice}] {tipos_de_gasto_padrao[indice]}")
                arquivo.write(f'{tipos_de_gasto_padrao[indice]}\n')
        return arquivo
