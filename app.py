import os

print("===== Python Application Started =====")

name = os.getenv("APP_NAME", "DefaultApp")
env = os.getenv("ENVIRONMENT", "DEV")

print(f"Application : {name}")
print(f"Environment : {env}")

print("Hello from GitHub Actions!")

print("===== Python Application Completed =====")
