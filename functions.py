FILENAME = "todo.txt"

def get_todo(filename=FILENAME):
    with open(filename, 'r') as file:
        todos = file.readlines()

    return todos

def write_todo(todo, filename=FILENAME):
    with open(filename, 'w') as file:
        file.writelines(todo)

if __name__ == "__main__":
    a = get_todo("todo.text")
    print(a)
    
