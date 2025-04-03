import os

def shutdown_pc():
    os.system("shutdown /s /t 1")  # Shuts down Windows in 1 second

print("Warning! This will turn off your computer.")
answer = input("Are you sure? (yes/no): ")

if answer.lower() == "yes":
    shutdown_pc()
else:
    print("Cancelled")