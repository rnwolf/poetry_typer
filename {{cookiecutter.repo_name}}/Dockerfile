FROM python:{{ cookiecutter.python_major_version }}.{{ cookiecutter.python_minor_version }}-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc bash && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/app
WORKDIR /usr/app
#ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENV POETRY_VERSION=1.0.9
RUN pip3 install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
# As we are already in an isolated environment we do not need to create another
RUN poetry config virtualenvs.create false
# Install the package dependencies (No dev packages)
RUN poetry export -f requirements.txt | pip install -r /dev/stdin

# Build and Install the app
COPY ./src ./src
COPY README.md README.md
RUN poetry build -f wheel -n && pip install --no-deps dist/*.whl && rm -rf dist *.egg-info

# Create app directory and change PWD for interfacing to outside world
RUN mkdir /app
WORKDIR /app

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.package_name}}"]
# The help argument will be overridden with any commandline arguments.
CMD ["--help"]

#Examples for Windows Powershell
# Show help
# docker run -t -i --rm -v ${PWD}:/app containername:latest
# Show version
# docker run -t -i --rm -v ${PWD}:/app containername:latest --version

# Open a bash shell inside of the docker container
# docker run -t -i --rm --entrypoint /bin/bash -v ${PWD}:/app containername:latest

# When using docker to run command setup a command alias for imagetitle
# In your powershell profile add the following
# function imagetitle {
#  docker run -it --rm v ${pwd}:/app containername:latest $args
# }

# In your bash profile  .bashrc add
# alias imagetitle='docker run -it --rm -v \`pwd\`:/app containername:latest'
#
