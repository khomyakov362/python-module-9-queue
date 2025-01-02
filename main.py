from QueueClass import Queue
from utils import get_public_methods_keys, call_object_method, get_help

working_queue = Queue()
keys = get_public_methods_keys(Queue)

user_input = ''

while user_input != 'quit':
    print(f'''\nInput the name of a method to call it.
The methods are {', '.join(keys)}.
To see documentation enter "help", to quit enter "quit".''')
    user_input = input('Enter your input: ').strip()

    if user_input in keys:
        call_object_method(working_queue, Queue, user_input)
    elif user_input == 'help':
        get_help(Queue, keys)
    elif user_input != 'quit':
        print('\nInvalid input.')
        continue
