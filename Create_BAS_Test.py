import os
import subprocess

# Get user input for the "name" and "operation"
name = input("Enter the name of the operation: ")
adversary_id = input("Enter the adversary ID: ")

# Define the curl command with user input
curl_command = f'''curl -X PUT -H "KEY:ADMIN123" \
http://127.0.0.1:8888/api/rest \
-d '{{"index":"operations","name":"{name}","adversary_id":"{adversary_id}"}}' '''

# Use a Windows path for the script (change this to your desired location)
script_path = 'C:\\tmp\\run_curl.bat'

# Ensure the directory exists
os.makedirs(os.path.dirname(script_path), exist_ok=True)

# Create a batch file to run the curl command
with open(script_path, 'w') as f:
    f.write(f"@echo off\n{curl_command}\n")

# Set the cron job (Windows equivalent: Task Scheduler)
# You can't use crontab in Windows, so we'll use Task Scheduler with PowerShell
task_command = f'Schtasks /Create /SC MONTHLY /TN "RunCurlCommand" /TR "{script_path}" /ST 00:00'

# Run the task scheduler command
subprocess.run(task_command, shell=True)

print(f"Cron job (Task Scheduler) has been set to run {script_path} every month.")


# To add Elastic export rules script? How can we do this with the Yaml file