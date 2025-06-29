First Steps
===========

Installation
------------

Minimals |version| depends on:

* Python_ ≥ 3.9.0

The easiest way to install and use Minimals is to use uv_::

  uvx minimals

You can also use a `virtual environment`_ and pip_::

  python3 -m venv .venv
  source .venv/bin/activate
  pip install minimals
  minimals

.. _Python: https://www.python.org/
.. _uv: https://docs.astral.sh/uv/
.. _virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
.. _pip: https://pip.pypa.io/


Command-Line
------------

Using the minimal command line interface can be as simple as this:

.. code-block:: sh

    minimals pykachu

For more information, you can use:

.. code-block:: sh

    minimals --help


Python Library
--------------

The Python version of the above example goes like this:

.. code-block:: python

    from minimals import hello
    hello("pykachu")
