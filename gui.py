import functions
import FreeSimpleGUI as gui

file= 'Projects/Todo_list/myvenv/todo.txt'
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todo(file), key ='todos', 
                        enable_events=False , size=[45, 10])
edit_button = gui.Button("Edit")

window= gui.Window('My To-Do App', 
                    layout=[ [label] , [input_box, add_button], [list_box, edit_button]], 
                    font = ('Helvetica', 10))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todo(file) 
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo( todos, file)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todo(file)  
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos, file)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'])
        case gui.WIN_CLOSED:
            break
window.close()