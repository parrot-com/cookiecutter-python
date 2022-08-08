FROM python:3.10-alpine3.16 as base

ENV POETRY_VERSION=1.1.13-r2 \
	PYTHONUNBUFFERED=1 \
	VIRTUAL_ENV=/opt/env \
	PYTHONPATH=/app

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN set -ex \
	# Upgrade image with latest security patches.
	&& apk update \
	# Install OS libraries and ignore recommended installs that are actually not needed.
	&& apk add --no-cache poetry=$POETRY_VERSION \
	# Remove unneeded libraries that are used for builds or can never be used in a headless image.
	# && apk del curl \
	&& rm -vrf /var/cache/apk/* /var/log/* /usr/share/man /usr/share/doc

WORKDIR /app

# Install python dependencies
COPY pyproject.toml poetry.lock ./

RUN python -m venv $VIRTUAL_ENV \
	&& poetry install --no-dev

# Copy source code
COPY . .

# Install poetry scripts
RUN poetry install --no-dev

CMD ["{{ cookiecutter.app_name }}"]

########################################################
FROM base as dev

RUN poetry install

########################################################
FROM base as production

# ...
