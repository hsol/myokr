FROM nikolaik/python-nodejs:python3.10-nodejs19
WORKDIR /temp

COPY . .

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false && poetry install

RUN pc init

EXPOSE 3000
EXPOSE 8000
ENTRYPOINT ["pc", "run", "--loglevel", "debug"]
