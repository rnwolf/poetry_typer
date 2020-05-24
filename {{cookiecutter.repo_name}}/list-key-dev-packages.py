#!/usr/bin/env python3
"""Create a file, dev-dependencies.txt, that we can use to load virtualenv with development packages,
based on previouly environment setup with pyproject.toml

Use:

pip freeze > installed-packages.txt

Run this script to filter for packages specified in pyproject.toml

python list-key-dev-packages.py

Next get all dependent packages and pinned version numbers:

pip-compile dev-dependencies.in --output-file dev-dependencies.txt

Load into a new Virtualenv with:

pip install -r dev-dependencies.txt
"""

import toml
from pathlib import Path
import datetime

source_file = Path("pyproject.toml")
config = toml.load(source_file)
packages = sorted(list(config["tool"]["poetry"]["dev-dependencies"].keys()))

output_file = open("dev-dependencies.in", "w")
output_file.write(f"# Created on: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\n")
output_file.write(f"# Directory: {source_file.cwd()}\n")
output_file.write(f"# File: {source_file}\n")
output_file.write("# Section: ['tool.poetry.dev-dependencies']\n")

with open("installed-packages.txt", encoding="utf-16-le") as file:
    lines = file.readlines()
    lines = sorted(lines)
    my_packages = packages.copy()
    for line in lines:
        clean_line = line.strip()
        for package in my_packages:
            if clean_line.startswith(package):
                output_file.write(clean_line + "\n")
                my_packages.remove(package)
                break

output_file.close()
