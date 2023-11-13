def yourtask():
    '''This function tell your remaining task, type the task number that you want to know about it"

    :returns: your task.
    :rtype: str

    Example

    .. code-block:: python

        task number(1,2,3): 1

    Output

    .. code-block:: python

        study git

    Task number & Return statement

    +-------------+---------------------------------------+
    | Task number |            return statement           |        
    +=============+=======================================+
    |      1      |                study git              |
    +-------------+---------------------------------------+
    |      2      | study sphinx & personal sphinx project|
    +-------------+---------------------------------------+
    |      3      |       learn Ammonite source code      |
    +-------------+---------------------------------------+

    '''
    task_num = input("task number(1,2,3): ")
    if task_num == "1":
        task = "study git"
        print(task)
    if task_num == "2":
        task = "study sphinx & personal sphinx project"
        print(task)
    if task_num == "3":
        task = "learn Ammonite source code"
        print(task)


    