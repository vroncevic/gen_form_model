<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/gen_form_model_logo.png" width="25%">

# Generate Form Model (Django/Flask)

☯️ **gen_form_model** is tool for generation form model for

* Django FWK
* Flask FWK

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_form_model py code checker](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_py_checker.yml/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_py_checker.yml) [![gen_form_model python package checker](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_package.yml/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation process](#generation-process)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/debtux.png)

[![gen_form_model build python2 package](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python2_publish.yml/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python2_publish.yml) [![gen_form_model build python3 package](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python3_publish.yml/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python3_publish.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python 📦 is located at **[pypi.org](https://pypi.org/project/gen_form_model/)**.

You can install by using pip

```bash
# python2
pip2 install gen_form_model
# python3
pip3 install gen_form_model
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_form_model/releases/)** download and extract release archive 📦.

To install **gen_form_model** type the following

```bash
tar xvzf gen_form_model-x.y.z.tar.gz
cd gen_form_model-x.y.z/
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py 
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install ./dist/gen_form_model-*-py2-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_form_model_run.py
ln -s /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_form_model_run.py /usr/local/bin/gen_form_model_run.py
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_form_model-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_form_model_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_form_model_run.py /usr/local/bin/gen_form_model_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_form_model/releases)** download and extract release archive 📦.

To install **gen_form_model**, locate and run setup.py with arguments

```bash
tar xvzf gen_form_model-x.y.z.tar.gz
cd gen_form_model-x.y.z
# python2
pip2 install -r requirements.txt
python2 setup.py install_lib
python2 setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container 🚢.

[![gen_form_model docker checker](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_docker_checker.yml/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_docker_checker.yml)

### Dependencies

**gen_form_model** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)
* [Flask-WTF - Simple integration of Flask and WTForms](https://pypi.org/project/Flask-WTF/)
* [Django - High-level Python Web framework](https://pypi.org/project/Django/)

### Generation process

Generation flow

![Generation flow](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/gen_form_model_flow.png)

### Tool structure

**gen_form_model** is based on OOP

![Generation model](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/gen_form_model.png)

Generator structure

```bash
gen_form_model/
├── conf/
│   ├── gen_form_model.cfg
│   ├── gen_form_model_util.cfg
│   ├── project.yaml
│   └── template/
│       ├── django.template
│       └── flask.template
├── __init__.py
├── log/
│   └── gen_form_model.log
├── pro/
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_form_model_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_form_model/badge/?version=latest)](https://gen_form_model.readthedocs.io/en/latest/?badge=latest)
 [![pages-build-deployment](https://github.com/vroncevic/gen_form_model/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/vroncevic/gen_form_model/actions/workflows/pages/pages-build-deployment)

📗 More documentation and info at

* [gen_form_model.readthedocs.io](https://gen_form_model.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to gen_form_model](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_form_model](https://vroncevic.github.io/gen_form_model/)

**gen_form_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
