# from funtions import get_todos,write_todos
import funtions
import time
# import funtions

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_actions=input("Type add, show,edit or exit :")
    user_actions=user_actions.strip()

    if user_actions.startswith("add"):
        todo=user_actions[4:]

        todos=funtions.get_todos()

        todos.append(todo + '\n')

        funtions.write_(todos)

    elif user_actions.startswith("show"):

        todos = funtions.get_todos()

        for index,item in enumerate(todos):
            new_item=item.strip('\n')
            row=f"{index+1}-{new_item}"
            print(row)


    elif user_actions.startswith("edit"):
        try:
            number=int(user_actions[5:])
            print(number)
            number=number-1

            todos = funtions.get_todos()

            new_todo=input("Enter the new todo: ")
            todos[number]=new_todo + '\n'

            funtions.write_todos(todos)

        except ValueError:
            print("Please enter valid input.")
            continue

    elif user_actions.startswith("complete"):
        try:
            number = int(user_actions[9:])

            todos = funtions.get_todos()

            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            funtions.write_todos(todos)

            message=f"Todo {todo_to_remove} was removed from list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_actions.startswith("exit"):
        break

    else:
        print("Command is not valid..!")
print("Bye!")