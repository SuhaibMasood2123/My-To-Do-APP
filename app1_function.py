
def get_todos(filepath = 'todos.txt'):
    """ Reads the text file and return the list  of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos_arg, filepath='todos.txt', ):
    """ Write the text file with the to-dos items. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
