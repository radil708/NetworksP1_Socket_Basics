import sys

def getArgs():
    '''
    Get the arguments passed
    :return: a list that omits the first argument(program name)
    '''
    l1 = sys.argv
    return l1[1:]

def check_args(list_args):
    '''
    Creates a dictionary of valid arguments. Throws an error if the amount of args
    is incorrect or is missing the required -s flag.
    :param list_args: a list of arguments passed
    :return: a dictionary of valid arguments with the following keys = port, host, neu
    '''
    dict_arg = {}

    # check correct amount of args
    if "-p" not in list_args and (len(list_args) < 3 or len(list_args) > 3):
        error_msg = "Not enough arguments passed. Arguments must be of format:" + \
                    "\n-p <port> <-s> <hostname> <NEU email prefix>\nor\n" + \
                    "<-s> <hostname> <NEU email prefix>"
        raise ValueError(error_msg)

    # s flag is required according to instructions
    if "-s" not in list_args:
        raise ValueError("Missing required -s flag")

    if "-p" not in list_args:
        dict_arg["port"] = 27995
        dict_arg["host"] = list_args[1]
        dict_arg["neu"] = list_args[2]
    else:
        dict_arg["port"] = list_args[1]
        dict_arg["host"] = list_args[3]
        dict_arg["neu"] = list_args[4]

    return dict_arg



