from setuptools import setup, find_packages

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
