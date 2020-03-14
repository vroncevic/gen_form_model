# Generate Form Model (Django/Flask).

gen_form_model is toolset for generation data model for:
* Django FWK
* Flask FWK

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_form_model/workflows/Python%20package/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_form_model.svg)](https://github.com/vroncevic/gen_form_model/graphs/contributors)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/gen_form_model/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf gen_form_model-1.0.tar.gz
cd gen_form_model-1.0/python-tool
cp -R ~/bin/   /root/scripts/gen_form_model/
cp -R ~/conf/  /root/scripts/gen_form_model/
cp -R ~/log/   /root/scripts/gen_form_model/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF FORM MODEL

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/python-tool-docs/gen_form_model_flow.png)

### TOOL STRUCTURE

gen_form_model is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/python-tool-docs/gen_form_model.png)

Generator structure:

```
.
├── bin
│   ├── form
│   │   ├── form_selector.py
│   │   ├── gen_form.py
│   │   ├── __init__.py
│   │   ├── read_template.py
│   │   └── write_template.py
│   ├── gen_form_model.py
│   └── gen_form_model_run.py
├── conf
│   ├── gen_form_model.cfg
│   ├── gen_form_model_util.cfg
│   └── template
│       ├── django.template
│       └── flask.template
└── log
    └── gen_form_model.log

```

### COPYRIGHT AND LICENCE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Copyright (C) 2018 by https://vroncevic.github.io/gen_form_model

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.4.2 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
