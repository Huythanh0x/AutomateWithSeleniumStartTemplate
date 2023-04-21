import os
from helper_class import stored_parameters_helper

def resize_all_vm_windows_commands():
    list_commands = []
    machine_idx = 0
    for row_idx in range(NUMBER_OF_VM_IN_COLUMN)[::1]:
        for column_idx in range(NUMBER_OF_VM//NUMBER_OF_VM_IN_COLUMN)[::1]:
            machine_idx += 1
            vm_height = (MONITOR_HEIGHT-TOP_BAR_VIRTUAL_SIZE)//NUMBER_OF_VM_IN_COLUMN
            vm_width = (MONITOR_WIDTH)//(NUMBER_OF_VM//NUMBER_OF_VM_IN_COLUMN)
            if column_idx < (NUMBER_OF_VM//NUMBER_OF_VM_IN_COLUMN//2):
                vm_width -= DOCK_WIDTH//(NUMBER_OF_VM//NUMBER_OF_VM_IN_COLUMN//2)
                machine_x = DOCK_WIDTH + column_idx*vm_width
            else: 
                machine_x = column_idx*vm_width
            machine_y = row_idx*vm_height
            if row_idx != 0:
                machine_y += TOP_BAR_VIRTUAL_SIZE
            command = f"wmctrl -i -r $(wmctrl -l | grep 'cambly-server-v{machine_idx}' | awk '{{print $1}}') -e 0,{machine_x},{machine_y},{vm_width},{vm_height}"
            list_commands += [command]
    os.system(";".join(list_commands))



def shutdown_all_vm(server_name_prefix):
    list_command =  [f"vboxmanage controlvm {server_name_prefix}{idx+1} poweroff" for idx in range(NUMBER_OF_VM)]
    os.system("&".join(list_command))

def start_all_vm(server_name_prefix):
    list_command =  [f"vboxmanage startvm {server_name_prefix}{idx+1}& sleep 1" for idx in range(NUMBER_OF_VM)]
    os.system(";".join(list_command))

def set_resolution_dual_monitors():
    os.system('cvt 5120 1296 30 ;sudo xrandr --newmode "5120x1296"  261.00  5120 5336 5856 6592  1296 1299 1309 1321 -hsync +vsync; sudo xrandr --addmode HDMI-2 "5120x1296"; sudo xrandr --output HDMI-2 --mode "5120x1296"')


def visual_sensors(interval_time = 0.5):
    os.system(f"while true; do sensors; sleep {interval_time}; clear; done")

def resize_application_window(application_name, width, height):
    vm_height_resolution = int(str(os.popen("xrandr | grep '*' | awk '{print $1}' | cut -d'x' -f2").read()).split("\n")[0])
    os.system(f"wmctrl -i -r $(wmctrl -l | grep '{application_name}' | awk '{{print $1}}') -e 0,0,{vm_height_resolution-height-40},{width},{height}")


NUMBER_OF_VM = 4
TOP_BAR_VIRTUAL_SIZE = 100
DOCK_WIDTH = 40
NUMBER_OF_VM_IN_COLUMN = 2
MONITOR_HEIGHT = 1300
MONITOR_WIDTH = 5120
if NUMBER_OF_VM <= 4: NUMBER_OF_VM_IN_COLUMN = 1