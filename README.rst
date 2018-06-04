=========
py-config
=========

.. image:: https://travis-ci.org/Maples7/py-app-config.svg?branch=master
    :target: https://travis-ci.org/Maples7/py-app-config

.. image:: https://img.shields.io/pypi/v/py-app-config.svg
    :target: https://pypi.python.org/pypi/py-app-config

Python Application Configuration. Py-config organizes hierarchical configurations for your app deployments.


Usage
=====

Installation
------------

.. code:: shell

    pip install py-app-config


Best Practice
-------------
Firstly, you should have a `config` folder under the codebase of your application, like this:

.. code:: shell

    .
    ├── config
    │   ├── __init__.py
    │   ├── default.json
    │   ├── development.json
    │   ├── production.json
    │   └── test.json
    .


Secondly, set environment variable `PY_ENV` to one of the names of JOSN files in the `config` folder, and it defaults to be `development`.

In your `__init__.py` under `config` folder, these codes can be used:

.. code:: python

    import os
    from py_config import set_config_dir, get_config

    config_dir = os.path.abspath(os.path.dirname(__file__))
    set_config_dir(config_dir)
    config = get_config()

Then, you can use `from config import config` to import your app config in any other places in you codebase.

The final `config` would **merge** `default.json` and `<PY_ENV>.json`. See `dict-recursive-update <https://github.com/Maples7/dict-recursive-update>`_ for the **recursive** update rules.


APIs
----

.. code:: python

    # Set the config directory path
    set_config_dir(
        config_dir=None  # Directory path of `config` folder
    )

    # Get final config according to the `config_dir`. 
    # It should be executed every time after a new `config_dir` is set.
    get_config()


Relatives
=========

- `dict-recursive-update <https://github.com/Maples7/dict-recursive-update>`_
- `node-config <https://github.com/lorenwest/node-config>`_


License
=======
`MIT <./LICENSE.txt>`_

