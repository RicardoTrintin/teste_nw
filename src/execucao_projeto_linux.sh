#! /bin/sh
docker build -t importador_dados .
docker run --rm --name importador_dados_container importador_dados
docker run --name postgres_neoway -d -i -t -p5439:5432 -ePOSTGRES_PASSWORD=12345 postgres:latest
docker exec -it postgres_neoway /bin/sh psql --username=postgres postgres -c "CREATE TABLE resumo_pedidos_cliente (id SERIAL, cpf varchar(15), cnpj VARCHAR(20), private integer, incompleto integer, data_ultima_compra DATE, ticket_medio decimal, ticket_ultima_compra decimal, loja_frequente VARCHAR(20), loja_ultima_compra VARCHAR, created_at timestamp, updated_at timestamp; create index cpf_index on resumo_pedidos_cliente (cpf); create index cnpj_index on resumo_pedidos_cliente (cnpj); create index data_ultima_compra_index on resumo_pedidos_cliente (data_ultima_compra_index); create index loja_frequente_index on resumo_pedidos_cliente (loja_frequente); create index loja_ultima_compra_index on resumo_pedidos_cliente (loja_ultima_compra);"
