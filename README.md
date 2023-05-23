# zzz233

A minimal python package.

1. download locally
   * clone repository: `git clone xxx`
   * download zip: `wget xxx`
   * download released package: TODO
2. install
   * install locally: `pip install .`
   * (for developer) install locally: `pip install -e ".[dev]"`
   * install from github: `pip install git+https://github.com/husisy/zzz233.git`
   * TODO pypi
3. uninstall `pip uninstall zzz233`
4. scrips
   * run in command line: `zzz233`
5. unittest: download locally
   * `pytest`
   * (require developer install locally) coverage `pytest --cov=python/zzz233`
6. documentation
   * build locally: `mkdocs serve`
   * website: `https://husisy.github.io/zzz233/`
7. github action (CI/CD)
   * build documentation
   * unittest
8. reading material
   * [github/setuptools_scm](https://github.com/pypa/setuptools_scm) (Source Code Management)
   * [setuptools/pyproject-config](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
   * distribute package to pypi

TODO make a clear table

usage

```Python
# a dummy example
from zzz233 import from_pickle, to_pickle
a = 233
to_pickle(a=a)
assert from_pickle('a')==a
```

TODO

1. [ ] semantic versioning [link](https://semver.org/)

## development

new environment

```bash
micromamba create -n zzz233 python
micromamba activate zzz233

pip install .
# pip install -e ".[dev]"
mkdocs serve
```
