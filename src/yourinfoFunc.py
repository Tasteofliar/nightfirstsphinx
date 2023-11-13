def yourinfo(name,age,gender):
    '''This function give me your information, so please fill in the information truthfully ;)

    :param str name: input your name.
    :param int age: input your age.
    :param str name: input your gender.

    :returns: your Personal information.
    :rtype: str

    Example

    .. code-block:: python

        myinfo = yourinfo("Nontaphat","20","Male")
        print(myinfo)

    Output

    .. code-block:: python

        name: Nontaphat
        age: 20
        gender: Male

    '''
    profile = "name: {}\nage: {}\ngender: {}".format(name,age,gender)
    return profile
