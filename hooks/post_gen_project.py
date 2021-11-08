import os
import sys


def set_python_version():
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = [
        r".github/workflows/main.yml",
    ]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)
    print(
        """
    # Enter project directory
    cd <repo_name>
    git init
    git add --all
    # Ensure that make-linux-release.sh file is executable.
    #  On  MS-Windows use :  git add --chmod=+x -- make-linux-release.sh
    #  On Linux : chmod + x make-linux-release.sh
    git commit -m "First commit"
    git branch -M main
    # Create a repository for the current directory.
    gh repo create --public
    # Connect up local and remote repo.
    git push -u origin main
    # Check that you don't have any existing virtualenv active and create new local .venv
    virtualenv -p {python_version} .venv
    # Create the Virtualenv in .venv and install dependencies
    poetry install
    # Setup pre-commit and pre-push hooks
    poetry run pre-commit install -t pre-commit
    poetry run pre-commit install -t pre-push
    Check out the README.md for much more detail.
    """
    )


if __name__ == "__main__":
    main()
