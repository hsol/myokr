FROM python:3.10
WORKDIR /temp

COPY . .

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false && poetry install

EXPOSE 3000
ENTRYPOINT ["pc", "run", "--loglevel", "debug"]
