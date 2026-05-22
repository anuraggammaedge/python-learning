import platform
import sys
from pathlib import Path
import os
import subprocess

# ANSI Escape Codes for Styling
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

# 1. Check Python Version
python_version = platform.python_version()

if sys.version_info < (3, 8):
    sys.exit(f"{RED}{BOLD}Error: Python 3.8 or higher is required. Current version: {python_version}{RESET}")

# Dictionary to track the status of our operations
report_status = {
    "Python Version": f"{GREEN}{python_version} (Compatible){RESET}",
    "Sub-folders": [],
    "Requirements": "Failed",
    "Gitignore": "Failed",
    "Virtual Env": "Failed",
    "Pip Install": "Skipped"
}

# 2. Setup Project Root Directory
project_dir = str(input(f"{CYAN}Enter the name of your project directory: {RESET}")).strip()
script_dir = Path(__file__).parent / project_dir
if not script_dir.exists():
    script_dir.mkdir()
    report_status["Root Directory"] = f"{GREEN}Created{RESET}"
else:
    report_status["Root Directory"] = f"{YELLOW}Already Exists{RESET}"

# 3. Setup Sub-folders
sub_folders = ['src', 'tests', 'docs', 'logs']

for folder in sub_folders:
    folder_path = script_dir / folder
    if not folder_path.exists():
        folder_path.mkdir()
        report_status["Sub-folders"].append(f"{GREEN}{folder}/{RESET}")
    else:
        report_status["Sub-folders"].append(f"{YELLOW}{folder}/ (Skipped){RESET}")

# 4. Generate requirements.txt
basic_packages = [
    "requests>=2.31.0",
    "pandas>=2.1.0",
    "python-dotenv>=1.0.0",
    "pytest>=7.4.0"
]

try:
    requirements_file = script_dir / 'requirements.txt'
    requirements_file.write_text("\n".join(basic_packages) + "\n", encoding="utf-8")
    report_status["Requirements"] = f"{GREEN}Generated successfully{RESET}"
except Exception as e:
    report_status["Requirements"] = f"{RED}Failed ({str(e)}){RESET}"

# 5. Generate .gitignore
gitignore_path = script_dir / '.gitignore'
gitignore_content = """# Byte-compiled
__pycache__/
*.py[cod]

# Environments
.venv/
venv/
env/

# Project-specific logs
logs/
*.log

# OS & IDEs
.DS_Store
.vscode/
.idea/

# Secrets
.env
"""

try:
    gitignore_path.write_text(gitignore_content, encoding='utf-8')
    report_status["Gitignore"] = f"{GREEN}Generated successfully{RESET}"
except Exception as e:
    report_status["Gitignore"] = f"{RED}Failed ({str(e)}){RESET}"

# Virtual Environment Setup

virtual_env_name = input(f"{CYAN}Enter a name for your virtual environment (or press Enter to skip): {RESET}").strip()
if virtual_env_name:
    venv_path = script_dir / virtual_env_name
    if not venv_path.exists():
        try:
            subprocess.run([sys.executable, '-m', 'venv', str(venv_path)], check=True)
            report_status["Virtual Env"] = f"{GREEN}Created successfully (.venv/){RESET}"
        except subprocess.CalledProcessError as e:
            report_status["Virtual Env"] = f"{RED}Creation Failed ({str(e)}){RESET}"
else:
    report_status["Virtual Env"] = f"{YELLOW}Already Exists (Skipped Build){RESET}"


if os.name == "nt":
    pip_executable = venv_path / "Scripts" / "pip.exe"
else:
    pip_executable = venv_path / "bin" / "pip"

# Execute installation using the isolated virtual environment pip
if pip_executable.exists() and requirements_file.exists():
    try:
        print(f"{CYAN}Installing packages inside virtual environment... Please wait...{RESET}")
        subprocess.run([str(pip_executable), "install", "-r", str(requirements_file)], check=True, stdout=subprocess.DEVNULL)
        report_status["Pip Install"] = f"{GREEN}All packages installed successfully{RESET}"
    except Exception as e:
        report_status["Pip Install"] = f"{RED}Installation Failed ({str(e)}){RESET}"
else:
    report_status["Pip Install"] = f"{RED}Failed (Missing pip engine or requirements.txt){RESET}"




# PRINT COLORFUL STATUS REPORT
print("\n")
print(f"{BLUE}{BOLD}==================================================={RESET}")
print(f"{CYAN}{BOLD}             ENVIRONMENT SETUP REPORT              {RESET}")
print(f"{BLUE}{BOLD}==================================================={RESET}")
print(f"{BOLD}Python Engine:{RESET}     {report_status['Python Version']}")
print(f"{BOLD}Project Root:{RESET}      {script_dir.resolve()}")
print(f"{BOLD}Root Status:{RESET}       {report_status['Root Directory']}")
print(f"{BLUE}---------------------------------------------------{RESET}")
print(f"{BOLD}Target Structures Created:{RESET}")
for folder_status in report_status["Sub-folders"]:
    print(f"  • {folder_status}")
print(f"{BLUE}---------------------------------------------------{RESET}")
print(f"{BOLD}File Configurations & Environment:{RESET}")
print(f"  • requirements.txt: {report_status['Requirements']}")
print(f"  • .gitignore:       {report_status['Gitignore']}")
print(f"  • Virtual Env (.venv): {report_status['Virtual Env']}")
print(f"  • Dependency Sync:   {report_status['Pip Install']}")
print(f"--")
print(f"{BOLD}How to activate manually in terminal:{RESET}")
if os.name == "nt":
    print(f"  {YELLOW}cd {script_dir} && .\\.venv\\Scripts\\activate{RESET}")
else:
    print(f"  {YELLOW}cd {script_dir} && source .venv/bin/activate{RESET}")
print(f"{BLUE}{BOLD}==================================================={RESET}")