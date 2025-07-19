#!/usr/bin/env python3
"""
Setup script for Poetype application
"""
import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def main():
    """Main setup function"""
    print("Setting up Poetype application...")
    
    # Check if virtual environment exists
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("Creating virtual environment...")
        if not run_command("python -m venv .venv", "Create virtual environment"):
            sys.exit(1)
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        pip_cmd = ".venv\\Scripts\\pip"
        python_cmd = ".venv\\Scripts\\python"
    else:  # Unix/Linux/macOS
        pip_cmd = ".venv/bin/pip"
        python_cmd = ".venv/bin/python"
    
    # Install dependencies
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Install dependencies"):
        sys.exit(1)
    
    # Create instance directory if it doesn't exist
    instance_path = Path("instance")
    instance_path.mkdir(exist_ok=True)
    
    # Copy environment file if it doesn't exist
    env_file = Path(".env")
    env_example = Path("env.example")
    if not env_file.exists() and env_example.exists():
        import shutil
        shutil.copy(env_example, env_file)
        print("✓ Created .env file from env.example")
    
    print("\nSetup completed successfully!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    print("2. Initialize database: flask init-db")
    print("3. Populate database: flask populate-db")
    print("4. Run the application: python app.py")


if __name__ == "__main__":
    main() 