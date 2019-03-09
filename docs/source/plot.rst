Matplotlib Support
==================

Another great feature would be to allow use of the
`matplotlib plot directive <https://matplotlib.org/devel/plot_directive.html>`_,
for example:

.. plot::

    import matplotlib.pyplot as plt 
    plt.plot([0,1], [2, -2])

This should show a really simple scatter plot as an image above.

The "plot" directive is provided by the adding 
`"matplotlib.sphinxext.plot_directive"` to the list of sphinx extensions.