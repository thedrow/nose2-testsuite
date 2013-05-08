============
Contributing
============

nose2-testsuite is currently in the initial development phase and contributions are always most welcome.

Please refer to the :doc:`roadmap <roadmap>` and to the `issue tracker <https://github.com/thedrow/nose2-testsuite/issues?labels=feature&state=open>`_ for the list of required features.

Contributing Documentation
==========================


If you are not a developer and you wish to contribute you can help a lot by improving the documentation.
If you have found a documentation bug, a typo or if you have found better phrasing feel free to fork the project and submit a pull request.

Requirements
------------

In order to contribute documentation to nose2-testsuite you must have the following software installed:

- `Git <http://git-scm.com/book/en/Getting-Started-Installing-Git>`_
- `Python <http://python.org>`_ (Either `2.7 <http://python.org/download/releases/2.7.4/>`_, `3.2 <http://python.org/download/releases/3.2.4/>`_, `3.3 <http://python.org/download/releases/3.3.1/>`_ or `pypy <http://pypy.org/download.html>`_)
- `pip <https://pypi.python.org/pypi/pip>`_
- `Sphinx <http://sphinx-doc.org/index.html>`_
- `sphinx-bootstrap-theme <http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html>`_

Please follow the instructions on the provided links to install the required software.

.. note::

    If you are running on Windows note that you can use the `chocolatey package manager <http://chocolatey.org>`_ to install `Python 2.7.4 <http://chocolatey.org/packages/python>`_.

    If you are running on your favorite Linux distribution, it might have already provided the required Python version when you installed the distribution.

    In order to verify that simply type:

    .. code-block:: bash

        python --version

    If not, your package manager might provide it.

In order to start contributing simply clone the repository or `your fork <https://help.github.com/articles/fork-a-repo>`_:

.. code-block:: bash

    git clone https://github.com/thedrow/nose2-testsuite.git

Build the documentation and watch the results:

.. code-block:: bash

    cd docs/
    make html


Design & Logo
-------------

The project is very new and thus does not have a unique design & logo yet.
It is currently not a priority but something I'd like to have in the future.

The documentation uses the amazing `bootstrap <http://twitter.github.io/bootstrap/>`_ css framework for styling.

If you'd like to contribute a logo or a new design do not hesitate to bring ideas or sketches to the `mailing list <https://groups.google.com/forum/?fromgroups#!forum/nose2-testsuite>`_.


Contributing Code
=================

In order to contribute code to nose2-testsuite you must have the following software installed:

- `Git <http://git-scm.com/book/en/Getting-Started-Installing-Git>`_
- `Python <http://python.org>`_ (Versions `2.6 <http://python.org/download/releases/2.6.8/>`_, `2.7 <http://python.org/download/releases/2.7.4/>`_, `3.2 <http://python.org/download/releases/3.2.4/>`_, `3.3 <http://python.org/download/releases/3.3.1/>`_ & `pypy <http://pypy.org/download.html>`_)
- `pip <https://pypi.python.org/pypi/pip>`_
- `virtualenv <https://pypi.python.org/pypi/virtualenv>`_

Please follow the instructions on the provided links to install the required software.



.. code-block:: bash

    git clone https://github.com/thedrow/nose2-testsuite.git


Submitting a pull request
=========================
