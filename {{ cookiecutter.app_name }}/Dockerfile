FROM python:3.10-slim as base

ENV POETRY_VERSION=1.1.14 \
	PYTHONUNBUFFERED=1 \
	VIRTUAL_ENV=/opt/env \
	PYTHONPATH=/app \
	POETRY_HOME=/opt/poetry

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/ \
	set -ex \
	# Upgrade image with latest security patches.
	&& apt update \
	&& apt upgrade -y \
	# Install OS libraries and ignore recommended installs that are actually not needed.
	&& apt install -y --no-install-recommends curl \
	&& curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION \
	# Remove unneeded libraries that are used for builds or can never be used in a headless image.
	&& rm -rf /var/lib/apt/lists/* /var/log/* /usr/share/man /usr/share/doc

WORKDIR /app

# Install python dependencies
COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/root/.cache/ \
	python -m venv $VIRTUAL_ENV \
	&& poetry install --no-dev


########################################################
FROM base as production

# Copy source code
COPY . .

# Install poetry scripts
RUN --mount=type=cache,target=/root/.cache/ \
	poetry install --no-dev

CMD ["{{ cookiecutter.module_name }}"]


########################################################
FROM base as dev

RUN --mount=type=cache,target=/root/.cache/ \
	poetry install

COPY . .

RUN --mount=type=cache,target=/root/.cache/ \
	poetry install

CMD ["{{ cookiecutter.module_name }}"]