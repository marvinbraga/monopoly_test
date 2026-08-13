FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /var/app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . ./

RUN uv sync --locked --no-dev

CMD ["uv", "run", "--no-dev", "python", "main.py"]
