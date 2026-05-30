import subprocess
from datetime import datetime

# nginx
nginx = subprocess.run(
    ["service", "nginx", "status"],
    capture_output=True,
    text=True
)

if "running" in nginx.stdout:
    nginx_status = "RUNNING"
else:
    nginx_status = "DOWN"

# RAM
memory = subprocess.run(
    ["free", "-h"],
    capture_output=True,
    text=True
)

# Disk
disk = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

time_now = datetime.now()

with open("health.log", "a") as file:
    file.write("\n")
    file.write("=" * 50 + "\n")
    file.write(f"Time: {time_now}\n")
    file.write(f"Nginx: {nginx_status}\n")
    file.write("\nRAM:\n")
    file.write(memory.stdout)
    file.write("\nDisk:\n")
    file.write(disk.stdout)

print("Health check completed")
