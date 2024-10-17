FROM python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"

RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "main.py"]