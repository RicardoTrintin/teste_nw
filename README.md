# teste_nw

## Serviço
Este serviço utiliza arquivo de texto para importar dados através de script python para um banco de dados relacional postgres.
&nbsp;

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

Com isso, o sistema entende como um resumo de dados de pedidos de cliente.

Então...
- **Se a informação de CPF ou CNPJ nao forem válidas:**
    - O registro não será importado para o banco, pois são informações crusciais para identificação do cliente;
- **Se o registro possui apenas CNPJ e não CPF:**
    - O cliente é considerado como privado ou seja, um cliente juridico;
- **Se alguma informação do cliente como ticket médio, data da última compra e etc... não existe:**
    - O cliente é considearado como incompleto, mas é importado para base desta maneira.
&nbsp;

## Estrutura do banco de dados

Como a lágica foi montada em cima dos dados, acreditando que eles são de um resumo de pedido do cliente, a estrutura do banco ficou da seguinte maneira.

* Tabela de resumo do pedido com informações que podem ser utilizadas para algum fim de relatório de BI por exemplo.
```
CREATE TABLE resumo_pedido_cliente (
	id SERIAL,
	cpf varchar(15),
	cnpj VARCHAR(20),
	private integer,
	incompleto integer,
	data_ultima_compra DATE,
	ticket_medio decimal,
	ticket_ultima_compra decimal,
	loja_frequente VARCHAR(20),
	loja_ultima_compra VARCHAR,
	created_at timestamp,
	updated_at timestamp
);
```

* E índices para uma melhor consulta pelo back-end.

```
CREATE INDEX cpf_index on resumo_pedido_cliente (cpf);
CREATE INDEX cnpj_index on resumo_pedido_cliente (cnpj);
CREATE INDEX data_ultima_compra_index on resumo_pedido_cliente (data_ultima_compra);
CREATE INDEX loja_frequente_index on resumo_pedido_cliente (loja_frequente);
CREATE INDEX loja_ultima_compra_index on resumo_pedido_cliente (loja_ultima_compra);
```
&nbsp;

## Como rodar o projeto

#### Dependências

Antes de proseguir, é preciso que o arquivo base_teste.txt esteja dentro do diretório **src/features/importar_dados/arquivos**.

#### Obs:. Sem o arquivo não estiver neste local, após rodar os próximos passos, teremos um retorno de erro de que nao é possível importar os dados, pois o arquivo de texto como base não foi encontrado.**
&nbsp;

Também é necessário que o Docker esteja instalado em seu computador.
1. [Instalar docker](https://docs.docker.com/install/)
&nbsp;

Com ele instalado, rodar os seguintes comandos:
&nbsp;

- Passo 1:
	- Este comando irá gerar e subir imagem e um container no docker do postgres, onde:
		- Nome: ```postgres_neoway```
		- Porta: ```parametro -p5432```
		- Senha para acesso: ```-ePOSTGRES_PASSWORD=12345```
	&nbsp;

		```
		docker run --name postgres_neoway -d -i -t -p5432:5432 -ePOSTGRES_PASSWORD=12345 postgres:latest
		```
	&nbsp;
	- Seus parâmetros para conexão após subir o container:

		```
		host: local
		port: 5432
		database: postgres
		user: postgres
		pass: 12345
		```
		&nbsp;

		- Caso a porta utilizada no comando já esteja sendo utilizada em seu computador, basta mudar no comando acima e rodar novamente
		&nbsp;
		&nbsp;

		- Ou se preferir, pode rodar o seguinte comando:
		&nbsp;

			```
			docker system prune
			```
			- #### Obs:. Este comando remova todos os contêineres, redes, imagens (tanto pendentes quanto não referenciados) não utilizados e, opcionalmente, volumes, caso tenha algo dentro destes requisítos que não deseja excluir, não é recomendado executar este passo.
			&nbsp;

		&nbsp;

		- Caso modifique esta informação de porta, também é necessário muda-la no arquivo Dockerfile:
		&nbsp;

			```
			PORT_DATABASE "ATRIBUA A PORTA QUE COLOCOU NO COMANDO PARA SUBIR O POSTGRES"
			```

* **Bônus: Se abrir o Dockerfile, verá que é nele que estão sendo declaradas as variáveis de ambiente, onde alí, também é possivel mudar host, usuário e demais informações de parâmetros do banco, porém, sempre lembre de que se modificar algumas destas variáveis, também é necessário validar se o comando em que sobe a imagem do postgres também necessitará de alterações.**
&nbsp;

- Passo 2:
	- Se posicione dentro da pasta src do projeto e rode o seguinte comando:
	&nbsp;

		```docker build -t importador_dados .```
		&nbsp;

		- Este comando irá gerar a imagem docker do script para execução com o nome ```importador_dados```
		&nbsp;
		&nbsp;

	- E Após gerar a imgaem do script basta executar um run:
	&nbsp;

		```docker run --rm --name importador_dados_container importador_dados```
	&nbsp;
	&nbsp;

# Rodar projeto local
Após criar o ambiente virtual você deve instalar as dependências em seu ambiente virtual:

    $ pip install -r src/requirements.txt

Após instalar as dependências você pode rodar a aplicação
(variáveis de ambiente estão dentro do arquivo Dockerfile):

    $ python src/main.py
&nbsp;

## Testes Unitários

Apesar do script não possuir uma step para rodar os testes unitários pelo docker, é possivel roda-los localmente no ambiente virtual

	$ pytest --cov .
&nbsp;
&nbsp;

Então ao final da execução, terá uma mensagem de que a **Importação dos dados do arquivo foi finalizada com sucesso!**
