import os
import subprocess

# Define the curl command you want to run
curl_command = '''curl -X PUT -H "KEY:ADMIN123" \
http://127.0.0.1:8888/api/rest \
-d '{"index":"operations","name":"testoperation1","adversary_id":"d69e8660-62c9-431e-87eb-8cf6bd4e35cT"}' '''

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


