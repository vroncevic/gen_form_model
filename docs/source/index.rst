Generate Form Model (Django/Flask)
----------------------------------

**gen_form_model** is generator for form model

* Django FWK
* Flask FWK

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_form_model python checker| |gen_form_model python package| |github issues| |documentation status| |github contributors|

.. |gen_form_model python checker| image:: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python_checker.yml

.. |gen_form_model python package| image:: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_form_model.svg
   :target: https://github.com/vroncevic/gen_form_model/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_form_model.svg
   :target: https://github.com/vroncevic/gen_form_model/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-form-model/badge/?version=latest
   :target: https://gen-form-model.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|gen_form_model python3 build|

.. |gen_form_model python3 build| image:: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_form_model/actions/workflows/gen_form_model_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_form_model/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_form_model-x.y.z.tar.gz
    cd gen_form_model-x.y.z/
    # python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen-form-model

Dependencies
-------------

**gen_form_model** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_form_model** is based on OOP

Code structure

.. code-block:: bash

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
        
        6 directories, 11 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_form_model <https://vroncevic.github.io/gen_form_model>`_

**gen_form_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_form_model/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
