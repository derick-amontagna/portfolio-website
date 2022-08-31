FROM python:3.9.12 as base

WORKDIR /application
COPY ["pyproject.toml", "poetry.lock", "/application/"]

ARG APP_NAME
ARG APP_VERSION
ENV APP_NAME=$APP_NAME
ENV APP_VERSION=$APP_VERSION
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8


RUN apt-get update && \
        apt-get install -y --no-install-recommends apt-utils && \
        apt-get install curl && \
        apt-get install -y \
        software-properties-common \
        python3-software-properties \
        gcc \
        g++ \
        libsnappy-dev \
        graphviz
        
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:${PATH}"


FROM base AS ci
RUN poetry config virtualenvs.create false && poetry install
COPY ./ /application

RUN make flake8 && \
    make pylint && \
    make black && \
    make pytest


FROM base AS dist
RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH "/root/google-cloud-sdk/bin:${PATH}"

RUN poetry config virtualenvs.create false && poetry install --no-dev
COPY ./ /application

EXPOSE 8080
CMD ["make", "app"]