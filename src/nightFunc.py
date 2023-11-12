def nightfunc(name):
    '''Greeting function for this module, tell me what your name and i'm gonna greet you!

    :param str name: input your name.

    :returns: greeting word.
    :rtype: str

    Example

    .. code-block:: python

        myGreet = nightfunc(name='Nontaphat')
        print(myGreet)

    Output

    .. code-block:: python

        "Hello Nontaphat!. My name is Night. Nice to meet you!"

    '''
    greet = "Hello {}!. My name is Night. Nice to meet you!".format(name)
    return greet
