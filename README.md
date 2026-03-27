# Controlador De Gastos
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-green)

## Como funciona:
- Funciona via CLI (Comand Line Interface);
- O usuário inserem dados via terminal;
- Ele pode cadastrar tipos de gastos ou usar os padrões do sistema;
- Pegas os dados, junto do mês que está atualmente e insere numa planilha (.xlsx);
- Cada mês/ano será uma página da planilha.

## Estrutura:
```
controle_gastos\
  L src\
    L controle_planilha/
      L trata_gastos.py
    L pega_gastos/
      L edicao_de_tipos.py
      L  pega_gastos.py
    L __init__.py
    L main.py
    L settings.py
  L .gitignore
  L README.md
  L banco_tipos_de_gastos.txt
  L requirements.txt
```

## Utilização:
  - Para utilizar, clone o projeto no seu PC:
  ```
    - git clone https://github.com/gustavozequim/controle_gastos
  ```
  - Em seguida, instale o requirements.txt:
      - Obs: Antes de instalar o requirements.txt, crie uma venv no Python:
        ```
          - python -m venv <escolha um nome para o ambiente>
          - python .\<nome do ambiente>\Sripts\Activate        
        ```
        Isso garante que você irá instalar as dependências apenas naquele projeto, não afetam nenhum de seus outros projetos.
  
  Após a configuração do ambiente virtual, e inicialização do mesmo, instale as dependências:
  ```
    - pip install -r requirements.txt
  ```
  
  - Execute:
  ```
    - python -m src.main
  ```
  É necessário que você primeiramente, selecione a opção "0", ela lhe permitirá inserir um gasto (obs: os tipos de gastos estão previamente configurados, você pode alterá-los no arquivo banco_tipos_de_gastos.txt).
  
  Após essa primeira inserção, selecione a opção "2", que é a configuração de planilha, ali você vai dar as informações necessárias para criar uma planilha de controle.
  
  Após esse primeiro contato, você terá esse script para controlar seus gastos.


