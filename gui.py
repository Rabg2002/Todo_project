import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")

window = gui.Window('My To-Do App', 
                    layout=[[label], [input_box, add_button]], 
                    font = ('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todo("todo.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
        case gui.WIN_CLOSED:
            break
    window.close()