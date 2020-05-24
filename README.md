# Python Cookiecutter for Public Typer CLI packages hosted in GitHub utilitsing Poetry for managing dependencies 

Do you need to quickly develop public commandline tools but struggle to install all the associated tooling?

Why not try the newish approach of using Poetry, Typer and GitHub workflow actions?

[Poetry](https://python-poetry.org/) is a Python package dependency management tool,
[Typer](https://pypi.org/project/typer/) is an appoarch to simplify CLI development
[GitHub Action Workflows](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) help you automate tedious tasks to check quality.


## Quickstart

Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [GitHub CLI](https://cli.github.com/).
Install [pipx](https://pipxproject.github.io/pipx/), then use pipx to install in isolated environments:
 - [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 - [Poetry](https://github.com/python-poetry/poetry/issues/677)
 - [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

Now you can create a Python cli, quickly with (See README.md for more details.)

```
cookiecutter gh:rnwolf/poetry_typer
cd <CLI directory>
git init
git config --global core.safecrlf false
git add --all
git commit -m "first commit"
gh repo create --public
git push -u origin master
```

Side note:  I use Windows and Linux frequently, so there is sometime a problem with line ending in text files on MS-Windows.
I use the following to supress all the git warnings about line ending changes.

git config --global core.safecrlf false

See this discussion for more comments about the complicatons https://github.com/actions/checkout/issues/135
My take and summary is you want to use .gitattributes and default to LF line endings everywhere.

## Features

- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Docstrings coverage check with [interrogate](https://pypi.org/project/interrogate/)
- Git hooks that run checks with [pre-commit](https://pre-commit.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
  - Github action to check for common security issues based on [PyCharm Security Scanner](https://github.com/marketplace/actions/pycharm-python-security-scanner)
  - Documents published to gh-pages
  - Create Github Release
  - Test package on latest Linux, MS-Windows and Mac operating systems
  - Build release packages.
  - Final manual step to download distibution artefacts and then publish to Github release notice and PyPI
- MkDocs to publish documentation to PUBLIC gh-pages site.  Repo has to be public.
- Writing style recomendations for Markdown files with [Vale](https://errata-ai.gitbook.io/vale/)
  - [Introducing Vale an NLP Powerlinter](https://medium.com/@jdkato/introducing-vale-an-nlp-powered-linter-for-prose-63c4de31be00)
  - [Google’s technical writing course](https://developers.google.com/tech-writing)
  - [Principles that govern good documentation](https://documentation.divio.com/)

## Interesting references

See https://dev.to/mburszley/an-introduction-to-poetry-2b6n
[Hyper moden Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
[How to make a Python package using Poetry](https://dev.to/sivakon/python-poetry-35ec)
[Packaging python using Poetry on Google Cloud](https://dev.to/sivakon/packaging-python-using-poetry-on-google-cloud-l8d)
[GitHub Actions: Automate Your Python Development Workflow with poetry](https://dan.yeaw.me/)


# TODO

## Setup Github workflow to create builds, wheels, for Win, Linux and Mac.

https://github.com/marketplace/actions/pypi-publish

https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

https://github.com/cspencerjones/xlayers/commit/3091b06d361c67629b2da0f56ee3fedfe09e2de6

https://github.com/kivy/kivy/actions/runs/27570257/workflow
