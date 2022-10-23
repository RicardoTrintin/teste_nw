docker run --name postgres_neoway -d -i -t -p5432:5432 -ePOSTGRES_PASSWORD=12345 postgres:latest
docker cp C:\Projetos\Projetos\teste_nw\configuracao_projeto_inicial\script_database.sql postgres_neoway:/
docker exec -it postgres_neoway /bin/sh -c "psql --username=postgres postgres < script_database.sql"
pause
