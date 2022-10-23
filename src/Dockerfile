FROM python:3
# .10-slim-bullseye

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTONPATH}:/"
ENV CAMINHO_ARQUIVO "features/importar_dados/arquivos/base_teste.txt"
# ENV CAMINHO_ARQUIVO_IMPORTADOS_BASE "src\\features\\importar_dados\\arquivos\\arquivos_importados\\base_teste.txt"
ENV INTEGRADOR_SETTINGS "settings.production"
ENV HOST_DATABASE "host.docker.internal"
ENV PORT_DATABASE "5439"
ENV DATABASE "postgres"
ENV USER_DATABASE "postgres"
ENV PASS_DATABASE "postgrespwneoway"

COPY . /src
RUN pip install -r src/requirements.txt

WORKDIR /src
CMD python main.py