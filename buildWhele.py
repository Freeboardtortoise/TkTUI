import os
import subprocess

setup_py = '''from setuptools import setup, find_packages

setup(
    name="cursesui",
    version="0.1.0",
    author="Freeboardtortoise",
    author_email="Freeboardtortoise@gmail.com",
    description="Tkinter-like themed UI framework for curses",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cursesui",
    packages=find_packages(),
    python_requires='>=3.6',
)
'''

pyproject_toml = '''[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
'''

def main():
    with open("setup.py", "w") as f:
        f.write(setup_py)
    with open("pyproject.toml", "w") as f:
        f.write(pyproject_toml)

    subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "build", "wheel", "setuptools"], check=True)
    subprocess.run(["python3", "-m", "build"], check=True)

if __name__ == "__main__":
    main()
