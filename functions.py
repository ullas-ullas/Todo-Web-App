FILEPATH = 'todos.txt'
def get_todos(path = FILEPATH):
    """ Reads a text file and returns a list of lines"""
    with open(path, 'r') as file_local:
        local_todo = file_local.readlines()
    return local_todo


def write_todos(todos_local, path=FILEPATH):
    """ Write a list onto a text file"""
    with open(path, 'w') as file_loc:
        file_loc.writelines(todos_local)


if __name__ == "main":
    print("HI")         # doesn't execute if main calls functions, only executes when functions is exec.

