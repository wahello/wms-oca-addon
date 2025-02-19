==========================================
Stock Available to Promise Release - Block
==========================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:c4fcf8d2a69cc69523b8d67f30fe066696669c88bacd237d55f1e3b652195eda
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fwms-lightgray.png?logo=github
    :target: https://github.com/OCA/wms/tree/16.0/stock_available_to_promise_release_block
    :alt: OCA/wms
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/wms-16-0/wms-16-0-stock_available_to_promise_release_block
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/wms&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows to block and unblock release of deliveries.

It can also automatically block backorders if goods to deliver are not available.

**Table of contents**

.. contents::
   :local:

Usage
=====

Deliveries can be blocked and unblocked manually with the respective buttons.

A new option *Auto-block Release on Backorders* is also available if
*Release based on Available to Promise* is enabled on a delivery route.
This option will automatically block a backorder if the goods to deliver are
not available.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/wms/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/wms/issues/new?body=module:%20stock_available_to_promise_release_block%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Camptocamp
* ACSONE SA/NV
* BCIM

Contributors
~~~~~~~~~~~~

* ACSONE SA/NV
* BCIM:
  * Jacques-Etienne Baudoux <je@bcim.be>
* Camptocamp:
  * Sébastien Alix <sebastien.alix@camptocamp.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/wms <https://github.com/OCA/wms/tree/16.0/stock_available_to_promise_release_block>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
