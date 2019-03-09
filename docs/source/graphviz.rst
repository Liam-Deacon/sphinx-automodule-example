Graphviz support
================

Another great feature would be inclusion of graphs given by the 
`graphviz <https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`_ 
directive for example:

.. graphviz::

    digraph foo {
        "eggs" -> "breakfast";
    }


Should show breakfast being dependent on eggs as an image above.

There should also be a note below stating which extension enables graphviz:

.. note::
    The "graphviz" directive is provided by `sphinx.ext.graphviz`.
