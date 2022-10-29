Things to do while releasing a new version
==========================================

This file is a memo for the maintainer.


0. Checks
---------

* If imagequant has been updated, ensure ``MANIFEST.in`` is up to date,
  generate an sdist package and check we are able to build a wheel from it.


1. Release
----------

* Update version number in ``setup.py``
* Edit / update changelog in ``README.rst``
* Commit / tag (``git commit -m vX.Y.Z && git tag vX.Y.Z && git push && git push --tags``)


2. Publish PyPI package
-----------------------

Publish source dist and wheels on PyPI.

→ Automated :)


3. Publish Github Release
-------------------------

* Make a release on Github
* Add changelog
