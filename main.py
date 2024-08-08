#from functions import get_todo, write_todo
import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_prompt = input("Type add,show,edit,completed or exit:")
    todo = user_prompt.strip()
    if 'add' in user_prompt:
        a = input("Enter a todo: ") + "\n"

        todos = functions.get_todo("todo.txt")

        todos.append(a)

        functions.write_todo("todo.txt",todos)

    elif 'show' in user_prompt:
        todos = functions.get_todo("todo.txt")

        '''new_todos = []
        for i in todos:
            new_item = i.strip('\n')
            new_todos.append(new_item)'''
        
        new_todos = [i.strip('\n') for i in todos]  #list comprehension

        for index,item in enumerate(new_todos):
            #item = item.strip('\n')
            print(f"{index+1} - {item}")
        
        print(todos)

    elif 'edit' in user_prompt:
        try:
            num = int(input("Enter item number you wanna edit:"))
        
            todos = functions.get_todo("todo.txt")
            #print('Existing todos',todos)
        
            add = input("Enter new todo:") + '\n'
            todos[num-1] = add
            #print("the new todos: ", todos)

            functions.write_todo("todo.txt",todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif 'completed' in user_prompt:
        try:
            com = int(input("Enter the todo number that you've completed: "))
            todos = functions.get_todo("todo.txt")
            #print('exiting todos:', todos)
            a = todos[com-1].strip('\n')
            print(f"todo:{a} successfully removed.")
            todos.pop(com-1)

            #print('new todos:',todos)
            

            functions.write_todo("todo.txt",todos)
        except IndexError:
            print("Enter number within the list")
            continue
        
    elif 'exit' in user_prompt:
        break
    else :
        print("you typed incorrect prompt")