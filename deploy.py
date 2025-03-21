import subprocess

def install_dependencies():
    """Install required dependencies from requirements.txt."""
    print("Installing dependencies...")
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        exit(1)

if __name__ == "__main__":
    install_dependencies()
