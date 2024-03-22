import os
import subprocess
import sys

def setup_venv():
    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

    print("Activating virtual environment...")
    if sys.platform == "win32":
        venv_activate = os.path.join(venv_dir, "Scripts", "activate")
        subprocess.run(f"cmd /c {venv_activate}", shell=True, check=True)
    else:
        venv_activate = os.path.join(venv_dir, "bin", "activate")
        subprocess.run(f"source {venv_activate}", shell=True, check=True)
    print("Virtual environment activated.")

    print("Installing requirements...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    print("Requirements installed.")

if __name__ == "__main__":
    setup_venv()