import uuid


def show_tasks():
    print("\n[YOUR TASKS]")
    task_show = read_to_todo_list()
    task_no = 1
    line = ""
    if task_show == None or task_show == "Empty list":
        print('\nEmpty list\nNo tasks to show')
    else:
        for char in task_show:
            line += char
            if char == '\n':
                line = line.strip('\n').split(';')
                new_line = line[1].strip() + " | " + line[2].strip()
                print(f"{task_no}: {new_line}")
                line = ""
                task_no += 1
        return task_show


def add_task():
    new_task = input("\n[ADD TASK]\nWhat is the task? ").strip().lower()
    task_due = input("What is the deadline? ").strip().lower()
    task_id = str(uuid.uuid4())
    todo_task = task_id + ";" + new_task + ";" + task_due + "\n"

    write_to_todo_list(todo_task, write_state='a')


def complete_task():
    print("\n[COMPLETE TASK]\n")
    task_show = show_tasks()

    line = ""
    list_of_tasks = []
    current_tasks = read_to_todo_list()
    for char in current_tasks:
        line += char
        if char == '\n':
            list_of_tasks.append(line)
            line = ""

    if task_show == None or task_show == "Empty list":
        pass
    else:
        complete_task_no = int(input('\nEnter task number to complete: '))
        complete_task_no -= 1
        list_of_tasks.pop(complete_task_no)

        write_tasks = ""
        for tasks in list_of_tasks:
            write_tasks += tasks

        write_to_todo_list(write_tasks)


def write_to_todo_list(todo_tasks, write_state='w'):
    with open(todo_file, write_state) as file:
        file.write(todo_tasks)


def read_to_todo_list():
    with open(todo_file, 'r') as file:
        contents = file.read()
    if len(contents) == 0:
        contents = "Empty list"
    return contents


def run():
    menu = "\n== TODO LIST ==\n\n\
  1) show tasks\n\
  2) add task\n\
  3) complete task\n\
\n\
  X) EXIT\n\
  >>  "

    try:
        while True:
            try:
                usr_input = input(menu).strip().lower()
                if usr_input == '1':
                    show_tasks()
                elif usr_input == '2':
                    add_task()
                elif usr_input == '3':
                    complete_task()

                elif usr_input == 'x':
                    print('\nThanks for playing!')
                    break
                else:
                    print('\ncommand not recognized')
                input('\npress enter to continue')
            except IndexError:
                print('\nNumber not found, try again.')
            except FileNotFoundError:
                print('\nNo todo list found, add a task to get started.')
    except KeyboardInterrupt:
        print('\nctrl+c')


if __name__ == '__main__':
    todo_file = "todo_list.txt"
    run()

print('\nGoodbye!')
