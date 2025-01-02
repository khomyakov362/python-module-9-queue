from QueueClass import Queue

def get_public_methods_keys(class_object : type) -> tuple:
    class_dict = class_object.__dict__
    methods_names = tuple(filter(lambda string: string[0] != '_', class_dict.keys()))
    return methods_names

def call_object_method(object_of_class : object, class_object : type, method_name : str) -> None:
    class_dict = class_object.__dict__
    try:
        return_value = class_dict[method_name](object_of_class)
    except TypeError:
        input_data = input('The method requires an additional argument: ')
        return_value = class_dict[method_name](object_of_class, input_data)
    
    print(f'\nThis is the return value of method {method_name}: {return_value}')

def get_help(class_object : type, method_tuple : tuple) -> None:
    for method_name in method_tuple:
        help(class_object.__dict__[method_name])
        print()

