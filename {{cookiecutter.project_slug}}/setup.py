import re
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

PROJECT_PATH = dirname(abspath(__file__))


def readme():
    with open("README.md") as fl:
        return fl.read()


def _read_requirements(fl):
    with open(fl) as fh:
        return fh.read().splitlines()


def _version():
    version = None
    for line in open(join(PROJECT_PATH, "{{ cookiecutter.project_slug }}", "__init__.py")):
        if line.startswith("__version__"):
            version = re.match(r"__version__.*(\d+\.\d+\.\d+).*", line).group(1)
    if version is None:
        raise ValueError("couldn't parse version number from __init__.py")
    return version


setup(
    name="{{ cookiecutter.project_slug }}",
    version=_version(),
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    license="Apache 2.0",    
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
      
    ],
    extras_require={
        "dev": ["pre-commit", "black", "isort", "pylint", "tox"]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",        
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
