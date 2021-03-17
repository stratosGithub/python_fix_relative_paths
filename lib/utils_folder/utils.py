import os

this_dir = os.path.dirname(os.path.realpath(__file__))

def correct_path(path, root=this_dir):
    return os.path.realpath(os.path.join(this_dir, path))

def correct_path_from_root_of_project(path):
    return os.path.realpath(os.path.join(this_dir, '../../', path))

def print_name_of_file():
    print(f"Current file is: {__file__} and current name is: {__name__}")

def print_first_list_of_file(file_path):
    with open(file_path, "r") as f:
        l = f.readline()
        print(l)



if __name__ == "__main__":
    print_name_of_file()
    filepath = correct_path('util_assets/test_file_C.txt')
    print_first_list_of_file(filepath)

    filepath2 = correct_path_from_root_of_project('assets/test_file_A.txt')
    print_first_list_of_file(filepath2)

