============
Contributing
============

nose2-testsuite is currently in the initial development phase and contributions are even more welcome than usual.

Please refer to the :doc:`roadmap <roadmap>` and to the `issue tracker <https://github.com/thedrow/nose2-testsuite/issues?labels=feature&state=open>`_ for the list of required features.

Required knowledge & experience
===============================

In order to contribute to the project in any fashion you must have some knowledge & experience with `Git <http://git-scm.com/book/en/>`_ and
`Github's forking model <http://gun.io/blog/how-to-github-fork-branch-and-pull-request/>`_.

If you are unfamiliar with Github please read about `forks <https://help.github.com/articles/fork-a-repo>`_ & `pull requests <https://help.github.com/articles/using-pull-requests>`_ before you proceed.

General guidelines about pull requests for this project
=======================================================

- Before submitting a pull request please ensure `your fork is up to date with the upstream <https://help.github.com/articles/syncing-a-fork>`_.
- If your contribution was made because an issue was previously opened on the subject please ensure that the last commit message contains `"Closes #issue-number" <https://help.github.com/articles/closing-issues-via-commit-messages>`_.
- When submitting the pull request please ensure you are requesting to merge it into the correct version or topic branch. **Pull requests against the master branch will not be merged**.

.. note::

    Pull requests containing offending commits **will not be merged** until they will be amended.

Contributing Documentation
==========================

The documentation is the most important aspect of any open source project since it serves as the face of the project.
It's the first thing you examine when you review a project.

Therefore, even if you are not a developer and you wish to contribute you can help a lot by improving the documentation.

If you have found a documentation bug, a typo or if you have found better phrasing feel
free to fork the project and submit a pull request.

This project uses `Sphinx <http://sphinx-doc.org/index.html>`_ as the documentation tool.
If you are unfamiliar with it please refer to the `Sphinx documentation <http://sphinx-doc.org/contents.html>`_ first.

Requirements
------------

In order to contribute documentation to nose2-testsuite you must have the following software installed:

- `Git <http://git-scm.com/book/en/Getting-Started-Installing-Git>`_
- `Python <http://python.org>`_ (Either `2.7 <http://python.org/download/releases/2.7.4/>`_, `3.2 <http://python.org/download/releases/3.2.4/>`_, `3.3 <http://python.org/download/releases/3.3.1/>`_ or `pypy <http://pypy.org/download.html>`_)
- `pip <https://pypi.python.org/pypi/pip>`_
- `Sphinx <http://sphinx-doc.org/index.html>`_
- `sphinx-bootstrap-theme <http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html>`_

Please follow the instructions on the provided links & on this document to install the required software.

.. note::

    If you are running on Windows note that you can use the `chocolatey package manager <http://chocolatey.org>`_ to install `Python 2.7.4 <http://chocolatey.org/packages/python>`_.

    If you are running on your favorite Linux distribution, it might have already provided the required Python version when you installed the distribution.

    In order to verify that simply type:

    .. code-block:: bash

        python --version

    If not, your package manager might provide it.

Required knowledge & experience
-------------------------------

- In order to edit the documentation you must be familiar with `reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_.

Building the documentation
--------------------------

In order to start contributing simply clone the repository or `your fork <https://help.github.com/articles/fork-a-repo>`_:

.. code-block:: bash

    # if you have already forked the project use https://github.com/<your-github-username>/nose2-testsuite.git instead
    git clone https://github.com/thedrow/nose2-testsuite.git
    cd nose2-testsuite

After that install the python dependencies

.. code-block:: bash

    pip install -r ./requirements/documentation.txt


.. note::

    While not required feel free to setup your own `virtualenv <https://pypi.python.org/pypi/virtualenv>`_ and install the required dependencies there.

Build the documentation to ensure everything is working properly.

.. code-block:: bash

    cd docs/
    make html
    cd ../

.. note::

    In order to save time you can simply type the following one-liner (assuming your current working directory is the project's root)

    .. code-block:: bash

        cd docs/ && make html && cd ../

If the build passes and the browser opens you can start editing the documentation immediately.

Guidelines
----------

.. note::

    This section is incomplete.
    As the documentation evolves more guidelines will be added.

- All new documentation files must have the *.rst extension.
- All documentation files must be named using lowercase letters with no spaces, hyphens or underscores.

Submitting a pull request with documentation changes
----------------------------------------------------

- The pull request's title must be descriptive.
- The description must summarize all the changes that were made in this pull request.
- If you fixed your own typo please `rebase <http://git-scm.com/book/en/Git-Branching-Rebasing>`_ the commit with the original commit in order to keep clean history. The same rule apply with rephrasing your own words for better clarity.

After you are done editing the documentation and you made sure your contribution follows the guidelines above please submit a `pull request <https://help.github.com/articles/using-pull-requests>`_.

If you followed the guidelines and the contribution is helpful the pull requests will be merged as soon as possible.

Design & Logo
-------------

The project is very new and thus does not have a unique design & logo yet.
It is currently not a priority but something I'd like to have in the future.

The documentation uses the amazing `bootstrap <http://twitter.github.io/bootstrap/>`_ css framework for styling.

If you'd like to contribute a logo or a new design do not hesitate to bring ideas or sketches to the `mailing list <https://groups.google.com/forum/?fromgroups#!forum/nose2-testsuite>`_.

You will be credited for your work and a link to your website and to a selection of social networks accounts you maintain
will appear on the documentation's footer.

Contributing Code
=================

Requirements
------------

In order to contribute code to nose2-testsuite you must have the following software installed:

- `Git <http://git-scm.com/book/en/Getting-Started-Installing-Git>`_
- `Python <http://python.org>`_ (Versions `2.6 <http://python.org/download/releases/2.6.8/>`_, `2.7 <http://python.org/download/releases/2.7.4/>`_, `3.2 <http://python.org/download/releases/3.2.4/>`_, `3.3 <http://python.org/download/releases/3.3.1/>`_ & `pypy <http://pypy.org/download.html>`_)
- `pip <https://pypi.python.org/pypi/pip>`_
- `virtualenv <https://pypi.python.org/pypi/virtualenv>`_
- `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ or `virtualenvwrapper-powershell <https://pypi.python.org/pypi/virtualenvwrapper-powershell>`_ if you are developing using windows.
- `nose2 <https://nose2.readthedocs.org/en/latest/>`_
- `tox <http://tox.readthedocs.org/en/latest/>`_
- `autopep8 <https://pypi.python.org/pypi/autopep8/>`_
- `pylint <http://www.pylint.org/>`_
- `travis-lint <https://github.com/travis-ci/travis-lint/>`_ if you are changing the build process.
- `Sphinx <http://sphinx-doc.org/index.html>`_
- `sphinx-bootstrap-theme <http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html>`_

.. warning::

    virtualenvwrapper-powershell is not stable enough and `currently it does not work with Python 3.x <https://bitbucket.org/guillermooo/virtualenvwrapper-powershell/pull-request/3/add-support-for-pip-installation-under/diff>`_.
    You can create your `virtualenv <http://www.virtualenv.org/en/latest/#usage>`_ without virtualenvwrapper-powershell but it is certainly less comfortable.

    Due to that the recommended development operating system is Linux.

Please follow the instructions on the provided links & on this document to install the required software.
