import os
import threading

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def sort_list(data):
    return sorted(data)

def process_file(file):
    data = read_file(file)
    sorted_data = sort_list(data)
    output_file = f"{os.path.splitext(file)[0]}_sorted.txt"
    write_file(output_file, sorted_data)

def gera_threads(input_files):
    threads = []

    for file in input_files:
        thread = threading.Thread(target=process_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

input_files = ['file1.txt', 'file2.txt', 'file3.txt']
gera_threads(input_files)