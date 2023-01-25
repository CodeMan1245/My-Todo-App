FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        res = []
        for sub in todos_local:
            res.append(sub.replace("\n", ""))
        return res


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        print()
        res = []
        for todo in todos_arg:
            res.append(todo + '\n')
        todos_local = file.writelines(res)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
