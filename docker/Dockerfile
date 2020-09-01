FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP "aa"
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc git g++ musl-dev build-base linux-headers libffi libffi-dev libxslt-dev libressl-dev libxml2 libxml2-dev libxslt libxslt-dev libjpeg-turbo-dev zlib-dev nodejs npm
COPY . /code
RUN pip install -r dev-requirements.txt
RUN pip install -r requirements.txt
RUN find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip
RUN pre-commit install
CMD ["python3", "app.py"]
