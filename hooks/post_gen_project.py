import subprocess

MESSAGE_COLOR = "\x1b[1;32m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Running post_gen_project.py...{RESET_ALL}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print("{MESSAGE_COLOR}Done!{RESET_ALL}")
