# Generate Form Model (Django/Flask)

**gen_form_model** is tool for generation form model for:

* Django FWK
* Flask FWK

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_form_model/workflows/Python%20package%20gen_form_model/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Generation process](#generation-process)
- [Library structure](#library-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_form_model/workflows/Install%20Python2%20Package%20gen_form_model/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_form_model/workflows/Install%20Python3%20Package%20gen_form_model/badge.svg?branch=master)

Navigate to **[release page](https://github.com/vroncevic/gen_form_model/releases)** download and extract release archive.

To install **gen_form_model** type the following:
```
tar xvzf gen_form_model-x.y.z.tar.gz
cd gen_form_model-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_form_model
copying gen_form_model/__init__.py -> build/lib.linux-x86_64-2.7/gen_form_model
creating build/lib.linux-x86_64-2.7/gen_form_model/form
copying gen_form_model/form/gen_form.py -> build/lib.linux-x86_64-2.7/gen_form_model/form
copying gen_form_model/form/__init__.py -> build/lib.linux-x86_64-2.7/gen_form_model/form
copying gen_form_model/form/write_template.py -> build/lib.linux-x86_64-2.7/gen_form_model/form
copying gen_form_model/form/form_selector.py -> build/lib.linux-x86_64-2.7/gen_form_model/form
copying gen_form_model/form/read_template.py -> build/lib.linux-x86_64-2.7/gen_form_model/form
creating /usr/local/lib/python2.7/dist-packages/gen_form_model
copying build/lib.linux-x86_64-2.7/gen_form_model/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model
creating /usr/local/lib/python2.7/dist-packages/gen_form_model/form
copying build/lib.linux-x86_64-2.7/gen_form_model/form/gen_form.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model/form
copying build/lib.linux-x86_64-2.7/gen_form_model/form/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model/form
copying build/lib.linux-x86_64-2.7/gen_form_model/form/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model/form
copying build/lib.linux-x86_64-2.7/gen_form_model/form/form_selector.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model/form
copying build/lib.linux-x86_64-2.7/gen_form_model/form/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_form_model/form
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/form/gen_form.py to gen_form.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/form/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/form/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/form/form_selector.py to form_selector.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_form_model/form/read_template.py to read_template.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_form_model.egg-info
writing requirements to gen_form_model.egg-info/requires.txt
writing gen_form_model.egg-info/PKG-INFO
writing top-level names to gen_form_model.egg-info/top_level.txt
writing dependency_links to gen_form_model.egg-info/dependency_links.txt
writing manifest file 'gen_form_model.egg-info/SOURCES.txt'
reading manifest file 'gen_form_model.egg-info/SOURCES.txt'
writing manifest file 'gen_form_model.egg-info/SOURCES.txt'
Copying gen_form_model.egg-info to /usr/local/lib/python2.7/dist-packages/gen_form_model-1.0.0-py2.7.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_form_model/run/gen_form_model_run.py -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_form_model/conf
copying gen_form_model/conf/gen_form_model.cfg -> /usr/local/lib/python2.7/dist-packages/gen_form_model/conf/
copying gen_form_model/conf/gen_form_model_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_form_model/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_form_model/conf/template
copying gen_form_model/conf/template/django.template -> /usr/local/lib/python2.7/dist-packages/gen_form_model/conf/template/
copying gen_form_model/conf/template/flask.template -> /usr/local/lib/python2.7/dist-packages/gen_form_model/conf/template/
creating /usr/local/lib/python2.7/dist-packages/gen_form_model/log
copying gen_form_model/log/gen_form_model.log -> /usr/local/lib/python2.7/dist-packages/gen_form_model/log/
```

Or You can use docker to create image/container.

[![gen_form_model docker checker](https://github.com/vroncevic/gen_form_model/workflows/gen_form_model%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_form_model/actions?query=workflow%3A%22gen_form_model+docker+checker%22)

### Dependencies

**gen_form_model** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)
* [Flask-WTF - Simple integration of Flask and WTForms](https://pypi.org/project/Flask-WTF/)
* [Django - High-level Python Web framework](https://pypi.org/project/Django/)

### Generation process

Generation flow:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/gen_form_model_flow.png)

### Library structure

**gen_form_model** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/gen_form_model.png)

Library structure:
```
.
├── conf/
│   ├── gen_form_model.cfg
│   ├── gen_form_model_util.cfg
│   └── template/
│       ├── django.template
│       └── flask.template
├── form/
│   ├── form_selector.py
│   ├── gen_form.py
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
├── __init__.py
├── log/
│   └── gen_form_model.log
└── run/
    └── gen_form_model_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_form_model/badge/?version=latest)](https://gen_form_model.readthedocs.io/projects/gen_form_model/en/latest/?badge=latest)

More documentation and info at:
* [gen_form_model.readthedocs.io](https://gen_form_model.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/gen_form_model](https://vroncevic.github.io/gen_form_model/)

**gen_form_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
