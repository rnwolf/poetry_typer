#!/bin/bash
# This file is used to build some of the release artefacts for linux.
# Ensure that this file is executable.
#  On  MS-Windows use :  git add --chmod=+x -- make-linux-release.sh
#  On Linux : chmod + x make-linux-release.sh
# Commit and push to repo.
#
# Building manylinux-compatible wheels is not trivial.
# As a general rule, binaries built on one Linux distro will only work on other Linux distros that are the same age or newer.
# Therefore, if we want to make binaries that run on most Linux distros, we have to use a very old distro -- CentOS 6.
#https://github.com/pypa/manylinux
#https://github.com/riddell-stan/poetry-install-shared-lib-demo
PYTHON_VERSIONS="cp37-cp37m cp38-cp38"
# Cannot use poetry build with python 3.7 as No module named 'importlib_metadata' which only arrives in python3.8
cd /io
/opt/python/cp38-cp38/bin/pip install pip -U
/opt/python/cp38-cp38/bin/pip install pipx -U
# Install Poetry in virtual env to ensure that its dependencies don't get removed by --no-dev installs for building release.
/opt/_internal/cpython-3.8.3/bin/pipx install --python /opt/python/cp38-cp38/bin/python poetry
/root/.local/bin/poetry config virtualenvs.in-project false
/root/.local/bin/poetry install --no-dev
/root/.local/bin/poetry build --format=wheel
/root/.local/bin/poetry build
cd -
