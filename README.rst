========================
ChangeTip Python Library
========================

A set of tools for interacting with the ChangeTip API - https://www.changetip.com/api/

Install
=======
.. code-block:: bash

    $ pip install changetip

Examples
========

.. code-block:: python

    from changetip.bots.base import BaseBot

    class YourBot(BaseBot):

        def check_for_new_tips(self)
            # Code to check for new tips
            pass

To see it in action, checkout the [ChangeTip Slack bot](https://github.com/changecoin/changetip-slack), which uses this library.

Tests
=====
CircleCI test status:

.. image:: https://circleci.com/gh/changecoin/changetip-python.svg?style=svg
    :target: https://circleci.com/gh/changecoin/changetip-python


To run tests:

.. code-block:: bash

    $ python setup.py test

Local Development
=================

Source code - [ChangeTip Python on Github](https://github.com/changecoin/changetip-python)

If you would like to post API messages locally instead of production (https://api.changetip.com/v1), you can pass the environemnt variable `CHANGECOIN_API`. For example:

.. code-block:: bash

    $ CHANGECOIN_API=http://localhost/v1/ python yourcode


License
=======
MIT
