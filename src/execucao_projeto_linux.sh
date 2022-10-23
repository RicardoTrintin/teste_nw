#! /bin/sh
docker run --name postgres_neoway -d -i -t -p5432:5432 -ePOSTGRES_PASSWORD=12345 postgres:latest
docker build -t importador_dados .
docker run --rm --name importador_dados_container importador_dados