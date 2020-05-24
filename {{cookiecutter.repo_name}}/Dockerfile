FROM python:{{ cookiecutter.python_major_version }}.{{ cookiecutter.python_minor_version }}-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv based on previously created virtualenv
# pip freeze > installed-packages.txt
# python .\list-key-dev-packages.py
# pip-compile dev-dependencies.in --output-file dev-dependencies.txt
COPY dev-dependencies.txt .
RUN pip install -r dev-dependencies.txt


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}"]
CMD ["10"]
