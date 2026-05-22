import os
import platform
import sys
from pathlib import Path


python_verison = platform.python_version()
print(f'Python version: {python_verison}')

if sys.version_info < (3,8):
    sys.exit("Python 3.8 or higher is required to run this script")

print(f'Python version is compatible to run script {python_verison}')

script_dir = Path(__file__).parent / 'project-setup'
if not script_dir.exists():
    script_dir.mkdir()
    print(f'Created directory: {script_dir}')
else:
    print(f'Directory already exists: {script_dir}')

sub_folder = ['src', 'tests', 'docs', 'logs']

for folder in sub_folder:
    folder_path = script_dir / folder
    if not folder_path.exists():
        folder_path.mkdir()
        print(f'Created folder: {folder}')
    else:
        print(f'Folder already exists: {folder}')



basic_packages = [
    "requests>=2.31.0",
    "pandas>=2.1.0",
    "python-dotenv>=1.0.0",
    "pytest>=7.4.0"
]

requirements_file = script_dir / 'requirements.txt'
requirements_file.write_text("\n".join(basic_packages) + "\n", encoding="utf-8")
print(f'Created requirements.txt with basic packages at: {requirements_file}')

gitignore_path = script_dir / '.gitignore'

gitignore_content = gitignore_content = """# Byte-compiled
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

gitignore_path.write_text(gitignore_content, encoding='utf-8')
print(f"Generated: {gitignore_path}")

