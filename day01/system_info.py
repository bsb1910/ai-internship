import platform
from datetime import datetime

print("=== System Information ===")

print("Operating System :", platform.system())
print("OS Version       :", platform.version())
print("Python Version   :", platform.python_version())
print("Current Time     :", datetime.now())