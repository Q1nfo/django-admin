FROM python:3.11-slim

WORKDIR /opt/django-admin

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=/opt/django-admin \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN groupadd --system service && useradd --system -g service admin

RUN apt-get update && apt-get install -y wget

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./

USER admin

ENTRYPOINT ["bash", "entrypoint.sh"]




