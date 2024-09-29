import os
import subprocess
from datetime import datetime

# Get user input for the "name" and "operation"
name = input("Enter the name of the operation: ")
adversary_id = input("Enter the adversary ID: ")

# Define the curl command with user input
curl_command = f'''curl -X PUT -H "KEY:ADMIN123" \
http://127.0.0.1:8888/api/rest \
-d '{{"index":"operations","name":"{name}","adversary_id":"{adversary_id}"}}' '''

# Execute the curl command right away
print("Executing the curl command immediately...")
subprocess.run(curl_command, shell=True)
print("Curl command executed right away.")

# Use a Linux path for the script (change this to your desired location)
script_path = '/tmp/run_curl.sh'

# Ensure the directory exists
os.makedirs(os.path.dirname(script_path), exist_ok=True)

# Create a shell script to run the curl command
with open(script_path, 'w') as f:
    f.write(f"#!/bin/bash\n")
    f.write(f"# This script was executed immediately on {datetime.now()}\n")
    f.write(f"{curl_command}\n")

# Make the script executable
os.chmod(script_path, 0o755)

# Generate a unique cron job comment using the operation name and current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
cron_comment = f"# RunCurlCommand_{name}_{timestamp}"

# Set the cron job to run the script monthly at midnight
cron_job = f'0 0 1 * * {script_path}'

# Add the cron job to the user's crontab
with open("/tmp/crontab.txt", "w") as f:
    subprocess.run(['crontab', '-l'], stdout=f)

with open("/tmp/crontab.txt", "a") as f:
    f.write(f"\n{cron_comment}\n{cron_job}\n")

# Install the new cron job
subprocess.run(['crontab', '/tmp/crontab.txt'])

# Final message
print(f"Cron job has been set to run {script_path} every month with a unique identifier: {cron_comment}.")
print(f"The curl command has already been executed and a script was created with a comment indicating it ran on {datetime.now()}.")

