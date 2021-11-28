import os

path_in_catalog = os.getcwd()

def my_func_sort(path):
    os.listdir(path)
    all_files_in_dir = []
    my_dict = {}
    for files in os.listdir(path):
        if files.endswith('.txt'):
            all_files_in_dir.append(files)
    for name_file in all_files_in_dir:
        with open(name_file, encoding='utf-8') as file:
            all_s = []
            for strings in file:
                all_s.append(strings)
                len_file_name = len(all_s)
        with open(name_file, encoding='utf-8') as file:
            data_file = file.read().strip().split('\n')
            my_dict.setdefault(name_file, (len_file_name, data_file))
    sort_list = sorted(my_dict.items(), key=lambda x: x[1][0])

    for n_file, strig in sort_list:
        with open('new_file.txt', 'at', encoding='utf-8') as file:
            file.write(f'{n_file}\n')
            file.write(f'{str(strig[0])}\n')
            for aing in strig[1]:
                file.write(f'{aing}\n')

my_func_sort(path_in_catalog)