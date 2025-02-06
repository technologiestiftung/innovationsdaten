![](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F-at%20Technologiestiftung%20Berlin-blue)

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# Innovationsdaten

## Prerequisites

- Latest Python 3.11 version (i.e. 3.11.4, other versions might work as well) – You can e.g. use pyenv, see below.

## Installation

### Set your virtual environment

The following steps are not required but recommended. This will allow you to install packages in your isolated virtual environment instead of globally, reducing the risk of breaking system tools or other projects.

1. Install [pyenv](https://github.com/pyenv/pyenv) and the [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) plugin.
2. Download the appropriate Python version with
```shell
pyenv install 3.11.4
```
in the command line.
3. Create a virtual environment with the appropriate Python version and name for your environment, for example
```shell
pyenv virtualenv 3.11.4 innovationserhebung
```
4. Activate the environment with
```shell
pyenv activate innovationserhebung
```


### Install Python requirements and pre-commit

Install the required libraries with the command line
```shell
pip install -r requirements.txt -r requirements-dev.txt
```

Install the pre-commit git hook
```shell
pre-commit install
```

## Usage or Deployment

### Convert the source XLSX data source to JSON

Taking an input XLSX file similar to the one in this repository, you can convert it to
JSON by running
```shell
python -m data_processing.xlsx2json
```

### Handling & updating requirements

We are using [pip-tools](https://pip-tools.readthedocs.io/en/latest/) to handle the
requirements and keep the dependencies updated.

In case you are updating or adding some dependencies, do so in the `requirements.*.in`
files and don't forget to compile the new `requirements.*.txt` files running:
```shell
pip-compile requirements.in
pip-compile requirements-dev.in
```

To update the packages, following the version pinning defined in the
`requirements*.in` files, run:
```shell
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
```

To keep your environment in sync, run:
```shell
pip-sync requirements.txt requirements-dev.txt
```

## Development

tbd...

## Tests

tbd...

## Contributing

Before you create a pull request, write an issue so we can discuss your changes.

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/guadiromero"><img src="https://avatars.githubusercontent.com/u/guadiromero" width="64px;" alt="Guadalupe Romero"/><br /><sub><b>Guadalupe Romero</b></sub></a><br /><a href="https://github.com/technologiestiftung/innovationsdaten/commits?author=guadiromero" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Content Licensing

Texts and content available as [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

## Credits

<table>
  <tr>
    <td>
      Made by  <a href="https://www.technologiestiftung-berlin.de/">
        <br />
        <br />
        <img width="150" src="https://logos.citylab-berlin.org/logo-technologiestiftung-berlin-de.svg" />
      </a>
    </td>
    <td>
      Supported by <a href="https://www.berlin.de/">
        <br />
        <br />
        <img width="150" src="https://logos.citylab-berlin.org/logo-berlin.svg" />
      </a>
    </td>
  </tr>
</table>

## Related Projects
