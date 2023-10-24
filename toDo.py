tasks = [{"task":"Quran", "completed":True}, 
         {"task":"Salah", "completed":True}, 
         {"task":"Study", "completed":False}, 
         {"task":"Exercise", "completed":True}, 
         {"task":"Sleep", "completed":False}, 
         {"task":"Visit Hamada", "completed":True}]

def main():
    message = '''
    1 - add task
    2 - marked as completed
    3 - view tasks
    4 - quit
    '''
    while True:
        print(message)
        choice = input('Enter your choice:')
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_as_completed()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        else:
            print('invalid choice, please enter between 1 to 4')

def add_task():
    task = input('Enter the task:')
    input_task = {'task':task, 'completed':False}
    tasks.append(input_task)
    print('the task entered successfully')
    print(tasks)

def mark_as_completed():
    unCompleted_tasks = [task for task in tasks if task['completed'] == False]
    if not unCompleted_tasks:
        print('no tasks to marked as complete')
        return
    
    for i, task in enumerate(unCompleted_tasks):
        print(f'{i+1}- {task["task"]}')
    try:
        ch = int(input('choose the number of task that completed'))
        unCompleted_tasks[ch-1]['completed'] = True

        if ch < 1 or ch > len(unCompleted_tasks):
            print("invalid task number")
            return
        print('the task marked successfully')
    except ValueError:
        print("invalid input, please enter number")
    except IndexError:
        print('please choose from availabls numbers of tasks')
   
def view_tasks():
    if not tasks:
        print('no tasks to show')
        return
    for i, task in enumerate(tasks):
        if task['completed']:
            statue = '✔'
        else:
            statue = '❌'
        print(f'{i-+1}. {task["task"]} {statue}')

main()


     
