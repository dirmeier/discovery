# {{ cookiecutter.project_slug }}

[![status](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)
[![ci](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_description }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_description }}/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_description }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_description }})
[![codacy]()]()
[![documentation](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest)
[![version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg?colorB=black&style=flat)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)

> {{ cookiecutter.project_short_description }}

## About

TODO

## Example usage

TODO

## Installation

To install from PyPI, call:

```bash
pip install {{ cookiecutter.project_short_description }}
```

To install the latest GitHub <RELEASE>, just call the following on the
command line:

```bash
pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_short_description }}@<RELEASE>
```

## Contributing

Contributions in the form of pull requests are more than welcome. A good way to start is to check out issues labelled
["good first issue"](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

In order to contribute:

1) Install `{{ cookiecutter.project_slug }}` and dev dependencies via `pip install -e '.[dev]'`,
2) test your contribution/implementation by calling `tox` on the (Unix) command line before submitting a PR.