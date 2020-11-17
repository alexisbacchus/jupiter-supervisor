#!/bin/python3
import subprocess, json
from colors import bcolors

def get_listenports():
    bash_command = "./netcommand.sh"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    processed_output = output.decode().strip().splitlines()
    return processed_output

def get_datadict():
    data_file_name = "data.json"
    jdump = {}
    with open(data_file_name) as f:
        data = f.read()
    jdump = json.loads(data)
    return jdump

MODULES_DICT = get_datadict()
accessible_ports = get_listenports()
accessible_modules = {}

for current_port in MODULES_DICT:
    if current_port in accessible_ports:
        accessible_modules[current_port] = MODULES_DICT[current_port]
    else :
        print("{}NOT ALIVE : {}{}".format(
            bcolors.FAIL,
            MODULES_DICT[str(current_port)],
            bcolors.ENDC
            ))

for key, value in accessible_modules.items():
    print("{}OK : {} on port {}{}".format(bcolors.OKGREEN,value, key,bcolors.ENDC))
