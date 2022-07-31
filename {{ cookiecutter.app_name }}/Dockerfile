FROM python:3.10-slim as base

ENV POETRY_VERSION=1.1

RUN set -ex \
	# Upgrade image with latest security patches.
	&& apt update \
	&& apt upgrade -y \
	# Install OS libraries and ignore recommended installs that are actually not needed.
	# && apt-get install -y --no-install-recommends vim \
	# Install poetry
	&& pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir "poetry==$POETRY_VERSION" \
	# Remove unneeded libraries that are used for builds or can never be used in a headless image.
	# && apt-get purge -y --auto-remove --allow-remove-essential vim \
	&& rm -rf /var/lib/apt/lists/* /var/log/* /usr/share/man /usr/share/doc

WORKDIR /app

# Install python dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install

# Copy source code
COPY . .

# Install {{ cookiecutter.app_name }}
RUN pip install /app

# TODO: do we want to have mulistage build?
# FROM base as production

# Remove dev dependencies
# RUN poetry install --no-dev \
# 	&& pip uninstall -y poetry

CMD ["{{ cookiecutter.app_name }}"]
