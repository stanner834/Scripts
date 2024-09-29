import os
import requests
import subprocess
from datetime import datetime

# Get user input for the "name" and "operation"
name = input("Enter the name of the operation: ")
adversary_id = input("Enter the adversary ID: ")

# Define the API endpoint and headers
url = "http://127.0.0.1:8888/api/rest"
headers = {"KEY": "ADMIN123"}
data = {"index": "operations", "name": name, "adversary_id": adversary_id}

# Execute the HTTP request and capture the response
response = requests.put(url, headers=headers, json=data)

# Check if the HTTP request was successful
if response.status_code == 200:
    print("HTTP request was successful.")
else:
    print("HTTP request failed.")

# Create a unique timestamp for the script name
timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
script_path = os.path.join(os.environ['TEMP'], f'run_request_{timestamp}.bat')

# Create a batch script to run the HTTP request
with open(script_path, 'w') as f:
    f.write(f"@echo off\n")
    f.write(f"REM This script was executed immediately on {datetime.now()}\n")
    f.write(f"curl -X PUT -H \"KEY:ADMIN123\" \\\n")
    f.write(f"http://127.0.0.1:8888/api/rest \\\n")
    f.write(f"-d \"{{\\\"index\\\":\\\"operations\\\",\\\"name\\\":\\\"{name}\\\",\\\"adversary_id\\\":\\\"{adversary_id}\\\"}}\"\n")

# Create a unique task name using the current timestamp
unique_task_name = f"RunCurlCommand-{timestamp}"

# Command to create a scheduled task using schtasks
task_command = f'Schtasks /Create /SC MONTHLY /TN "{unique_task_name}" /TR "{script_path}" /ST 00:00 /F'

# Run the task scheduler command
subprocess.run(task_command, shell=True)

# Final message indicating the task was created
print(f"Task Scheduler job '{unique_task_name}' has been created to run '{script_path}' every month at 00:00.")
