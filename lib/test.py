from .utils_folder.utils import correct_path, print_name_of_file, print_first_list_of_file, correct_path_from_root_of_project


if __name__ == "__main__":
    print_name_of_file()
    filepath = correct_path_from_root_of_project('assets/test_file_A.txt')
    filepath2 = correct_path_from_root_of_project('lib/lib_assets/test_file_B.txt')
    filepath3 = correct_path_from_root_of_project('lib/utils_folder/util_assets/test_file_C.txt')

    print_first_list_of_file(filepath)
    print_first_list_of_file(filepath2)
    print_first_list_of_file(filepath3)
