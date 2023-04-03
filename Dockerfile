FROM nikolaik/python-nodejs:python3.10-nodejs19
WORKDIR /temp

RUN git clone -b pynecone-deploy --single-branch https://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@github.com/hsol/myokr .

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false && poetry install

EXPOSE 80
EXPOSE 8000
ENTRYPOINT ["pc", "run", "--env", "prod", "--port", "80"]
