
def send_message_display_helper(str_in : str) -> str:
    '''
    Helper function to mySimpleSocketObj.send_msg()
        that will help in formatting messages ent over so the user
        can see special characters like "\n", "\r\n\r\n", and "\n\n\n".
        Existence of different combinations of characters in the string
        may be formatted incorrectly.
    :param str_in: a string to be formatted. The only special characters that
        should exist in the string are "\n", "\r\n\r\n", and "\n\n\n". Errors
        may occur if other combinations exist like \n\n or \r or \r\r\r\r.
    :return: a formatted string.
    '''
    replaced_0 = str_in.replace("\n", "\\n\n")
    replaced_1 = replaced_0.replace("\r\\n\n\r\\n\n", "\\r\\n\\r\\n\r\n\r\n")
    return replaced_1.replace("\\n\n\\n\n\\n\n ", "\\n\\n\\n\n\n\n")