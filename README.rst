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


Tests
=====
CircleCI test status:

.. image:: https://circleci.com/gh/changecoin/changetip-python.svg?style=svg
    :target: https://circleci.com/gh/changecoin/changetip-python


To run tests:

.. code-block:: bash

    $ python setup.py test


License
=======
MIT
