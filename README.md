# teste_nw

## Serviço
Este serviço utiliza arquivo de texto para importar dados através de script python para um banco de dados relacional postgres.

## Regra de negócio

O serviço captura os dados do arquivo base_teste.txt e separa através dos seguintes campos:

    CPF
    CNPJ
    PRIVATE
    INCOMPLETO
    DATA_ULTIMA_COMPRA
    TICKET_MEDIO
    TICKET_ULTIMA_COMPRA
    LOJA_FREQUENTE
    LOJA_ULTIMA_COMPRA

    Com isso, o sistema entende como um resumo de dados de pedidos de cliente

    Então....
    - Se a informação de CPF ou CNPJ nao forem validas:
        O registro nao sera importado para o banco, pois sao informacoes crusciais para identificacao do cliente;
    - Se o registro possui apenas CNPJ e não CPF:
        o cliente é considerado como privado ou seja, um cliente juridico; 
    - Se alguma informação do cliente como ticket médio, data da ultima compra e etc... não existe
        o cliente é considearado como incompleto, mas e importado para base desta maneira.

## Como rodar o projeto

    Antes de proseguir, é preciso que o arquivo base_teste.txt esteja dentro do diretório src/features/importar_dados/arquivos

    Tambem e necessario que o Docker esteja instalado em seu computador.

    ### Obs:. Sem o arquivo nao estiver neste local, apos rodar os proximos passos, teremos um retorno de erro de que nao e possivel importar os dados, pois o arquivo de texto como base nao foi encontrado.

    * Se estiver usando windows
        - Executar o arquivo execucao_projeto_windows.bat
    * Se estiver usando Linux
        - Executar o arquivo exucao_projeto_linux.sh