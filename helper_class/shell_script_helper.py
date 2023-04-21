import os


def execute_command(command):
    os.system(command)

def execute_command_with_root(command, root_password):
    os.system(f"echo '{root_password}' | sudo -S {command}")
