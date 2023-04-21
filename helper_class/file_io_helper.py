import random
import socket
import os

def remove_data_from_file(removedData, file_name):
    with open(f"csv_file/{file_name}.csv", 'r') as f:
        list_data = f.readlines()
    new_list_data = [
        data for data in list_data if removedData not in data]
    with open(f"csv_file/{file_name}.csv", 'w') as f:
        f.writelines("".join(new_list_data))

def get_first_data_from_file(file_name):
    with open(f"csv_file/{file_name}.csv", 'r') as f:
        return  f.readlines()[0].replace("\n","")

def get_random_data_from_file(file_name):
    with open(f'csv_file/{file_name}.csv', 'r') as f:
        list_data = [data.replace("\n","") for data in f.readlines()]
        return list_data[random.randrange(len(list_data))]
        
def get_all_data_as_list_from_file(file_name):
    with open(f"csv_file/{file_name}.csv", 'r') as f:
        return [data.replace("\n", "") for data in f.readlines() if data != ""]

def save_new_data(data, file_name):
    with open(f"csv_file/{file_name}.csv", "a") as f:
        f.writelines(f"{data}\n")

def keep_log_data(data, additional_data = "", file_name = "data"):
    with open(f"csv_file/{file_name}.log", "a") as f:
        f.writelines(f"{data} {additional_data}\n")

def get_machine_name():
    return socket.gethostname()

def create_csv_directory():
    csv_directory = "csv_file"
    if not os.path.exists(csv_directory):
        os.makedirs(csv_directory)
    return csv_directory