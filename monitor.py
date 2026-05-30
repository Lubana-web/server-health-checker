import subprocess
from datetime import datetime

result = subprocess.run(
    ["service", "nginx", "status"],
    capture_output=True,
    text=True
)

status = result.stdout.strip()

time_now = datetime.now()

with open("monitor.log", "a") as file:
    file.write(f"{time_now} - nginx status: {status}\n")

print(status)

if "running" in status:
    print("Nginx is healthy")
else:
    print("Nginx is DOWN")
