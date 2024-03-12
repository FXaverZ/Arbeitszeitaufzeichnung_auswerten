# evaluate_working_time_recording
Tool to evaluate my working time records.

## Python Version

Tested with Python v3.11

Use the module best within a virtual environment. To create a new environment use
``` sh
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
python -m venv .venv
# You can also use 
py -3.11 -m venv .venv
```

Activate the environment with
``` sh
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Use the provided `requirements.txt` (if present) to install all needed python packages
```sh
pip install -r ./requirements.txt
```

If packages were added or updated, use 
```sh
pip freeze > ./requirements.txt
```
to save this new dependencies. Commit these changes!