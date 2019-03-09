example package
=========================

example.function module
----------------------------------

.. automodule:: example.function
    :members:
    :undoc-members:
    :show-inheritance:

example code block
------------------

First code block below is in python syntax, showing line numbering and emphasizing line 2:

.. code-block::
    :language: python
    :linenos:
    :emphasize-lines: 2

    import math
    print(math.sqrt(9))


Second is in bash:

.. code-block:: 
    :language: bash
     
    echo "some stuff" 1>&2
    ls /etc/


(and using hightlight directive):

.. highlight:: bash
     
    echo "some stuff" 1>&2
    ls /etc/


Finally a literal include:

.. literalinclude:: example.py
   :language: python
   :emphasize-lines: 2
   :linenos:


example image
-------------

An image should be included below (with hyperlink):

.. image:: Git-Icon-Black.png
   :target: https://github.com/codejamninja/sphinx-markdown-builder

example ReST table
-------------------

The following Python packages are used for the example:

+----------------------------------------------------------------------+----------------------------+---------------------------------------------------------------------------+
| Package                                                              | License                    | Notes                                                                     |
+======================================================================+============================+===========================================================================+
| `NavPy == 1.0 <https://navpy.readthedocs.io/en/latest/>`_            | BSD                        | NavPy is pretty cool                                                      |
+----------------------------------------------------------------------+----------------------------+---------------------------------------------------------------------------+
| `aero-calc >= 0.13.2 <https://pypi.org/project/aero-calc/>`_         | BSD                        | Forked from `AeroCalc <https://kilohotel.com/python/aerocalc/>`_).        |
|                                                                      |                            | Used in aerospace stuff.                                                  |
+----------------------------------------------------------------------+----------------------------+---------------------------------------------------------------------------+
