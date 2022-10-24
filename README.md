# teste_nw

## Serviço
Este serviço utiliza arquivo de texto para importar dados através de script python para um banco de dados relacional postgres.

## Regra de negócio

O serviço captura os dados do arquivo base_teste.txt e separa através dos seguintes campos:

- **CPF**
- **CNPJ**
- **PRIVATE**
- **INCOMPLETO**
- **DATA_ULTIMA_COMPRA**
- **TICKET_MEDIO**
- **TICKET_ULTIMA_COMPRA**
- **LOJA_FREQUENTE**
- **LOJA_ULTIMA_COMPRA**

Com isso, o sistema entende como um resumo de dados de pedidos de cliente

Então....
- **Se a informação de CPF ou CNPJ nao forem válidas:**
    - O registro não será importado para o banco, pois são informações crusciais para identificação do cliente;
- **Se o registro possui apenas CNPJ e não CPF:**
    - O cliente é considerado como privado ou seja, um cliente juridico; 
- **Se alguma informação do cliente como ticket médio, data da última compra e etc... não existe:**
    - O cliente é considearado como incompleto, mas é importado para base desta maneira.

## Como rodar o projeto

Antes de proseguir, é preciso que o arquivo base_teste.txt esteja dentro do diretório **src/features/importar_dados/arquivos**

#### Obs:. Sem o arquivo não estiver neste local, após rodar os próximos passos, teremos um retorno de erro de que nao é possível importar os dados, pois o arquivo de texto como base não foi encontrado.**

Também é necessário que o Docker esteja instalado em seu computador.

- **Se estiver usando windows**
    - Executar o arquivo execucao_projeto_windows.bat
- **Se estiver usando Linux**
    - Executar o arquivo execucao_projeto_linux.sh

Este arquivo **bat** ou **sh**, irá subir um container com um banco postgres na sua máquina, onde será possível acessá-lo pelos seguintes parâmetros:

```
host: host.docker.internal
port: 5432
database: postgres
user: postgres
pass: 12345
```

Caso a porta criada por default pelo executável já esteja sendo utilizada em seu computador, é possível modificá-la no arquivo em que está executando pelo seguinte comando:

```
docker run --name postgres_neoway -d -i -t -pAQUI_DEFINA_A_PORTA_DESEJADA:5432 -ePOSTGRES_PASSWORD=12345 postgres:latest
```

Ou se preferir, pode rodar o seguinte comando:

```
docker system prune
```

#### Obs:. Este comando excluirá todas as imagens, networks e containers que não estão sendo utilizados em sua máquina, caso tenha algo dentro destes requisítos que não deseja excluir, não é recomendado executar este passo.

Caso modifique esta informação, também é necessário muda-la no arquivo Dockerfile:

```
PORT_DATABASE "ATRIBUA A PORTA QUE COLOCOU NO COMANDO PARA SUBIR O POSTGRES"
```

**Bônus: Se abrir o Dockerfile, verá que é nele que estão sendo declaradas as variáveis de ambiente, onde alí, também é possivel mudar host, usuário e demais informações de parâmetros do banco, porém, sempre lembre de que se modificar algumas destas variáveis, também é necessário validar se o comando em que sobe a imagem do postgres no arquivo executável também necessitará de alterações.**

Então ao final da execução, terá uma mensagem de que a **Importação dos dados do arquivo foi finalizada com sucesso!**
