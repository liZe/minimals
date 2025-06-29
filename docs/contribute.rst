Contribute
==========

You want to add some code to Minimals, launch its tests or improve its documentation? Thank you very much! Here are some tips to help you play with Minimals in good conditions.

The first step is to clone the repository, create a virtual environment and install Minimals dependencies:

.. code-block:: shell

   git clone https://github.com/liZe/Minimals.git
   cd Minimals
   python -m venv .venv
   .venv/bin/pip install -e '.[doc,test]'

You can then launch Python to test your changes:

.. code-block:: shell

   .venv/bin/python

Running Minimals might look something like this:

.. code-block:: shell

   .venv/bin/python -m minimals pykachu


Code & Issues
-------------

If you’ve found a bug in Minimals, it’s time to report it, and to fix it if you can!

You can report bugs and feature requests on `GitHub`_. If you want to add or fix some code, please fork the repository and create a pull request, we’ll be happy to review your work.

You can find more information about the code architecture in the :ref:`Dive into the Source` section.

.. _GitHub: https://github.com/liZe/Minimals


Tests
-----

Tests are stored in the ``tests`` folder at the top of the repository. They use
the pytest_ library.

You can launch tests using the following command::

  .venv/bin/python -m pytest

Minimals also uses ruff_ to check the coding style::

  .venv/bin/python -m ruff check

.. _pytest: https://docs.pytest.org/
.. _ruff: https://docs.astral.sh/ruff/


Documentation
-------------

Documentation is stored in the ``docs`` folder at the top of the repository. It relies on the `Sphinx`_ library.

You can build the documentation using the following command::

  .venv/bin/sphinx-build docs docs/html

The documentation home page can now be found in the ``/path/to/minimals/docs/html/index.html`` file. You can open this file in a browser to see the final rendering.

.. _Sphinx: https://www.sphinx-doc.org/
