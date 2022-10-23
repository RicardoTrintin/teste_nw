FROM python:3
# .10-slim-bullseye

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTONPATH}:/"
ENV CAMINHO_ARQUIVO_BASE "src\\features\\importar_dados\\arquivos\\arquivo_para_importar\\base_teste.txt"
ENV CAMINHO_ARQUIVO_IMPORTADOS_BASE "src\\features\\importar_dados\\arquivos\\arquivos_importados\\base_teste.txt"
ENV INTEGRADOR_SETTINGS "settings.production"

COPY . /src
RUN pip install psycopg2 \
    && pip install Unidecode \
    && pip install validate_docbr

WORKDIR /src
CMD python main.py