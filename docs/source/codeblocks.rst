example code block
------------------

First code block below is in python syntax, showing line numbering and emphasizing line 2:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import math
    print(math.sqrt(9))


Second is in bash:

.. code-block:: bash

    echo "some stuff" 1>&2
    ls /etc/


(and using highlight directive):

.. highlight:: bash

::

    echo "some stuff" 1>&2
    ls /etc/


Finally a literal include:

.. literalinclude:: example.py
   :language: python
   :emphasize-lines: 2
   :linenos:

